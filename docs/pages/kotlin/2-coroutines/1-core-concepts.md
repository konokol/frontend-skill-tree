# 核心概念

Kotlin 中的协程的本质是一套依靠编译器（CPS 与状态机）和上层官方的协程库（kotlinx.coroutines）实现的轻量级并发框架。解决了传统异步编程中的三个痛点问题：

- **可读性** 通过挂起/恢复机制消除了回调地狱，用写同步代码的方式写异步代码；
- **安全性** 通过结构化并发将异步任务绑定到特定的生命周期作用域内，父子任务联动，从机制上消除了异步失控导致的内存泄漏和状态错乱；
- **高性能** 协程挂起时并不会阻塞底层操作系统的线程，通过少量的线程池就能完成大量的并发任务，从而减少了线程创建、销毁、上下文切换带来的性能开销。

基于这些价值，Kotlin 协程在日常使用和底层实现中主要包含六大核心概念：挂起函数、协程构建器、协程作用域、协程上下文、协程调度器、Job。

## 挂起函数（suspend）

挂起函数是用 `suspend` 关键字修饰的函数，它是 Kotlin 协程中的核心语言特性。

```kotlin
suspend fun foo(url: String): Result {
    // ...
}
```

**非阻塞式暂停**  

挂起函数的特点是能在挂起点（比如 withContext 调用的网络请求、delay等）处暂停并且释放当前线程的控制权，不阻塞当前线程，当异步结果就绪之后，在挂起点处恢复。

**调用限制**  

只能在协程代码块内部或者其他的挂起函数中调用。

```kotlin
suspend fun fetchDocs() {
    val result = get("https://developer.android.com") // ✅ 调用正常
    show(result)
}

fun checkConnect() {
    val result = get("https://developer.android.com") // ❌ 编译错误 Suspend function 'fun checkConnect()' can only be called from a coroutine or another suspend function.
}

suspend fun get(url: String) = withContext(Dispatchers.IO) {
    /* ... */
}
```

**挂起/恢复的工作流程**  

挂起（Suspend）：当遇到耗时操作时，当前协程的局部状态（局部变量、执行进度）会被保存下来，函数提前返回（返回一个特殊标记 COROUTINE_SUSPENDED），释放底层资源。

恢复（Resume）：当后台耗时操作（如 I/O 线程的网络请求）完成后，系统会通过回调触发恢复逻辑，将协程重新调度回指定线程，带着返回结果从上次暂停的下一行代码继续往下执行。

## 协程构建器（Coroutine Builders）

协程构建器是用来创建和启动协程的函数，通常协程构建器是 `CoroutineScope` 的扩展函数，常见的协程构建器有 `CoroutineScope.launch`、`CoroutineScope.async`、`runBlocking`。

还有一个 `withContext`，尽管它不是协程构建器，也经常放在一起讲，它是一个挂起函数，不会启动新的协程，仅用来。

| 构建器 | 所属包层级 | 返回值类型 | 是否阻塞当前线程 | 异常处理机制 | 核心适用场景 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`CoroutineScope.launch`** | `kotlinx.coroutines` | `Job` | 否（异步非阻塞） | 立即向父协程传播（未捕获会直接导致崩溃） | 不需要返回结果的“发射后不管”任务（如更新 UI、写日志）。 |
| **`CoroutineScope.async`** | `kotlinx.coroutines` | `Deferred<T>` | 否（异步非阻塞） | 暂存在 `Deferred` 中，调用 `await()` 时抛出（同时也会向上传播） | 需要获取异步结果，或多个独立接口并发聚合。 |
| **`runBlocking`** | `kotlinx.coroutines` | `T`（闭包最后一行结果） | **是（阻塞当前物理线程）** | 直接向外部调用线程抛出 | **仅限单元测试**或 `main` 函数入口，**严禁在 Android 主线程使用**。 |
| **`withContext`** | **挂起函数** (`kotlinx.coroutines`) | `T`（直接返回最后一行结果） | 否（**串行**非阻塞挂起） | 直接在当前调用栈向上抛出（可用常规 `try-catch` 捕获） | **单任务的线程切换**（如在主线程中切到 `Dispatchers.IO` 执行耗时操作后切回）。 |

**协程的启动模式**  

