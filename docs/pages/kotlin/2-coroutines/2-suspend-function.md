# 挂起函数

挂起函数指的是用 `suspend` 关键字修饰的函数，它赋予了函数“在不阻塞当前底层线程的前提下暂停执行，并在异步结果就绪后从断点恢复执行”的能力。

挂起函数只能在协程内部或者其他挂起函数中调用。

## 挂起（suspend） vs 阻塞（block）

- **阻塞**（如 Thread.sleep()、传统同步 I/O）：当前操作系统线程被死死占用并进入休眠，无法执行任何其他任务，造成线程资源浪费。
- **挂起**（如 delay()、withContext()）：协程主动保存当前执行进度与局部变量后直接退出当前函数调用栈，释放底层线程去执行其他任务；等外部耗时任务完成后，再由调度器将后续代码重新派发到线程上继续执行。

## suspend 关键字的本质作用

挂起函数本身并没有线程切换的能力，仅在普通函数前面加上 `supspend` 关键字并不会让函数体中的代码变成异步执行。`suspend` 关键字本质上只是一个标记，说明函数内的代码可能会异步支持，它约束了异步代码的边界，由于挂起函数只能在协程内部和其他挂起函数中调用，保证了异步代码的最上层一定在一个作用域内。

直接给普通函数加 `suspend` 关键字，这个函数不会变成异步，它只是一个伪挂起函数。如果在 IDE 中写代码，IDE 还会提示 `suspend` 关键字是多余的。

```kotlin
// ⚠️ Redundant 'suspend' modifier
suspend fun sum(n: Int) : Int {
    return List(n) { it + 1 }.sum()
}
```

## 原理

对于挂起函数，编译器会特殊处理，编译生成的字节码中，会对挂起函数做两件事情：

- **改写函数签名** 给函数追加一个 `Continuation<T>` 参数，同时将返回值修改成 Any?。
- **生成状态机** 给挂起函数生成一个状态机

### CPS 转换

CPS（Continuation-Passing Style，续体传递风格）转换是一种在编译期的转换，它将传统的函数中“函数直接返回结果”改写成“函数接收一个回调，通过回调传递结果”。

挂起函数编译的字节码中，通过给函数追加 `Continuation<T>` 参数，并将返回值修改成 `Any?` 来实现。返回值是 `Any?` 而不是 `Unit` 是因为函数如果同步很快能得到结果，就直接返回结果，如果需要挂起，会返回 `COROUTINE_SUSPENDED`。

举一个例子：

```kotlin
// 开发者编写的 Kotlin 代码（看似同步）
suspend fun fetchOrder(): List<Order> {
    val user = api.getUser()   // 挂起点 1
    val orders = api.getOrders(user.id) // 挂起点 2
    return orders
}
```

编译之后的函数签名就变成：

```java
// 编译器对 fetchOrder() 进行 CPS 变换后的字节码等价签名：
public static final Object fetchOrder(Continuation<? super List<Order>> completion) {...}
```

### Continuation

在 `kotlinx.coroutines` 中，Continuation 定义很简单：

```kotlin
public interface Continuation<in T> {
    // 1. 当前协程的运行环境配置（调度器、Job、异常处理器等）
    public val context: CoroutineContext

    // 2. 唤醒并恢复协程执行的唯一入口
    public fun resumeWith(result: Result<T>)
}
```

Continuation 代表的是挂起后恢复执行的入口，挂起时保存 Continuation，恢复时调用 `resumeWith()`，每一个挂起点对应一个 `Continuation`。比如上面的例子上，两个挂起点分别生成了一个Continuation对象。

### 状态机

编译器会给每个挂起函数生成一个继承自 `ContinuationImpl` 的状态机类：

- lable 用来表示执行到哪个挂起点中
- result 存放每个挂起点返回的结果
- 临时变量 挂起点活跃的临时变量会被提升成成员变量

在函数体中，根据挂起点将函数分成多段，每一段对应 lable 中的一个case。如果挂起点挂起了，就会返回 COROUTINE_SUSPENDED，立即释放当前的线程，当挂起点恢复时，通过 `resumeWith()` 最终再次调入 `invokeSuspend()`，进入下一个label中执行，从而实现了挂起和恢复。

