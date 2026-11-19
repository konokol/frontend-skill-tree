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

## 协程作用域（CoroutineScope）

## 协程上下文（CoroutineContext）

## Job

## 协程调度器（Dispatcher）
