# 协程 (Coroutine)

## 基础

协程（Coroutine）是一个轻量级的并发编程解决方案，一般用来处理异步任务，它本质上是运行在用户态的轻量级任务执行单元。协程不是 Kotlin 特有的概念，如果抛开语言来讲，协程就是一个可以被暂停和恢复的函数。

协程处理异步通过挂起/恢复来实现，任务一直运行在用户态，和线程的阻塞不同，线程的切换会涉及用户态和内核态的切换，因此协程更轻量。而挂起/恢复的机制可以让我们以同步的代码结构来执行异步的任务，避免异步编码的层层回调，这也是协程的核心价值。

## 协程和线程的差异

协程和线程并不是互相替代的关系，而是承载与协作的关系，协程的运行必须依赖线程，不能独立于线程实现。线程是操作系统内核调度的最小单元，协程只是在线程的基础上由语言封装出来的并发框架。

![协程和线程](https://openaidoc.org/kotlin/coroutines-and-threads.svg)

从底层实现和工厂控制的角度来看，协程和线程的核心差异有四个：

- **调度方式（抢占式 vs 协作式）和切换成本** 线程的切换是操作系统内核控制的，由内核抢占式控制，线程切换时需要先进入内核态保存上下文，开销很大。协程运行在线程之上，完全运行在用户态，是协作式调度，只有在遇到 supend 挂起点时才主动让出执行权，它的切换完全是内存里对象的状态切换，开销非常低。
- **阻塞（Block）和挂起（Suspend）的机制** 协程通过挂起/恢复来实现异步操作，遇到耗时操作时，会释放线程的控制权，让线程去执行别的任务。而线程的等待是阻塞式的，遇到耗时操作会一直占着 CPU 的资源不释放。
- **内存模型和资源占用** 线程创建时，操作系统会为每个线程创建独立的调用栈，占用内存有数 MB。协程没有独立的调用栈，编译器把 suspend 函数编译成 CPS 状态机，把局部对象的状态保存在 Continuation 对象中，所以开一个协程占用的空间非常少，大约只有几十 KB。
- **生命周期和异常管控** 线程的生命周期完全由操作系统控制，开启线程后具体执行的时机是不可控的，处理不好往往容易造成内存泄漏。协程引入了结构性并发的概念，通过 viewModelScope 和 lifecycleScope 把任务和组件的生命周期绑定，页面结束时，父作用域会自动取消子作用域的协程，异常也能向上汇聚，从而从架构上解决异步问题。

从使用场景上看，如果是 CPU 密集型的任务，还是需要使用线程，能充分发挥多核的优势。如果是 IO 密集型任务，使用协程能够减少线程占据 CPU 空等的时间。

## 协程解决的问题

协程解决了传统线程并发编程中三个核心的问题：

**异步代码过于复杂（回调地狱）**：Android 中通过传统线程写异步代码，为了不阻塞主线程，通常都需要用异步回调的方式获取结果，调用链路过深时层层嵌套的回调导致代码非常难维护。协程通过挂起/恢复的方式来写异步代码，能让异步代码像写同步代码一样简单，异常处理也更方便。

**高并发下的资源与性能瓶颈（线程过重）**：Java 中的线程直接映射到操作系统的线程，线程创建和切换开销都比较大，同时线程是阻塞式调度，使用不合理很容易造成内存以及死锁等问题。协程只运行在用户态中，占用的资源很少，又是通过协作式调度，在并发度、内存占用方面协程都占优势。

**异步任务失控与泄漏（难管理）**：线程启动之后就不好控制，Android 开发中页面销毁时忘记取消异步任务，容易出现内存泄漏、状态异常等各种问题。协程引入结构化并发，能在页面销毁时取消子作用域内的协程，任意子协程出现异常，也能向上传递到父作用域，从架构层面避免了这类异常。

## 结构化并发（Structured Concurrency）

Kotlin 的协程是通过结构化并发来解决传统异步编程中出现的各种问题的。结构化并发是一种现代化的并发编程范式，它要求并发代码也要像结构化代码块一样，必须有明确的入口和出口。

结构化并发是协程的核心设计思想之一，它要求协程必须在作用域（CoroutineScope）中启动，作用域负责管理其中所有子协程的生命周期。Kotlin 协程的结构化并发中中有四大核心原则：

- 作用域边界约束，协程不能凭空创建，必须在作用域中启动。
- 父等子原则，父协程执行完自己的代码之后会挂起，必须等待所有的子协程结束才真正结束。
- 取消向下传递，父协程取消时子协程也会自动取消，防止子协程在父协程生命周期结束后还在执行。
- 异常向上传递，默认机制下，子协程有异常时会向上传播到父协程，父协程收到异常后会先取消它自己的子协程（即异常协程的兄弟协程），随即将异常继续向上传递。

## 协程的使用

启动一个简单的协程：

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val deferred = async {
        delay(1000L)
        "World!"
    }
    print("Hello ")
    println(deferred.await()) // 等待结果
}
```

例子中启动一个简单协程，例子会输出 `Hello, World`。

### 启动协程--三个核心的构建器

协程构建器（Coroutine Builders）用来启动协程，kotlinx.coroutines 包中有三个核心构建器 `launch`、`async`、`runBlocking`。此外在 Channel 通信模型中还有一个 `produce` 构建器。

**1. CoroutineScope.launch**  

启动一个独立的子协程，不阻塞当前作用域的其他部分。CoroutineScope.launch 返回一个 Job 对象。可以通过 `job.cancel()` 取消协程，`job.join()`等待结束。

```kotlin
val job = viewModelScope.launch(Dispatchers.IO) {
    // 执行耗时操作，无返回值
    saveDataToLocal()
}
// 需要时可手动取消
// job.cancel()
```

**2. CoroutineScope.async**  

启动一个独立的子协程，和 launch 一样也是非阻塞。返回一个 `Deferred<T>` 对象，它是 Job 的子类。调用 `deferred.await()` 可以挂起并等待结果。

```kotlin
viewModelScope.launch {
    // 两个 async 立即并发启动
    val deferredA = async(Dispatchers.IO) { getUserInfo() }
    val deferredB = async(Dispatchers.IO) { getBannerList() }

    // 挂起等待结果返回
    val info = deferredA.await()
    val banners = deferredB.await()
}
```

**3. runBlocking**  

runBlocking 启动一个新协程并阻塞当前的物理线程，直到内部的子协程都执行完。runBlocking 返回代码块的最后一行。

Android 中在主线程直接调用或在 viewModelScope 中调用 runBlocking 都会阻塞主线程，有可能导致 ANR。所以 runBlocking一般只用在测试代码中。

```kotlin
@Test
fun testFetchUser() = runBlocking {
    // 在 JUnit 测试环境中直接调用 suspend 函数
    val user = repository.fetchUser()
    assertEquals("Alice", user.name)
}
```

### 在挂起函数内部启动协程

如果已经在挂起函数内部，并且不希望使用外部的作用域来启动协程，还可以用 `coroutineScope { ... }` 和 `supervisorScope { ... }`。他们会挂起当前的协程，创建一个新的作用域，直到内部所有的子任务全部完成后才返回。

```kotlin
suspend fun loadAllData() = coroutineScope {
    // 在挂起函数内部安全地开启并发
    val task1 = async { fetchPart1() }
    val task2 = async { fetchPart2() }
    // 必须等 task1 和 task2 都结束，loadAllData 才会返回
    merge(task1.await(), task2.await())
}
```

- **coroutineScope**：一损俱损。任一子任务失败，会自动取消其他兄弟任务并向外抛出异常。
- **supervisorScope**：互不干扰。任一子任务失败，不会影响其他兄弟任务的运行（常用于页面多个独立模块并发加载）。

### withContext

`withContext` 不是协程的调度器，它是一个挂起函数，调用它也不会启动一个新的协程。它的作用是在当前协程的作用域内临时切换上下文(常见的是调用线程调度器)，代码块执行完毕后，会自动切换到原来的上下文。

当执行到 `withContext` 时，当前协程会挂起并释放原线程的控制权，等 `withContext` 中的代码块执行完之后，最后一行是它的返回值，会自动恢复原线程继续往下走。

----

*参考*  

[1] Android Developers. [Android 上的协程](https://developer.android.google.cn/kotlin/coroutines?hl=zh-cn). Accessed 2026-11-17.  
[2] Kotlin 中文文档. [协程指南](https://book.kotlincn.net/text/coroutines-guide.html). Accessed 2026-11-17.  
[3] Open AIDoc. [协程指南](https://openaidoc.org/kotlin/coroutines-guide). Accessed 2026-11-17.  
[4] 灰色飘零. [深入浅出Kotlin协程：核心原理与线程的本质区别](https://www.cnblogs.com/renhui/articles/13433301.html). 博客园, 2020.  
[5] Android Developers. [利用 Kotlin 协程提升应用性能](https://developer.android.google.cn/kotlin/coroutines/coroutines-adv?hl=zh-cn). Accessed 2026-11-17