```java
// 编译器为 fetchOrder() 生成的等价 Java 状态机代码：
public static final Object fetchOrder(Continuation<? super List<Order>> completion) {
    final class FetchOrderSM extends ContinuationImpl {
        int label;      // 状态标签：0=初始，1=getUser恢复，2=getOrders恢复
        Object result;  // 暂存子挂起函数传回的结果

        FetchOrderSM(Continuation<? super List<Order>> c) { super(c); }

        @Override
        public final Object invokeSuspend(Object res) {
            this.result = res;
            this.label |= Integer.MIN_VALUE;
            return fetchOrder(this); // 异步完成时，带着保存了状态的状态机重入原函数！
        }
    }

    FetchOrderSM sm = (completion instanceof FetchOrderSM)
        ? (FetchOrderSM) completion : new FetchOrderSM(completion);
    Object suspended = IntrinsicsKt.getCOROUTINE_SUSPENDED();

    switch (sm.label) {
        case 0: // === 阶段 0：初始执行，准备调用挂起点 1 ===
            ResultKt.throwOnFailure(sm.result);
            sm.label = 1; // 关键：在发起挂起前，先把进度标记推进到 1
            Object res1 = api.getUser(sm); // 把状态机自己（sm）作为续体传入
            if (res1 == suspended) {
                return suspended; // 发生挂起，直接退出调用栈释放当前线程！
            }
            sm.result = res1; // 若命中缓存未挂起，直接穿透进入 case 1

        case 1: // === 阶段 1：从 getUser() 恢复，准备调用挂起点 2 ===
            ResultKt.throwOnFailure(sm.result);
            User user = (User) sm.result; // 取出 getUser() 返回的 User 对象
            
            sm.label = 2; // 推进进度标记到 2
            Object res2 = api.getOrders(user.getId(), sm); // 继续把 sm 传入挂起点 2
            if (res2 == suspended) {
                return suspended; // 再次挂起，释放线程！
            }
            sm.result = res2;

        case 2: // === 阶段 2：从 getOrders() 恢复，返回最终结果 ===
            ResultKt.throwOnFailure(sm.result);
            List<Order> orders = (List<Order>) sm.result; // 取出 getOrders() 返回的订单列表
            return orders;                                // 全部执行完毕，返回最终结果！
    }
    throw new IllegalStateException();
}
```

### 挂起与恢复的流程

以上面的例子分析，在主线程调用 fetchOrder()

```kotlin
// 场景设定：在 Main 线程启动协程调用 fetchOrder()
viewModelScope.launch(Dispatchers.Main) {
    val orders = fetchOrder() // <--- 入口
    updateUI(orders)
}

suspend fun fetchOrder(): List<Order> {
    val user = api.getUser()            // 挂起点 1
    val orders = api.getOrders(user.id) // 挂起点 2
    return orders
}

```

整个挂起恢复的流程如下：

```text
[Main 线程] 调用 fetchOrder(outerCont)
   │
   ├─► 创建状态机 sm (label = 0)
   ├─► 执行 case 0：设置 sm.label = 1 ──► 调用 api.getUser(sm)
   └─► 收到 COROUTINE_SUSPENDED ──► 直接 return 出栈！（Main 线程立刻自由去画 UI）
                                           │
                                           ▼ （后台网络耗时 300ms）
                                    [IO 线程] getUser 拿到 User
                                           │
                                           ▼ 调用 sm.resumeWith(user)
[Main 线程] ◄── Handler.post 切回主线程 ───┘
   │
   ├─► 触发 sm.invokeSuspend(user) ──► 重入 fetchOrder(sm)
   ├─► 命中 case 1 (因 label == 1)：拿到 user，设置 sm.label = 2 ──► 调用 api.getOrders(user.id, sm)
   └─► 收到 COROUTINE_SUSPENDED ──► 再次 return 出栈！（Main 线程再次自由）
                                           │
                                           ▼ （后台网络耗时 200ms）
                                    [IO 线程] getOrders 拿到 List<Order>
                                           │
                                           ▼ 调用 sm.resumeWith(orders)
[Main 线程] ◄── Handler.post 切回主线程 ───┘
   │
   ├─► 触发 sm.invokeSuspend(orders) ──► 重入 fetchOrder(sm)
   ├─► 命中 case 2 (因 label == 2)：拿到 orders，执行 return orders
   └─► 调用 outerCont.resumeWith(orders) ──► 唤醒外层协程执行 updateUI(orders)！
```

## 高级用法

**1.桥接回调封装回调式交互**  

客户端业务逻辑中经常有链式回调的写法，比如权限请求、交互式的确认弹窗、三方 SDK 的回调等，直接写就会层层嵌套。利用  suspendCancellableCoroutine/suspendCoroutine 可以将异步的调用代码变成同步的形式。

