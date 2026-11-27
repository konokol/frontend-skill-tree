# 取消与超时

## 协作式取消

### 基本的取消操作

**基本的操作**  

- `job.cancel()`：向协程发送取消信号（状态变为 `Cancelling`），但不会等待协程彻底清理结束。
- `job.cancelAndJoin()`：先发送取消信号，再挂起等待其执行完 `finally` 清理并彻底退出（`Cancelled`），防止新旧任务状态交错（竞态条件）。

**取消原理**  

Kotlin 协程的取消是协作式（Cooperative）的——框架不会像 `Thread.stop()` 那样粗暴杀掉线程，而是只把 `Job` 的标志位 `isActive` 置为 `false`，需要协程内部代码主动配合退出：

- 自动响应：所有 `kotlinx.coroutines` 提供的挂起函数（如 `delay()`、`withContext()`）内部都会检查 `isActive`，一旦被取消就立刻抛出 `CancellationException`。
- 手动响应（纯 CPU 密集型计算循环）：如果循环里没有调用任何挂起函数，必须手动检测取消状态：

```kotlin
val job = launch(Dispatchers.Default) {
    var count = 0
    // 方式 1：检查 isActive 属性（最常用，适合循环条件判断）
    while (isActive && count < 1_000_000) {
        // 方式 2：ensureActive() —— 若已取消则立刻抛出 CancellationException
        ensureActive()
        
        // 方式 3：yield() —— 既检查取消，又主动让出线程时间片防止掉帧
        if (count % 1000 == 0) yield()
        
        count++
    }
}
delay(100)
job.cancelAndJoin() // 协程立刻协作退出
```

### 资源清理

**同步资源清理：try-finally**  

```kotlin
launch(Dispatchers.IO) {
    val inputStream = File("data.txt").inputStream()
    try {
        // 模拟耗时读取，期间如果外部调用 job.cancel()，会在挂起点抛出 CancellationException
        delay(2000)
        inputStream.readBytes()
    } finally {
        // 【Cleanup 动作】：无论协程正常结束还是中途被取消，finally 块必定会执行！
        inputStream.close() 
    }
}
```

当协程在挂起点抛出 `CancellationException` 退出时，会正常走完 `finally` 块，适合关闭文件流、`Cursor` 等同步资源。

**异步挂起清理：try-finally + withContext(NonCancellable)**  

一旦协程进入 `Cancelling` 状态，它的 `isActive` 已经是 `false`。此时如果在 `finally` 块中直接调用任何挂起函数（如把日志写入 Room 数据库、调用登出接口），会立刻再次抛出 `CancellationException` 导致收尾代码执行失败！

解法：在 `finally` 中使用 `withContext(NonCancellable)` 临时切入一个永不取消的上下文，确保异步收尾动作完整执行完毕：

```kotlin
val job = launch {
    try {
        delay(5000) // 模拟耗时上传
    } finally {
        // ❌ 错误：直接写 delay(100) 或 db.insertLog() 会立刻被取消中断！
        
        // ✅ 正确：包裹在 NonCancellable 中，保证异步清理动作必定执行完
        withContext(NonCancellable) {
            delay(100)
            println("清理完成：已将中断状态安全写入本地数据库")
        }
    }
}
delay(500)
job.cancelAndJoin()
```

**底层回调句柄清理：invokeOnCancellation（与 Job.invokeOnCompletion）**  

适用于通过 suspendCancellableCoroutine 封装三方异步 API 时的清理动作（例如取消 OkHttp 请求、注销 GPS 定位监听、关闭确认弹窗）：

```kotlin
suspend fun fetchLocation(): Location = suspendCancellableCoroutine { cont ->
    val listener = LocationListener { location -> cont.resume(location) }
    locationManager.requestLocationUpdates(listener)

    // 【Cleanup 动作】：一旦协程取消，立刻注销系统定位监听器，防止内存泄漏与耗电
    cont.invokeOnCancellation {
        locationManager.removeUpdates(listener)
    }
}
```

### CancellationException 的特殊规则与避坑

**特殊传播规则，`CancellationException` 不终止父协程**  

在结构化并发中，子协程抛出普通异常（如 IOException）会向上传播并取消父协程和兄弟协程；但 `CancellationException` 被协程框架视为“正常终止信号”，当子协程抛出 `CancellationException` 时，它只会结束自己，不会向上取消父协程。

**致命大坑：try-catch 或 runCatching 吞掉取消异常**  

代码中捕获异常时经常直接捕获 `Exception`，会有一个致命的问题，导致 `CancellationException` 像普通异常一样被捕获了。

```kotlin
launch {
    try {
        delay(2000) // 外部调用 job.cancel() 时，此处会抛出 CancellationException
    } catch (e: Exception) {
        // ❌ 致命错误：宽泛捕获了 Exception，把 CancellationException 当成普通网络错误吞掉了！
        println("请求失败，准备重试...") 
    }
    // ❌ 后果：协程不知道自己已被取消，继续往下执行更新 UI，极易引发页面销毁后的空指针崩溃！
    updateUI() 
}
```

正确解法：捕获通用异常时，遇到 CancellationException 必须立刻重新 throw（或使用专门封装的 suspendRunCatching 放行取消异常）：

```kotlin
try {
    ...
} catch (e: Exception) {
    if (e is CancellationException) throw e // 放行取消信号！
    handleError(e)
}
```

**结构化级联取消与 cancelChildren()**  

- **级联取消**：父作用域取消（scope.cancel()）会自动递归取消名下所有子协程和孙协程。
- **保留父作用域**：如果只想清空当前正在跑的所有子任务，但希望父作用域保持活跃以便后续继续 launch 新任务（例如页面下拉刷新时取消旧的加载任务），必须调用 scope.coroutineContext.cancelChildren()（若直接调 scope.cancel()，该作用域会永久失效，后续无法再启动任何协程）。

## 超时控制

协程库提供了两个超时控制挂起函数，它们底层会在内部开启定时任务，超时瞬间自动向内部代码块发送取消信号：

**withTimeout(timeMillis)**  

行为：如果代码块在指定毫秒内未完成，立即取消内部挂起操作，并向外抛出 `TimeoutCancellationException`（CancellationException 的子类）。

*注意*：如果在顶层协程直接裸用 withTimeout 而不捕获异常，虽然不会导致 App 崩溃（因为它是 `CancellationException`），但超时后的代码会被直接跳过。

**withTimeoutOrNull(timeMillis)（生产首选）**  

行为：如果超时，不抛出任何异常，而是取消内部任务并优雅地返回 null，极其适合客户端弱网降级场景：

```kotlin
// 生产环境推荐写法：最多等待 2 秒，超时返回 null 并自动降级读本地缓存
val profile = withTimeoutOrNull(2000L) {
    remoteApi.fetchUserProfile() // 超时自动取消网络请求
} ?: localCache.getUserProfile()

```

---

*参考*  

[1] Kotlin. [Cancellation and timeouts](https://kotlinlang.org/docs/coroutines-cancellation.html). Accessed 2026-11-25.  
[2] Open AIDoc. [取消](https://openaidoc.org/kotlin/coroutines-cancellation). Accessed 2026-11-25.  