```kotlin
public fun CoroutineScope.launch(
    context: CoroutineContext = EmptyCoroutineContext,
    start: CoroutineStart = CoroutineStart.DEFAULT,
    block: suspend CoroutineScope.() -> Unit
): Job {
    val newContext = newCoroutineContext(context)
    val coroutine = if (start.isLazy)
        LazyStandaloneCoroutine(newContext, block) else
        StandaloneCoroutine(newContext, active = true)
    coroutine.start(start, coroutine, block)
    return coroutine
}
```

```kotlin
public fun <T> CoroutineScope.async(
    context: CoroutineContext = EmptyCoroutineContext,
    start: CoroutineStart = CoroutineStart.DEFAULT,
    block: suspend CoroutineScope.() -> T
): Deferred<T> {
    val newContext = newCoroutineContext(context)
    val coroutine = if (start.isLazy)
        LazyDeferredCoroutine(newContext, block) else
        DeferredCoroutine<T>(newContext, active = true)
    coroutine.start(start, coroutine, block)
    return coroutine
}
```

`CoroutineScope.launch` 和 `CoroutineScope.async` 函数有一个 start 参数，使用 `launch` 和 `async` 启动协程时，都可以用 start 参数来控制协程的调度方式。CoroutineStart 有四种启动模式：

- **CoroutineStart.DEFAULT（默认）** 立即根据调度器安排执行，如果在开启执行前已经调用了 `cancel()`，则直接进入取消状态。
- **CoroutineStart.LAZY（懒加载）** 创建后处于新建状态，直到调用 `job.start()`、`job.join()`、`deferred.async()`才会开始执行。• 如果连续调用两个惰性 `async` 再分别 `await()`，就会退化成串行执行。
- **CoroutineStart.ATOMIC（原子启动）** 立即执行，和默认模式不同的是，在执行到第一个挂起点之前不能被取消，保证初始化代码块一定能执行。
- **CoroutineStart.UNDISPATCHED（无调度启动）** 立即在当前线程上执行协程块中的代码，遇到第一个挂起点之后才切换到指定的 Diaptcher（Dispatch.Main.immediate思想类似，可以减少一次handle.post()调度）。

## 协程作用域（CoroutineScope）

协程作用域是追踪和管理协程生命周期的容器，是结构化并发在代码层面的体现。Kotlin 中的协程必须在某个作用域（CoroutineScope）内启动，从而保证
了每个协程都有明确的生命周期归属。

### 核心原则（结构化并发的体现）

在作用域内或者协程内部启动子协程时，他们会形成树形结构，遵循核心原则：

- **上下文继承**，子协程会继承父协程的所有上下文，同时创建新的 Job 挂载到父协程上；
- **父等子**，父作用域内的代码执行完之后，会等待子协程全部执行完再结束父协程
- **取消向下传递**，调用 `scope.cancel()` 取消父作用域之后，该作用域下的所有子协程都会被取消
- **异常向上传递**，默认行为中，子协程出现异常没有处理，会传递给父作用域，父作用域取消自身，从而取消父作用域内的所有子协程

### 作用域的构成

```kotlin
public interface CoroutineScope {
    public val coroutineContext: CoroutineContext
}
```

CoroutineScope 是一个接口，持有一个上下文对象。协程作用域本身不执行代码，但是它持有生命周期管理器（Job）、调度器（Dispatchers）、协程名（CoroutineName）、异常处理器（CoroutineExceptionHandler），这些都是协程上下文。

```kotlin
CoroutineScope(
    SupervisorJob() +  // 生命周期管理器
    Dispatchers.IO +  // 调度器
    CoroutineName("user") + // 协程名称
    CoroutineExceptionHandler() { _, _ -> } // 异常处理器
    )
```

### 作用域与父子协程的关系

**父子作用域的树形结构是如何构成的？**

在启动子协程（比如调用 launch）时，从当前的上下文中取出 Job 作为父 Job，新协程的 Job 会添加到父协程的 children 列表中，从而形成 Job 树。

取消的时候，也跟根据这个父子 Job 树来管理协程。

### 常见的协程作用域

**全局作用域 GlobalScope**  

```kotlin
GlobalScope.launch {
    // 生命周期与进程一致
}
```

全局单例的作用域，生命周期和进程一致，没有父 Job。很容易内存泄漏，除了需要用到全局状态的情况（比如全局进程状态的上报），一般不使用。

**Android 生命周期作用域**  