```kotlin
// 1. 封装一个“挂起式确认弹窗”：挂起当前协程等待用户点击，若界面销毁则自动 dismiss 防 WindowLeaked
suspend fun FragmentActivity.awaitUserConfirmation(title: String, message: String): Boolean =
    suspendCancellableCoroutine { cont ->
        val dialog = AlertDialog.Builder(this)
            .setTitle(title)
            .setMessage(message)
            .setPositiveButton("确认") { _, _ ->
                if (cont.isActive) cont.resume(true)
            }
            .setNegativeButton("取消") { _, _ ->
                if (cont.isActive) cont.resume(false)
            }
            .setOnCancelListener {
                if (cont.isActive) cont.resume(false)
            }
            .create()

        // 页面销毁（lifecycleScope 取消）时，自动关闭弹窗，杜绝内存泄漏
        cont.invokeOnCancellation { dialog.dismiss() }
        dialog.show()
    }

// 2. 业务层调用：
suspend fun startCheckoutFlow(activity: FragmentActivity) {
    val agreed = activity.awaitUserConfirmation("海外购提示", "跨境商品不支持无理由退货，是否继续？")
    if (!agreed) return // 用户点取消，直接优雅退出，无需多层嵌套
    
    val orderResult = orderRepository.submitOrder()
    navigateToPayment(orderResult)
}
```

`suspendCancellableCoroutine` 获取一个可取消的续体 `CancellableContinuation<T>`，挂起当前协程释放线程；当外部回调触发时，调用 `resume()` 或 `resumeWithException()` 唤醒协程，并通过 `invokeOnCancellation` 绑定生命周期取消动作。

`suspendCancellableCoroutine` 是一次性桥接，使用时需要注意：

1. **必须注册 `invokeOnCancellation`**：只要底层 SDK 提供了 `cancel()`、`removeListener()` 或 `dismiss()` 方法，就必须写进 `invokeOnCancellation` 中，实现结构化并发联动。
2. **严禁重复调用 `resume`**`：CancellableContinuation` 只能被唤醒一次，第二次调用会直接抛出 `IllegalStateException: Already resumed`。面对不可控的三方回调，务必加上 `if (continuation.isActive)` 保护。
3. **优先用 `suspendCancellableCoroutine` 而非 `suspendCoroutine`**：前者支持协程取消与资源清理，后者会死等回调导致内存泄漏。

**2.请求合并与并发去重（Single-Flight 模式，防缓存击穿与重复请求）**  

业务场景：进入复杂首页时，顶部 Banner 组件、个人中心卡片、底部弹窗组件几乎在同一毫秒调用了同一个挂起函数 `suspend fun getUserProfile()`。如果不做防重入处理，底层会同时发出 3 个一模一样的 HTTP 请求，浪费用户流量且容易引发状态竞态。

高级解法：Mutex + 飞行中任务引用（Deferred） 实现客户端 Single-Flight 模式——第一个调用者发起请求，后续同时进来的调用者直接挂起复用同一个 `Deferred` 结果，请求结束后自动清理。

```kotlin
class UserRepository(private val api: UserApi) {
    private val mutex = Mutex()
    private var inFlightRequest: Deferred<UserProfile>? = null

    suspend fun getUserProfileDedup(): UserProfile = coroutineScope {
        val deferred = mutex.withLock {
            // 如果当前已经有正在进行的请求，直接复用它（注意：只复用活跃未取消的）
            inFlightRequest?.takeIf { it.isActive } ?: async {
                try {
                    api.fetchUserProfile()
                } finally {
                    // 请求无论成功或失败，结束后清空引用
                    mutex.withLock { inFlightRequest = null }
                }
            }.also { inFlightRequest = it }
        }
        // 所有并发调用者都在这里挂起等待同一个结果
        deferred.await()
    }
}

```

**3.高阶挂起函数：弱网环境下的“指数退避重试”（Exponential Backoff）**  

客户端痛点：弱网情况下，会有网络抖动。直接在挂起函数里写 `while` 死循环重试会瞬间打爆客户端电量与服务端网关；若用 `runCatching` 捕获异常，还极易误吞 `CancellationException` 导致页面退出后仍在后台死循环重试。

高级解法：编写带泛型、退避延迟、取消安全校验的通用高阶挂起重试器：

```kotlin
suspend inline fun <T> retryWithBackoff(
    times: Int = 3,
    initialDelayMs: Long = 500L,
    maxDelayMs: Long = 5000L,
    factor: Double = 2.0,
    block: suspend () -> T
): T {
    var currentDelay = initialDelayMs
    repeat(times - 1) { attempt ->
        try {
            return block()
        } catch (e: Throwable) {
            // 【核心铁律】：如果是协程被取消，必须立刻向上抛出，绝不能当作网络失败去重试！
            if (e is CancellationException) throw e
            // 如果是客户端 4xx 业务参数错误，重试无意义，直接抛出
            if (e is HttpException && e.code() in 400..499) throw e
        }
        delay(currentDelay) // 非阻塞挂起等待
        currentDelay = (currentDelay * factor).toLong().coerceAtMost(maxDelayMs)
    }
    return block() // 最后一次尝试，若仍失败则直接抛出异常
}

// 业务层调用：一行代码赋予任何挂起函数弱网自愈能力
val config = retryWithBackoff(times = 3) { remoteConfigApi.fetchConfig() }
```

**4.客户端异常安全封装：suspendRunCatching（规避 runCatching 吞掉取消异常大坑）**  

客户端痛点：Kotlin 标准库的 `runCatching { ... }` 内部捕获的是顶级 `Throwable`。在挂起函数中使用 `runCatching` 时，如果用户退出页面触发了 `CancellationException`，它会被 `runCatching` 默默捕获并装进 `Result.failure` 中，导致协程取消信号失效、后续 UI 更新代码继续执行引发空指针崩溃！

高级解法：在客户端基础架构层定义专用的挂起安全包装器，遇到 `CancellationException` 自动重新抛出：

```kotlin
suspend inline fun <R> suspendRunCatching(crossinline block: suspend () -> R): Result<R> {
    return try {
        Result.success(block())
    } catch (c: CancellationException) {
        // 严格遵守协作式取消契约，放行取消异常
        throw c
    } catch (e: Throwable) {
        Result.failure(e)
    }
}
```

**5.“缓存优先 + 后台静默刷新”或“限时竞速降级”（withTimeoutOrNull）**  

客户端痛点：App 首页配置接口，为了保证用户秒开体验，不能无限期等待弱网请求（比如最多只允许等 1.5 秒）；如果 1.5 秒内网络没回来，必须立刻使用本地缓存渲染，但同时让后台网络继续把最新数据拉回来更新缓存供下次使用。

高级解法：结合 `withTimeoutOrNull` 与独立的作用域策略：

```kotlin
suspend fun getDisplay(appScope: CoroutineScope): Module {
    // 1. 启动一个绑定全局作用域的后台网络更新任务（即使超时也不会被取消，确保能落盘更新缓存）
    val remoteDeferred = appScope.async(Dispatchers.IO) {
        api.fetchDisplayConfig().also { localCache.save(it) }
    }

    // 2. 当前调用方最多只挂起等待 1500ms：
    //    - 1.5s 内回来，直接用最新远程配置；
    //    - 超时返回 null，立刻降级读取本地磁盘缓存秒开页面！
    return withTimeoutOrNull(1500L) {
        remoteDeferred.await()
    } ?: localCache.read()
}
```

**6. 使用 `yield()` 让出线程占用**  

客户端痛点：客户端有时必须在主线程或有限线程池处理大型列表数据转换（如计算 5,000 条本地聊天记录的布局高度）。如果在 suspend 函数里写一个纯粹的 for 循环，即使它加了 suspend 关键字，也会连续霸占 CPU 几十毫秒导致丢帧（Jank）甚至无法响应用户取消。

高级解法：在循环内部每隔一定步长调用标准库挂起函数 yield()。yield() 一方面会主动检查协程是否已被取消，另一方面会暂时让出当前线程执行权，让排在队列前面的 UI 渲染或高优先级触摸事件先执行：

```kotlin
suspend fun processLargeMessagesOnMain(messages: List<Message>): List<UiItem> {
    val result = ArrayList<UiItem>(messages.size)
    messages.forEachIndexed { index, msg ->
        // 每处理 100 条数据，主动让出一次线程时间片并响应取消状态，防止主线程掉帧
        if (index % 100 == 0) {
            yield()
        }
        result.add(convertToUiItem(msg))
    }
    return result
}
```

---

*参考*  

[1] Open AIDoc. [组合挂起函数](https://openaidoc.org/kotlin/composing-suspending-functions#structured-concurrency-with-async). Accessed 2026-11-24.  
[2] Time Fine. [Kotlin-协程(三)理解挂起函数](https://juejin.cn/post/7200641773428555832). 掘金, 2023-02-16.  
[3] jzssuanfa. [深入解析 Kotlin suspend 挂起函数：从概念到后端实践](https://www.cnblogs.com/jzssuanfa/p/19801390). 博客园, 2026-03-31.