- viewModelScope 绑定 ViewModel 的生命周期，`onClear()`时取消；
- lifecycleScope 绑定 Fragment/Activity 的生命周期，`onDestroy()`时取消；
- repeatOnLifecycle 绑定 Lifecycle 的状态，低于指定状态时取消收集。

**挂起函数作用域 coroutineScope/supervisorScope**  

```kotlin
suspend fun load() = coroutineScope {
    launch { fetchA() }
    launch { fetchB() }
    // 等待所有子协程完成
}
```

用于在挂起函数中启动子协程，非阻塞式，等待子协程完成之后，当前函数才会返回。差异点是 `coroutineScope` 出现未处理异常时会取消所有协程，`supervisorScope` 出现异常时不会影响到兄弟协程。

`supervisorScope` 适用于页面多个独立模块并发加载，其中一个模块失败不影响别的模块。

**自定义作用域**  

```kotlin
val scope = CoroutineScope(SupervisorJob() + Dispatchers.IO)
scope.launch { ... }
scope.cancel() // 手动取消
```

需要手动管理生命周期，适用于封装独立的业务管理类，常配合 `SupervisorJob` 隔离异常。

## 协程上下文（CoroutineContext）

协程上下文是协程运行的环境信息的集合，它包含了 Job、Dispatcher、CoroutineName、CoroutineExceptionHandler。CoroutineContext 的数据结构是一个索引不可变的集合，重载了 `+`，可以和其他上下文一起组合成新的上下文。

```kotlin
public interface CoroutineContext {
    public operator fun <E : Element> get(key: Key<E>): E?
    public fun <R> fold(initial: R, operation: (R, Element) -> R): R
    public operator fun plus(context: CoroutineContext): CoroutineContext
    public fun minusKey(key: Key<*>): CoroutineContext

    public interface Element : CoroutineContext {
        public val key: Key<*>
    }

    public interface Key<E : Element>
}
```

### 常见的上下文元素

- **Job** 管理协程，控制协程的启动、等待、取消，并维系结构化并发的父子层级树。
- **Dispatcher** 调度器，决定协程在哪个线程上运行
- **CoroutineName** 协程名，常用来打日志或者调试
- **CoroutineExceptionHandle** 异常处理器，用来处理根协程未捕获异常

### 底层实现

CoroutineContext 提供了四个核心的操作：

- get（即[]），按 Key 访问，例如 `val job = context[Job]`；
- plus（+运算符），合并两个上下文并返回新上下文，如果有相同的 Key，右值会覆盖左侧元素。合并时，有一个优化，ContinuationInterceptor（即调度器的 Dispatcher）会被调整到链表的末端，每次挂起恢复的时候都需要访问，这样可以快速命中；
- minusKey，移除指定 Key 对应的元素，都移除完了会返回一个 EmptyCoroutineContext；
- fold，按顺序遍历集合中的所有元素；

`CoroutineContext` 的底层实现是一个链表，拼接元素时，底层会构建一个名为 `CombinedContext` 的链表，上面的这些操作就是沿着链表来操作的。

```kotlin
internal class CombinedContext(
    private val left: CoroutineContext,
    private val element: Element
) : CoroutineContext, Serializable {

    override fun <E : Element> get(key: Key<E>): E? {
        var cur = this
        while (true) {
            cur.element[key]?.let { return it }
            val next = cur.left
            if (next is CombinedContext) {
                cur = next
            } else {
                return next[key]
            }
        }
    }
}
```

### 自定义上下文

自定义上下文只需要继承 AbstractCoroutineContextElement，并且在内部定义一个伴生对象作为唯一的 Key 即可。

```kotlin
import kotlin.coroutines.AbstractCoroutineContextElement
import kotlin.coroutines.CoroutineContext
import kotlin.coroutines.coroutineContext

// 1. 继承 AbstractCoroutineContextElement，传入自定义的 Key
class TraceContext(val traceId: String) : AbstractCoroutineContextElement(TraceContext) {
    // 2. 定义伴生对象实现 CoroutineContext.Key，充当唯一索引
    companion object Key : CoroutineContext.Key<TraceContext>
}

// 3. 在挂起函数中随时提取（无需层层传参）
suspend fun fetchUserProfile() {
    val traceId = coroutineContext[TraceContext]?.traceId ?: "unknown"
    println("当前请求链路 ID: $traceId")
}

// 4. 启动协程时像普通元素一样通过 '+' 号注入
fun startRequest(scope: CoroutineScope) {
    scope.launch(Dispatchers.IO + TraceContext("REQ-20261123-8899")) {
        fetchUserProfile() // 自动继承父协程的 TraceContext
    }
}
```

自定义上下文的一些使用场景：

1. 全局 Loading/弹窗 的状态控制，比如同一个请求，第一次进页面需要展示loading，下拉刷新的时候展示刷新，如果用参数控制，需要把参数一层层传递。通过自定义上下文就能让简化函数调用，`LoadingConfigContext(val showLoading: Boolean, val cancelable: Boolean)`。
2. 端到端链路监控，比如某一个业务流程很长，可以在入口地方自定义一个上下文记录上来源等信息，`UserActionContext(actionId = UUID, sourcePage = "HomeBanner")`，可以很方便把整条链路串联起来。
3. 统一的错误信息提示与降级策略，比如在网络请求失败时，有的场景下弹Toast、有的不需要提示，可以结合自定义的 CoroutineExceptionHandler，定义自定义的上下文 `ErrorPolicyContext(val silent: Boolean, val customErrorHandler: ((Throwable) -> Unit)?)`，在请求中捕获异常时直接从上下文中获取错误处理策略。

### 进阶用法（跨线程绑定 TheadLocal）

ThreadLocal 的设计本身是为了做线程隔离，但是在协程中，由于协程可能在不同线程中执行，可能会出现状态丢失或状态错乱的问题。

1. 状态丢失，线程 A 设置了 threadLocal.set("AAA")，在协程中通过 `withContext(Dispatcher.IO)` 切到了线程 B，则在线程 B 中获取 threadLocal.get() 值为 null。
2. 状态错乱，线程 A 设置了 threadLocal.set("AAA")，挂起后线程被复用去执行别的任务，在其他任务中可能获取到残留的状态。

为了解决这个问题，可以用扩展函数 `ThreadLocal<T>.asContextElement`，返回一个 ThreadLocalElement 对象，里面有 `updateThreadContext(context: CoroutineContext)` 和 `restoreThreadContext(context: CoroutineContext, oldState: T)`。当协程在当前线程执行完一段代码、即将挂起或切换走时，框架自动调用这两个方法，用来更新和恢复值。

```kotlin
public fun <T> ThreadLocal<T>.asContextElement(value: T = get()): ThreadContextElement<T> =
    ThreadLocalElement(value, this)
```

**使用限制**  

`asContextElement` 只追踪 CoroutineContext 传入的值，如果在协程内部调用 threadLocal.set("B") 方法，值并不会被同步回来，正确做法是用 `withContext(userThreadLocal.asContextElement("B"))` 来更新上下文元素。

## Job

Job 是用来管理协程生命周期的，也是结构化并发树形结构中的核心节点。使用 launch 和 async 启动协程都会返回一个 Job 对象（async 返回的 `Deferred<T>` 也是Job的子类）。

```kotlin
public interface Job : CoroutineContext.Element {
    public val children: Sequence<Job>
    public val parent: Job?
    public val isActive: Boolean
    public val isCompleted: Boolean
    public val isCancelled: Boolean
    public fun start(): Boolean
    public fun cancel(cause: CancellationException? = null)
    public suspend fun join()
    public fun invokeOnCompletion(handler: CompletionHandler): DisposableHandle
}
```

### Job的核心操作

**启动协程`start()`**

启动协程，懒加载的协程不会立即开始调度，调用 **job.start()** 之后会开始调度。

**取消协程 `cancel()/cancelAndJoin()`**

`cancel()` 是取消协程，并抛出 CancellationException 异常。

`cancelAndJoin()` 取消并等待完成，等价于 `cancel()` + `join()`。

**等待 `join()/joinAll()/await()`**

`join()` 挂起等待 Job 完成，不返回结果。如果 Job 已经取消，直接返回，不抛异常。

`joinAll(vararg jobs: Job)` 等待多个 Job 完成，等价于逐个 `join()`

`await()` Deferred 的方法，会返回结果，如果有异常会抛异常。

**完成回调 `invokeOnCompletion { cause -> ... }: DisposableHandle`**

Job 完成时会调用，回调参数中 cause 为 null 表示正常结束，CancellationException 表示被取消，其他的是异常。返回 DisposableHandle，'handle.dispose()'可以取消回调。

invokeOnCompletion 经常用来做资源清理、日志记录，或者监听协程的状态。

### Job 的状态机

一个 Job 在生命周期中会经过六个状态，通过 `isActive`、`isCompleted`、`isCancelled` 三个状态标记。

| 状态 | 触发条件 | `isActive` | `isCompleted` | `isCancelled` |
| --- | --- | --- | --- | --- |
| `New`（新建） | 使用 `CoroutineStart.LAZY` 创建，尚未调用 `start()` 或 `join()` | `false` | `false` | `false` |
| `Active`（活跃） | 默认创建后立即进入，或 `New` 状态调用 `start()` 后 | `true` | `false` | `false` |
| `Completing`（完成中） | 自身代码已执行完毕，但正在等待名下子协程全部完成 | `true` | `false` | `false` |
| `Cancelling`（取消中） | 调用了 `cancel()` 或抛出未捕获异常，正在执行 `finally` 清理和取消子协程 | `false` | `false` | `true` |
| `Cancelled`（已取消） | 取消清理工作及所有子协程均已结束（最终态） | `false` | `true` | `true` |
| `Complete`（已完成） | 自身代码与所有子协程均正常执行结束（最终态） | `false` | `true` | `false` |

在 Completing（等子协程）期间，isActive 依然为 true；一旦触发取消进入 Cancelling，isActive 会立刻变为 false，而 isCancelled 立刻变为 true。

### 几种不同的 Job

**普通 Job**  

通过 `CoroutineScope.launch` 创建，无法返回结果，发生异常时立即向上抛出，父 Job 接受到异常后立即取消自己，同时连带也会取消异常 Job 的兄弟 Job。

**`Differed<T>`**  

继承自 Job，多了await方法。通过 `CoroutineScope.async` 方法创建，调用 `differed.await()` 获取结果。发生异常时不会立即抛出，会在调用`await()` 时才抛出。

```kotlin
// Job：不关心结果
val job = scope.launch { doWork() }

// Deferred：需要结果
val deferred = scope.async { fetchData() }
val result = deferred.await()
```

**SupervisorJob**  

```kotlin
public fun SupervisorJob(parent: Job? = null): CompletableJob
```

和普通 Job 的区别是，发生异常时，不会向上继续传递异常影响到兄弟 Job，仅终止当前 Job。

```kotlin
public class SupervisorJobImpl(parent: Job?) : JobImpl(parent) {
    override fun childFailed(child: Job, cause: Throwable) = false // 直接返回 false 不取消自己，也告诉子协程当前未处理取消
}
```

### Job 的底层实现

Job 的核心实现是 JobSupport，本质上是一个基于 CAS 的无锁状态机，状态都存在 `_state` 字段中。

``` kotlin
public open class JobSupport(active: Boolean) : Job, ChildJob, ParentJob {
    // 状态机：用 _state 字段保存状态
    private val _state = atomic<Any?>(if (active) EMPTY_ACTIVE else EMPTY_NEW)
}
```

关键实现机制：

**状态转换**  

协程状态变更时，内部都会开启一个 `loopOnState` 的自旋循环，读取当前的 `_state`，计算目标状态，通过 CAS 原子替换 `_state`。

```kotlin
    private inline fun loopOnState(block: (Any?) -> Unit): Nothing {
        while (true) {
            block(state)
        }
    }
```

**父子关联**  

建立关联：子协程启动时，会在父 Job 的 `NodeList` 中插入一个 `ChildHandleNode`，同时子协程持有 `parentHandle`。

向下取消：父 Job 调用 `cancel()`时，遍历自己的 `NodeList`，通知所有的 `ChildHandleNode` 调用 `childJob.parentCancelled(parentJob)`。

向上处理异常：子 Job 发生异常时，通过 `parentHandler` 回调父 Job 的 `onChildCanceled(cause)`

## 协程调度器（Dispatcher）

---

*参考*  

[1] Android Developers. [Android 上的协程](https://developer.android.google.cn/kotlin/coroutines?hl=zh-cn). Accessed 2026-11-17.  
[2] Kotlin 中文文档. [协程指南](https://book.kotlincn.net/text/coroutines-guide.html). Accessed 2026-11-17.  
[3] Open AIDoc. [协程指南](https://openaidoc.org/kotlin/coroutines-guide). Accessed 2026-11-17.  
