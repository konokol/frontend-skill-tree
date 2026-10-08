# Kotlin 面试 50 题

---

## 一、基础与空安全

### 题目 1：`safeCast<T>` 用 `reified` 实现

**题目描述**  
实现 `Any?.safeCast<T>()`，安全转换为 `T?`。使用 `reified`，调用时无需传 `Class`。

<details>
<summary>点击查看代码</summary>

```kotlin
inline fun <reified T> Any?.safeCast(): T? = this as? T

val x: Any = "hello"
val s: String? = x.safeCast<String>()   // "hello"
val i: Int? = x.safeCast<Int>()         // null
```
</details>

**关键点**：`inline` + `reified` 将类型具体化，避免泛型擦除；`as?` 安全转换。

**追问与答案**  
1. **`reified` 为什么必须配合 `inline`？**  
   答：只有内联函数才能在调用处展开函数体，并将类型参数替换为具体类型；非内联函数编译后泛型被擦除，无法在运行时判断类型。  
2. **`reified` 能用在类成员函数吗？**  
   答：不能。类成员若内联会暴露私有成员，编译器限制 `reified` 只能用于顶层或扩展内联函数。  
3. **`as?` 和 `as` 区别？**  
   答：`as?` 失败返回 `null`，`as` 失败抛 `ClassCastException`。

---

### 题目 2：`String?.orEmpty()` 扩展

**题目描述**  
为可空字符串实现 `orEmpty()`，`null` 返回 `""`。

<details>
<summary>点击查看代码</summary>

```kotlin
fun String?.orEmpty(): String = this ?: ""
```
</details>

**关键点**：可空接收者扩展，`null` 安全调用。

**追问与答案**  
1. **可空接收者扩展和普通扩展区别？**  
   答：可空接收者扩展的接收者类型是 `String?`，内部 `this` 可能为 `null`，调用时无需 `?.`；普通扩展接收者非空。  
2. **为什么不用 `!!`？**  
   答：`!!` 在 `null` 时抛 NPE，`orEmpty()` 是安全兜底，返回空串。

---

### 题目 3：`sealed class` 建模网络状态

**题目描述**  
用密封接口建模 `Loading`、`Success<T>`、`Error`，`when` 穷举。

<details>
<summary>点击查看代码</summary>

```kotlin
sealed interface NetState<out T> {
    data object Loading : NetState<Nothing>
    data class Success<T>(val data: T) : NetState<T>
    data class Error(val code: Int, val msg: String) : NetState<Nothing>
}

fun <T> render(state: NetState<T>) = when (state) {
    is NetState.Loading -> showLoading()
    is NetState.Success -> showData(state.data)
    is NetState.Error -> showError(state.code, state.msg)
}
```
</details>

**关键点**：密封接口限制子类，`when` 可穷举；`Nothing` 占位，`out T` 协变。

**追问与答案**  
1. **密封类和枚举区别？**  
   答：枚举每个值都是单例且不能携带不同数据；密封类子类可以有不同构造参数和状态。  
2. **密封接口和密封类选择？**  
   答：需要多继承用密封接口；需要构造器状态用密封类。  
3. **`data object` 和 `object` 区别？**  
   答：`data object` 自动生成 `toString/equals/hashCode`，`object` 不生成。

---

### 题目 4：`Result<T>` 风格类型

**题目描述**  
实现 `MyResult<T>`，支持 `map`、`flatMap`、`getOrElse`、`onSuccess`。

<details>
<summary>点击查看代码</summary>

```kotlin
sealed class MyResult<out T> {
    data class Success<T>(val value: T) : MyResult<T>()
    data class Failure(val error: Throwable) : MyResult<Nothing>()

    fun <R> map(transform: (T) -> R): MyResult<R> = when (this) {
        is Success -> Success(transform(value))
        is Failure -> this
    }

    fun <R> flatMap(transform: (T) -> MyResult<R>): MyResult<R> = when (this) {
        is Success -> transform(value)
        is Failure -> this
    }

    fun getOrElse(default: T): T = when (this) {
        is Success -> value
        is Failure -> default
    }

    fun onSuccess(action: (T) -> Unit): MyResult<T> {
        if (this is Success) action(value)
        return this
    }
}
```
</details>

**关键点**：函数式 Either 模式；`Failure` 用 `Nothing` 占位。

**追问与答案**  
1. **为什么 `Failure` 用 `Nothing`？**  
   答：`Nothing` 是所有类型的子类型，`MyResult<Nothing>` 可以赋给任意 `MyResult<T>`，表示失败不携带数据。  
2. **`map` 和 `flatMap` 区别？**  
   答：`map` 转换成功值并返回普通值；`flatMap` 转换后返回新的 `MyResult`，避免嵌套。  
3. **和 `try/catch` 对比？**  
   答：`Result` 把错误变成值，适合链式处理；`try/catch` 适合命令式流程。

---

### 题目 5：`value class UserId`

**题目描述**  
用 `value class` 包装 `Long`，保证类型安全。

<details>
<summary>点击查看代码</summary>

```kotlin
@JvmInline
value class UserId(val id: Long)

fun fetchUser(id: UserId) { /* ... */ }
fetchUser(UserId(1001L))
// fetchUser(1001L) // 编译错误
```
</details>

**关键点**：内联类，多数场景无装箱；只能一个主构造属性。

**追问与答案**  
1. **`value class` 和 `data class` 区别？**  
   答：`value class` 编译后内联为底层类型，无对象头；`data class` 是普通类，有 `copy/equals/hashCode`。  
2. **什么时候会装箱？**  
   答：作为可空类型、泛型参数、接口引用时，会装箱为包装对象。  
3. **`value class` 能做标识符吗？**  
   答：能，编译后是底层类型，但方法名可能被修饰（如 `fetchUser-xxxxx`）。

---

## 二、类、委托、密封

### 题目 6：自定义 `by lazy` 线程安全委托

**题目描述**  
手写线程安全懒加载委托，模拟 `by lazy(SYNCHRONIZED)`。

<details>
<summary>点击查看代码</summary>

```kotlin
class MyLazy<T>(private val initializer: () -> T) {
    @Volatile private var value: Any? = UNINITIALIZED
    private val lock = Any()

    val lazyValue: T
        get() {
            if (value === UNINITIALIZED) {
                synchronized(lock) {
                    if (value === UNINITIALIZED) {
                        value = initializer()
                    }
                }
            }
            @Suppress("UNCHECKED_CAST")
            return value as T
        }

    companion object {
        private val UNINITIALIZED = Any()
    }
}
```
</details>

**关键点**：双重检查锁 + `@Volatile`；哨兵对象区分未初始化。

**追问与答案**  
1. **`PUBLICATION` 模式如何实现？**  
   答：使用 `AtomicReferenceFieldUpdater` 做 CAS，允许多个线程都执行初始化，但只保留一个结果，不阻塞线程。  
2. **`NONE` 适合什么场景？**  
   答：单线程或确定不会并发访问的场景，性能最高，无锁。  
3. **`lazy` 能重置吗？**  
   答：标准 `lazy` 不能重置；需要重置可用自定义委托。

---

### 题目 7：`observable` 属性委托

**题目描述**  
实现属性委托，变化时回调旧值和新值。

<details>
<summary>点击查看代码</summary>

```kotlin
class ObservableProperty<T>(
    initial: T,
    private val onChange: (old: T, new: T) -> Unit
) {
    private var value: T = initial

    operator fun getValue(thisRef: Any?, property: KProperty<*>): T = value

    operator fun setValue(thisRef: Any?, property: KProperty<*>, newValue: T) {
        val old = value
        value = newValue
        onChange(old, newValue)
    }
}
```
</details>

**关键点**：`getValue`/`setValue` 是委托核心；`vetoable` 可阻止赋值。

**追问与答案**  
1. **`observable` 和 `vetoable` 区别？**  
   答：`vetoable` 的 `setValue` 返回 `Boolean`，返回 `false` 可阻止赋值；`observable` 只是通知。  
2. **`KProperty` 能做什么？**  
   答：获取属性名、类型、注解、是否可空等元信息。  
3. **委托属性编译后长什么样？**  
   答：生成一个委托对象字段，属性访问转发到 `getValue/setValue`。

---

### 题目 8：`ResetableLateinit` 委托

**题目描述**  
实现可重置的 `lateinit` 委托。

<details>
<summary>点击查看代码</summary>

```kotlin
class ResetableLateinit<T> {
    private var value: T? = null

    operator fun getValue(thisRef: Any?, property: KProperty<*>): T =
        value ?: throw UninitializedPropertyAccessException(property.name)

    operator fun setValue(thisRef: Any?, property: KProperty<*>, newValue: T) {
        value = newValue
    }

    fun reset() { value = null }
}
```
</details>

**关键点**：用 `null` 表示未初始化；可重置。

**追问与答案**  
1. **`lateinit` 为什么不能用于基本类型？**  
   答：基本类型无法用 `null` 表示未初始化状态，`lateinit` 依赖 `null` 检查。  
2. **`lateinit` 能用于可空类型吗？**  
   答：不能，`lateinit var x: String?` 编译错误。  
3. **如何判断 `lateinit` 是否初始化？**  
   答：用 `::x.isInitialized`。

---

### 题目 9：密封接口 `UiState`

**题目描述**  
定义 `Idle`、`Loading`、`Content<T>`、`Error` 并穷举 `when`。

<details>
<summary>点击查看代码</summary>

```kotlin
sealed interface UiState<out T> {
    data object Idle : UiState<Nothing>
    data object Loading : UiState<Nothing>
    data class Content<T>(val data: T) : UiState<T>
    data class Error(val throwable: Throwable) : UiState<Nothing>
}

fun <T> UiState<T>.render(): String = when (this) {
    UiState.Idle -> "idle"
    UiState.Loading -> "loading"
    is UiState.Content -> "content: $data"
    is UiState.Error -> "error: ${throwable.message}"
}
```
</details>

**关键点**：密封接口支持多实现；`data object` 单例。

**追问与答案**  
1. **密封接口和密封类区别？**  
   答：接口支持多继承，类支持构造器状态；密封接口更灵活。  
2. **`data object` 和 `object` 区别？**  
   答：`data object` 自动生成 `toString/equals/hashCode`。  
3. **密封类能跨模块继承吗？**  
   答：不能，密封类子类必须同模块（Kotlin 1.5+ 同模块）。

---

### 题目 10：类委托 `LoggingList`

**题目描述**  
用类委托增强 `MutableList`，只覆写 `add`/`remove`。

<details>
<summary>点击查看代码</summary>

```kotlin
class LoggingList<T>(
    private val inner: MutableList<T> = mutableListOf()
) : MutableList<T> by inner {

    override fun add(element: T): Boolean {
        println("add: $element")
        return inner.add(element)
    }

    override fun remove(element: T): Boolean {
        println("remove: $element")
        return inner.remove(element)
    }
}
```
</details>

**关键点**：`by inner` 自动转发所有方法；只覆写需要增强的。

**追问与答案**  
1. **类委托底层？**  
   答：编译器生成所有接口方法的转发方法，调用 `inner.xxx()`。  
2. **类委托和继承区别？**  
   答：委托组合优于继承，避免脆弱基类，只暴露接口。  
3. **能委托多个接口吗？**  
   答：能，`class A : B by b, C by c`。

---

## 三、扩展、内联、泛型、DSL

### 题目 11：`startActivity<T>` 用 `reified`

**题目描述**  
实现 `Context.startActivity<T>()`，用 `reified` 避免传 Class。

<details>
<summary>点击查看代码</summary>

```kotlin
inline fun <reified T : Activity> Context.startActivity() {
    startActivity(Intent(this, T::class.java))
}

inline fun <reified T : Activity> Context.startActivity(
    block: Intent.() -> Unit
) {
    val intent = Intent(this, T::class.java).apply(block)
    startActivity(intent)
}
```
</details>

**关键点**：`reified` 让 `T::class.java` 可用；`inline` 避免 lambda 对象。

**追问与答案**  
1. **`inline` 函数中的 lambda 能非局部返回吗？**  
   答：能，内联后 `return` 直接作用于外层函数，称为非局部返回。  
2. **`noinline` 和 `crossinline` 区别？**  
   答：`noinline` 禁止某 lambda 参数内联；`crossinline` 禁止非局部返回，但保持内联。  
3. **`reified` 限制？**  
   答：不能用于类成员函数，不能用于非内联函数。

---

### 题目 12：`myFilter` 对比 `Iterable` 和 `Sequence`

**题目描述**  
分别实现 `Iterable.myFilter` 和 `Sequence.myFilter`，对比惰性。

<details>
<summary>点击查看代码</summary>

```kotlin
fun <T> Iterable<T>.myFilter(predicate: (T) -> Boolean): List<T> {
    val result = mutableListOf<T>()
    for (item in this) if (predicate(item)) result.add(item)
    return result
}

fun <T> Sequence<T>.myFilter(predicate: (T) -> Boolean): Sequence<T> = sequence {
    for (item in this@myFilter) if (predicate(item)) yield(item)
}
```
</details>

**关键点**：`Iterable` 立即求值；`Sequence` 惰性，`yield` 逐元素。

**追问与答案**  
1. **Sequence 如何实现惰性？**  
   答：每个操作符返回新 Sequence，`iterator` 串联，逐元素传递，直到终端操作才执行。  
2. **Sequence 有开销吗？**  
   答：有，每次元素传递有函数调用开销，小数据量可能比 Iterable 慢。  
3. **什么时候用 Sequence？**  
   答：大数据量、链式操作多、只需部分结果时。

---

### 题目 13：`Producer<out T>` 和 `Consumer<in T>`

**题目描述**  
演示协变与逆变。

<details>
<summary>点击查看代码</summary>

```kotlin
interface Producer<out T> {
    fun produce(): T
}

interface Consumer<in T> {
    fun consume(item: T)
}

class StringProducer : Producer<String> {
    override fun produce() = "hello"
}

class AnyConsumer : Consumer<Any> {
    override fun consume(item: Any) = println(item)
}

fun main() {
    val p: Producer<Any> = StringProducer()  // 协变
    val c: Consumer<String> = AnyConsumer()  // 逆变
}
```
</details>

**关键点**：产出用 `out`，消费用 `in`；`List<out T>` 协变。

**追问与答案**  
1. **为什么 `List` 协变？**  
   答：`List` 只读，元素只出不进，所以 `List<String>` 可赋给 `List<Any>`。  
2. **`MutableList` 型变？**  
   答：不变，既可读又可写，不能协变也不能逆变。  
3. **使用处型变？**  
   答：在类型使用处声明型变，如 `Array<out T>`。

---

### 题目 14：类型安全 DSL：`intent { }`

**题目描述**  
用带接收者 lambda 实现 `intent {}`。

<details>
<summary>点击查看代码</summary>

```kotlin
class IntentBuilder {
    var action: String = ""
    var data: String = ""
    var extras: MutableMap<String, Any> = mutableMapOf()

    fun extra(key: String, value: Any) { extras[key] = value }
}

fun intent(block: IntentBuilder.() -> Unit): IntentBuilder =
    IntentBuilder().apply(block)
```
</details>

**关键点**：带接收者 lambda + `apply`；DSL 核心。

**追问与答案**  
1. **DSL 和 Builder 区别？**  
   答：DSL 用 lambda 和接收者，更灵活，可嵌套、控制作用域；Builder 是链式调用。  
2. **`apply` 和 `also` 区别？**  
   答：`apply` 接收者是 `this`，返回自身；`also` 参数是 `it`，返回自身。  
3. **如何防止 DSL 作用域污染？**  
   答：用 `@DslMarker`。

---

### 题目 15：`@DslMarker` 防止作用域污染

**题目描述**  
用 `@DslMarker` 实现嵌套 DSL，防止外层接收者被内层误用。

<details>
<summary>点击查看代码</summary>

```kotlin
@DslMarker
annotation class HtmlDsl

@HtmlDsl
class Html {
    private val children = mutableListOf<String>()
    fun body(block: Body.() -> Unit) {
        val b = Body().apply(block)
        children.add(b.render())
    }
    fun render() = "<html>${children.joinToString("")}</html>"
}

@HtmlDsl
class Body {
    private val children = mutableListOf<String>()
    fun p(text: String) { children.add("<p>$text</p>") }
    fun render() = "<body>${children.joinToString("")}</body>"
}

fun html(block: Html.() -> Unit): Html = Html().apply(block)
```
</details>

**关键点**：`@DslMarker` 隐藏外层接收者，防止错误嵌套。

**追问与答案**  
1. **`@DslMarker` 底层？**  
   答：编译器作用域解析规则，最近接收者优先，外层同标记接收者被隐藏。  
2. **不加会怎样？**  
   答：内层可访问外层成员，容易写出错误嵌套调用。

---

### 题目 16：`Gson.fromJson<T>` 用 `reified`

**题目描述**  
实现 `Gson.fromJson<T>` 支持简单类型和泛型。

<details>
<summary>点击查看代码</summary>

```kotlin
inline fun <reified T> Gson.fromJson(json: String): T? =
    fromJson(json, T::class.java)

inline fun <reified T> Gson.fromJsonTyped(json: String): T? =
    fromJson(json, object : TypeToken<T>() {}.type)
```
</details>

**关键点**：简单类型用 `T::class.java`；泛型用 `TypeToken` 匿名子类。

**追问与答案**  
1. **`TypeToken` 为何能保留泛型？**  
   答：匿名子类编译后 `Signature` 属性保留泛型信息，Gson 通过反射读取。  
2. **`kotlinx.serialization` 对比？**  
   答：编译期生成序列化器，无反射，性能更好，但需要注解和插件。

---

### 题目 17：路由 DSL：`path("/user/{id}")`

**题目描述**  
实现简单路由 DSL。

<details>
<summary>点击查看代码</summary>

```kotlin
class RouteBuilder {
    private val routes = mutableListOf<Route>()

    fun path(pattern: String, block: Route.() -> Unit = {}) {
        val route = Route(pattern).apply(block)
        routes.add(route)
    }

    fun build() = routes
}

class Route(val pattern: String) {
    var method: String = "GET"
    var handler: (Map<String, String>) -> Unit = {}
    val params = mutableMapOf<String, String>()

    fun get(handler: (Map<String, String>) -> Unit) {
        method = "GET"
        this.handler = handler
    }
}

fun router(block: RouteBuilder.() -> Unit): List<Route> =
    RouteBuilder().apply(block).build()
```
</details>

**关键点**：嵌套 DSL；实际可用 KSP 生成路由表。

**追问与答案**  
1. **DSL 如何做类型安全路由？**  
   答：用 `reified` 和泛型参数，在编译期检查路由参数类型。  
2. **注解处理器如何生成路由？**  
   答：KSP 扫描注解，生成注册代码，避免运行时反射。

---

## 四、协程基础与进阶

### 题目 18：`launch` vs `async` 异常传播

**题目描述**  
对比二者异常传播。

<details>
<summary>点击查看代码</summary>

```kotlin
fun main() = runBlocking {
    val job = launch {
        throw RuntimeException("launch error")
    }
    job.join()

    val deferred = async {
        throw RuntimeException("async error")
    }
    try {
        deferred.await()
    } catch (e: Exception) {
        println("caught: ${e.message}")
    }
}
```
</details>

**关键点**：`launch` 立即抛，取消父；`async` 延迟到 `await`。

**追问与答案**  
1. **`async` 不 `await` 会怎样？**  
   答：异常可能丢失，取决于作用域；若在根作用域，会走 `CoroutineExceptionHandler`。  
2. **`CoroutineExceptionHandler` 作用？**  
   答：处理未捕获异常，仅对根协程生效。

---

### 题目 19：`SupervisorJob` 隔离异常

**题目描述**  
用 `SupervisorJob` 让子协程异常不影响兄弟。

<details>
<summary>点击查看代码</summary>

```kotlin
fun main() = runBlocking {
    val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)

    val child1 = scope.launch {
        delay(100)
        throw RuntimeException("child1 failed")
    }
    val child2 = scope.launch {
        delay(200)
        println("child2 completed")
    }

    child1.join()
    child2.join()
    println("done")
}
```
</details>

**关键点**：`SupervisorJob` 子异常不取消兄弟；普通 `Job` 会。

**追问与答案**  
1. **`SupervisorJob` 子协程再启动子协程？**  
   答：异常会取消该子协程的子树，但不影响兄弟协程。  
2. **`supervisorScope` 与 `SupervisorJob` 区别？**  
   答：`supervisorScope` 是作用域函数，内部使用 `SupervisorJob`；`SupervisorJob` 是直接创建 Job。

---

### 题目 20：`withTimeoutOrNull` 简化版

**题目描述**  
手写简化版 `withTimeoutOrNull`。

<details>
<summary>点击查看代码</summary>

```kotlin
suspend fun <T> myWithTimeoutOrNull(
    timeoutMs: Long,
    block: suspend () -> T
): T? = coroutineScope {
    val job = launch {
        delay(timeoutMs)
        throw TimeoutCancellationException("timeout")
    }
    try {
        val result = block()
        job.cancel()
        result
    } catch (e: TimeoutCancellationException) {
        null
    }
}
```
</details>

**关键点**：超时抛异常，捕获返回 `null`。

**追问与答案**  
1. **`withTimeout` 与 `withTimeoutOrNull` 区别？**  
   答：`withTimeout` 超时抛 `TimeoutCancellationException`；`withTimeoutOrNull` 返回 `null`。  
2. **超时后任务会取消吗？**  
   答：会，协程被取消。

---

### 题目 21：`Mutex` 并发安全计数器

**题目描述**  
用 `Mutex` 实现并发安全计数器。

<details>
<summary>点击查看代码</summary>

```kotlin
class SafeCounter {
    private val mutex = Mutex()
    private var count = 0

    suspend fun increment() {
        mutex.withLock {
            count++
        }
    }

    suspend fun get(): Int = mutex.withLock { count }
}
```
</details>

**关键点**：协程挂起锁，不阻塞线程；`withLock` 自动释放。

**追问与答案**  
1. **`Mutex` 与 `synchronized` 区别？**  
   答：`Mutex` 是协程挂起锁，不阻塞线程；`synchronized` 阻塞线程。  
2. **`Mutex` 和 `Semaphore` 区别？**  
   答：`Mutex` 是二值锁，`Semaphore` 可设多个许可。

---

### 题目 22：`Channel` 生产者消费者

**题目描述**  
用 `Channel` 实现生产者消费者。

<details>
<summary>点击查看代码</summary>

```kotlin
fun main() = runBlocking {
    val channel = Channel<Int>(capacity = 3)

    val producer = launch {
        for (i in 1..10) {
            channel.send(i)
            println("produced: $i")
        }
        channel.close()
    }

    val consumer = launch {
        for (value in channel) {
            println("consumed: $value")
            delay(100)
        }
    }

    producer.join()
    consumer.join()
}
```
</details>

**关键点**：`Channel` 热流，多消费者竞争；容量策略。

**追问与答案**  
1. **`Channel` 与 `Flow` 区别？**  
   答：`Channel` 是热流，多消费者竞争；`Flow` 是冷流，一对一。  
2. **`Channel` 和 `SharedFlow` 区别？**  
   答：`Channel` 单消费，`SharedFlow` 广播多订阅者。

---

### 题目 23：`coroutineScope` vs `supervisorScope`

**题目描述**  
对比异常行为。

<details>
<summary>点击查看代码</summary>

```kotlin
suspend fun testCoroutineScope() = coroutineScope {
    launch { throw RuntimeException("fail") }
    launch { delay(1000); println("sibling") }  // 被取消
}

suspend fun testSupervisorScope() = supervisorScope {
    launch { throw RuntimeException("fail") }
    launch { delay(1000); println("sibling") }  // 正常执行
}
```
</details>

**关键点**：`coroutineScope` 子异常取消所有；`supervisorScope` 不影响兄弟。

**追问与答案**  
1. **`supervisorScope` 异常如何传播？**  
   答：子异常不影响兄弟，但会取消自己，异常向上传播。  
2. **`coroutineScope` 和 `runBlocking` 区别？**  
   答：`coroutineScope` 是挂起函数，不阻塞线程；`runBlocking` 阻塞线程。

---

### 题目 24：协程取消：`ensureActive`

**题目描述**  
实现可取消循环。

<details>
<summary>点击查看代码</summary>

```kotlin
suspend fun cancellableLoop() = coroutineScope {
    val job = launch {
        try {
            for (i in 1..1000) {
                ensureActive()
                println("work $i")
                delay(10)
            }
        } catch (e: CancellationException) {
            println("cancelled")
            throw e
        } finally {
            println("cleanup")
        }
    }

    delay(50)
    job.cancel()
    job.join()
}
```
</details>

**关键点**：取消是协作式；`ensureActive` 检查取消；`finally` 清理。

**追问与答案**  
1. **`finally` 中能挂起吗？**  
   答：默认不能，会抛 `CancellationException`；需 `withContext(NonCancellable)`。  
2. **`isActive` 和 `ensureActive` 区别？**  
   答：`isActive` 返回布尔；`ensureActive` 抛异常。

---

### 题目 25：`CoroutineExceptionHandler` 使用与原理

**题目描述**  
使用 `CoroutineExceptionHandler` 捕获未处理异常。

<details>
<summary>点击查看代码</summary>

```kotlin
fun main() = runBlocking {
    val handler = CoroutineExceptionHandler { _, exception ->
        println("Caught: ${exception.message}")
    }

    val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default + handler)

    scope.launch {
        throw RuntimeException("child failed")
    }

    delay(500)
}
```
</details>

**关键点**：只对根协程生效；`async` 异常走 `await`。

**追问与答案**  
1. **为什么只对根协程生效？**  
   答：子协程异常会先取消父协程，最终传播到根，由根协程的 handler 处理。  
2. **`SupervisorJob` 和 handler 一起用？**  
   答：`SupervisorJob` 阻止异常取消兄弟，handler 负责最终处理根异常。  
3. **handler 能恢复协程吗？**  
   答：不能，协程已结束，只能记录日志或上报。

---

### 题目 26：`NonCancellable` 与 finally 中挂起

**题目描述**  
在 `finally` 中执行挂起操作，使用 `NonCancellable`。

<details>
<summary>点击查看代码</summary>

```kotlin
suspend fun doWork() = coroutineScope {
    val job = launch {
        try {
            repeat(1000) { i ->
                delay(10)
                println("work $i")
            }
        } finally {
            withContext(NonCancellable) {
                delay(100)
                println("cleanup in finally")
            }
        }
    }

    delay(50)
    job.cancelAndJoin()
}
```
</details>

**关键点**：`NonCancellable` 允许 `finally` 中挂起。

**追问与答案**  
1. **`finally` 中能直接 `delay` 吗？**  
   答：不能，会立即抛 `CancellationException`。  
2. **`NonCancellable` 和 `SupervisorJob` 区别？**  
   答：`NonCancellable` 用于不可取消的清理，`SupervisorJob` 用于隔离异常。  
3. **`withContext(NonCancellable)` 会切换线程吗？**  
   答：不会，只改变 Job，线程由其他上下文决定。

---

### 题目 27：`async` 并发组合与 `awaitAll`

**题目描述**  
用 `async` 并发执行多个请求。

<details>
<summary>点击查看代码</summary>

```kotlin
suspend fun fetchAll(): List<String> = coroutineScope {
    val deferreds = listOf(
        async { fetch1() },
        async { fetch2() },
        async { fetch3() }
    )
    deferreds.awaitAll()
}

suspend fun fetch1(): String { delay(100); return "1" }
suspend fun fetch2(): String { delay(200); return "2" }
suspend fun fetch3(): String { delay(300); return "3" }
```
</details>

**关键点**：`awaitAll` 等待所有；总耗时取决于最慢。

**追问与答案**  
1. **`awaitAll` 和 `joinAll` 区别？**  
   答：`awaitAll` 返回结果列表；`joinAll` 只等待完成，不返回结果。  
2. **`async` 异常何时抛出？**  
   答：`await` 时抛出；若在 `coroutineScope` 中，也会取消父作用域。  
3. **如何限制并发数？**  
   答：用 `Semaphore` 或 `Flow` 的 `flatMapMerge` + `concurrency`。

---

## 五、Flow 基础与进阶

### 题目 28：冷流 `flow { emit }`

**题目描述**  
实现冷流，每次 `collect` 重新执行。

<details>
<summary>点击查看代码</summary>

```kotlin
fun numbers(): Flow<Int> = flow {
    for (i in 1..5) {
        delay(100)
        emit(i)
    }
}

fun main() = runBlocking {
    numbers()
        .catch { e -> println("caught: $e") }
        .onCompletion { println("done") }
        .collect { println(it) }
}
```
</details>

**关键点**：冷流每次 collect 重新执行；`catch` 捕获上游异常。

**追问与答案**  
1. **`flow` 如何保证上下文保持？**  
   答：`emit` 检查 `coroutineContext` 一致，跨上下文需 `flowOn`。  
2. **`catch` 能捕获下游异常吗？**  
   答：不能，只捕获上游异常。

---

### 题目 29：`flatMapLatest` 搜索防抖

**题目描述**  
实现搜索防抖。

<details>
<summary>点击查看代码</summary>

```kotlin
class SearchViewModel {
    private val queryFlow = MutableStateFlow("")

    val results: Flow<List<String>> = queryFlow
        .debounce(300)
        .filter { it.isNotBlank() }
        .distinctUntilChanged()
        .flatMapLatest { query ->
            searchApi(query)
        }

    private fun searchApi(query: String): Flow<List<String>> = flow {
        delay(500)
        emit(listOf("$query-1", "$query-2"))
    }
}
```
</details>

**关键点**：`debounce` 防抖；`flatMapLatest` 取消旧请求。

**追问与答案**  
1. **`flatMapLatest` 与 `flatMapMerge` 区别？**  
   答：`flatMapLatest` 新流到来取消旧流；`flatMapMerge` 并发合并所有流。  
2. **`debounce` 与 `sample` 区别？**  
   答：`debounce` 取稳定后最后一个；`sample` 周期性采样。

---

### 题目 30：`callbackFlow` 包装回调

**题目描述**  
把回调 API 转成 Flow。

<details>
<summary>点击查看代码</summary>

```kotlin
fun locationFlow(): Flow<Location> = callbackFlow {
    val listener = object : LocationListener {
        override fun onLocation(location: Location) {
            trySend(location)
        }
        override fun onError(e: Throwable) {
            close(e)
        }
    }
    locationManager.requestLocationUpdates(listener)

    awaitClose {
        locationManager.removeUpdates(listener)
    }
}
```
</details>

**关键点**：`callbackFlow` 强制 `awaitClose`；`trySend` 非挂起。

**追问与答案**  
1. **`callbackFlow` 与 `channelFlow` 区别？**  
   答：`callbackFlow` 是 `channelFlow` 特化，强制 `awaitClose`。  
2. **`awaitClose` 必须调用吗？**  
   答：必须，否则流无法完成，资源无法释放。

---

### 题目 31：`StateFlow` 管理 UI 状态

**题目描述**  
用 `StateFlow` 管理 UI 状态。

<details>
<summary>点击查看代码</summary>

```kotlin
data class UiState(
    val loading: Boolean = false,
    val data: List<String> = emptyList(),
    val error: String? = null
)

class MyViewModel : ViewModel() {
    private val _state = MutableStateFlow(UiState())
    val state: StateFlow<UiState> = _state.asStateFlow()

    fun load() {
        viewModelScope.launch {
            _state.update { it.copy(loading = true) }
            try {
                val data = repository.fetch()
                _state.update { it.copy(loading = false, data = data) }
            } catch (e: Exception) {
                _state.update { it.copy(loading = false, error = e.message) }
            }
        }
    }
}
```
</details>

**关键点**：`StateFlow` 始终有值，重放最新；无生命周期感知。

**追问与答案**  
1. **`StateFlow` 会重放吗？**  
   答：始终重放最新值给新订阅者。  
2. **`StateFlow` 和 `LiveData` 区别？**  
   答：`StateFlow` 无生命周期感知，需 `repeatOnLifecycle`；`LiveData` 生命周期感知。

---

### 题目 32：`SharedFlow` 一次性事件

**题目描述**  
用 `SharedFlow` 实现一次性事件。

<details>
<summary>点击查看代码</summary>

```kotlin
class EventViewModel : ViewModel() {
    private val _events = MutableSharedFlow<Event>(
        replay = 0,
        extraBufferCapacity = 1,
        onBufferOverflow = BufferOverflow.DROP_OLDEST
    )
    val events: SharedFlow<Event> = _events.asSharedFlow()

    fun trigger() {
        viewModelScope.launch {
            _events.emit(Event.Toast("hello"))
        }
    }
}

sealed class Event {
    data class Toast(val msg: String) : Event()
    data class Navigate(val route: String) : Event()
}
```
</details>

**关键点**：`replay=0` 不重放；`SharedFlow` 广播。

**追问与答案**  
1. **`SharedFlow` 和 `Channel` 区别？**  
   答：`SharedFlow` 广播多订阅者；`Channel` 单消费。  
2. **`SharedFlow` 和 `StateFlow` 区别？**  
   答：`SharedFlow` 可无初始值、可重放多个；`StateFlow` 始终有值、只重放最新。

---

### 题目 33：简化版 `debounce`

**题目描述**  
手写简化版 `debounce`。

<details>
<summary>点击查看代码</summary>

```kotlin
fun <T> Flow<T>.myDebounce(timeoutMs: Long): Flow<T> = flow {
    var lastValue: T? = null
    var job: Job? = null

    collect { value ->
        lastValue = value
        job?.cancel()
        job = launch {
            delay(timeoutMs)
            lastValue?.let { emit(it) }
        }
    }
}
```
</details>

**关键点**：取消旧 job，延迟后发射。

**追问与答案**  
1. **`debounce` 和 `sample` 区别？**  
   答：`debounce` 取稳定后最后一个；`sample` 周期采样。  
2. **`debounce` 底层？**  
   答：标准库用 `produceIn` + `select` 实现，更高效。

---

### 题目 34：背压：`buffer`、`conflate`、`collectLatest`

**题目描述**  
对比 Flow 背压处理。

<details>
<summary>点击查看代码</summary>

```kotlin
fun main() = runBlocking {
    val flow = flow {
        for (i in 1..5) {
            delay(100)
            emit(i)
        }
    }

    flow.collect { delay(300); println("default: $it") }
    flow.buffer(2).collect { delay(300); println("buffer: $it") }
    flow.conflate().collect { delay(300); println("conflate: $it") }
    flow.collectLatest { delay(300); println("latest: $it") }
}
```
</details>

**关键点**：`buffer` 加缓冲；`conflate` 只保留最新；`collectLatest` 取消旧处理。

**追问与答案**  
1. **`buffer` 和 `flowOn` 区别？**  
   答：`flowOn` 改变上游上下文；`buffer` 只加缓冲，不改变上下文。  
2. **`conflate` 和 `collectLatest` 区别？**  
   答：`conflate` 丢弃中间值，保留最新；`collectLatest` 取消旧处理，处理最新。

---

### 题目 35：`shareIn` 和 `stateIn` 用法与区别

**题目描述**  
将冷流转为热流。

<details>
<summary>点击查看代码</summary>

```kotlin
class MyViewModel : ViewModel() {
    private val repository = Repository()

    val sharedFlow: SharedFlow<Data> = repository.dataFlow()
        .shareIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000),
            replay = 1
        )

    val stateFlow: StateFlow<Data> = repository.dataFlow()
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000),
            initialValue = Data.Empty
        )
}
```
</details>

**关键点**：`shareIn` 返回 `SharedFlow`；`stateIn` 返回 `StateFlow`，有初始值。

**追问与答案**  
1. **`shareIn` 和 `stateIn` 区别？**  
   答：`stateIn` 返回 `StateFlow`，有初始值，去重；`shareIn` 返回 `SharedFlow`，更灵活。  
2. **`replay` 和 `extraBufferCapacity` 区别？**  
   答：`replay` 给新订阅者重放；`extraBufferCapacity` 给慢消费者缓冲。  
3. **为什么用 `WhileSubscribed`？**  
   答：避免无订阅者时浪费资源，有订阅者时启动，无订阅者延迟停止。

---

### 题目 36：`retry` 和 `retryWhen` 操作符

**题目描述**  
实现 Flow 失败重试。

<details>
<summary>点击查看代码</summary>

```kotlin
fun fetchData(): Flow<String> = flow {
    if (Random.nextBoolean()) throw IOException("network error")
    emit("success")
}

fun simpleRetry(): Flow<String> = fetchData().retry(3)

fun advancedRetry(): Flow<String> = fetchData()
    .retryWhen { cause, attempt ->
        if (cause is IOException && attempt < 5) {
            delay(1000L * (attempt + 1))
            true
        } else {
            false
        }
    }
```
</details>

**关键点**：`retry` 固定次数；`retryWhen` 自定义条件。

**追问与答案**  
1. **`retry` 和 `retryWhen` 区别？**  
   答：`retry` 固定次数；`retryWhen` 自定义条件、延迟、异常类型。  
2. **重试会重新执行上游吗？**  
   答：会，冷流重新执行。  
3. **如何避免无限重试？**  
   答：用 `attempt < N` 限制。

---

### 题目 37：`flowOn` 与 `buffer` 的区别与上下文切换

**题目描述**  
解释 `flowOn` 和 `buffer` 区别。

<details>
<summary>点击查看代码</summary>

```kotlin
fun main() = runBlocking {
    val flow = flow {
        println("Upstream thread: ${Thread.currentThread().name}")
        emit(1)
        emit(2)
    }

    flow.flowOn(Dispatchers.IO)
        .collect { println("Collect thread: ${Thread.currentThread().name}") }

    flow.buffer(2)
        .collect { println("Collect: $it") }
}
```
</details>

**关键点**：`flowOn` 切换上游上下文；`buffer` 只加缓冲。

**追问与答案**  
1. **`flowOn` 和 `withContext` 区别？**  
   答：`flowOn` 只作用于上游；`withContext` 作用于整个代码块。  
2. **`flowOn` 多次调用？**  
   答：只有最近的一次生效，且只影响上游。  
3. **`buffer` 和 `flowOn` 一起用？**  
   答：可以，`flowOn` 切上下文，`buffer` 加缓冲。

---

## 六、反射、KSP、编译期

### 题目 38：Kotlin 反射：获取类信息、调用方法

**题目描述**  
使用 Kotlin 反射获取类信息并调用方法。

<details>
<summary>点击查看代码</summary>

```kotlin
data class User(val name: String, var age: Int) {
    fun greet(): String = "Hello, $name"
}

fun main() {
    val kClass = User::class
    println("Class: ${kClass.simpleName}")

    kClass.memberProperties.forEach { prop ->
        println("Property: ${prop.name}, type: ${prop.returnType}")
    }

    val user = User("Alice", 30)
    val greet = kClass.memberFunctions.find { it.name == "greet" }
    val result = greet?.call(user)
    println("greet result: $result")

    val nameProp = kClass.memberProperties.find { it.name == "name" }
    println("name: ${nameProp?.get(user)}")
}
```
</details>

**关键点**：需 `kotlin-reflect`；性能低于 Java 反射。

**追问与答案**  
1. **Kotlin 反射和 Java 反射区别？**  
   答：Kotlin 反射支持可空性、默认参数、扩展等；Java 反射更底层。  
2. **反射性能问题？**  
   答：有开销，避免热路径，缓存 `KProperty`/`KFunction`。  
3. **如何反射调用伴生对象方法？**  
   答：通过 `companionObject` 实例获取。

---

### 题目 39：KSP：注解处理器与 KAPT 对比

**题目描述**  
编写简单 KSP 处理器，生成类。

<details>
<summary>点击查看代码</summary>

```kotlin
@Target(AnnotationTarget.CLASS)
annotation class GenerateHello

class HelloProcessor(
    private val codeGenerator: CodeGenerator,
    private val logger: KSPLogger
) : SymbolProcessor {
    override fun process(resolver: Resolver): List<KSAnnotated> {
        val symbols = resolver.getSymbolsWithAnnotation(GenerateHello::class.qualifiedName!!)
        symbols.filterIsInstance<KSClassDeclaration>().forEach { classDecl ->
            val className = classDecl.simpleName.asString()
            val file = codeGenerator.createNewFile(
                Dependencies(false, classDecl.containingFile!!),
                packageName = classDecl.packageName.asString(),
                fileName = "Generated_$className"
            )
            file.write("fun hello$className() = \"Hello from $className\"\n".toByteArray())
            file.close()
        }
        return emptyList()
    }
}
```
</details>

**关键点**：KSP 直接分析 Kotlin，不生成存根，比 KAPT 快。

**追问与答案**  
1. **KSP 和 KAPT 区别？**  
   答：KAPT 生成 Java 存根再处理，慢；KSP 直接分析 Kotlin，快 2-5 倍。  
2. **KSP 能处理 Java 注解吗？**  
   答：能，但主要面向 Kotlin。  
3. **KSP 生成代码如何增量编译？**  
   答：通过 `Dependencies` 声明依赖关系。

---

## 七、Compose

### 题目 40：`remember`、`rememberSaveable`、`derivedStateOf` 区别

**题目描述**  
解释三者区别。

<details>
<summary>点击查看代码</summary>

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    var savedCount by rememberSaveable { mutableStateOf(0) }
    val isEven by remember { derivedStateOf { count % 2 == 0 } }

    Column {
        Text("Count: $count, isEven: $isEven")
        Button(onClick = { count++ }) { Text("Increment") }
    }
}
```
</details>

**关键点**：`remember` 配置变更丢失；`rememberSaveable` 恢复；`derivedStateOf` 减少重组。

**追问与答案**  
1. **`remember` 和 `rememberSaveable` 区别？**  
   答：`remember` 在重组间保持，配置变更丢失；`rememberSaveable` 保存到 Bundle，配置变更恢复。  
2. **`derivedStateOf` 什么时候用？**  
   答：依赖多个状态计算一个值，且希望减少重组时。  
3. **`remember` 的 key 参数？**  
   答：key 变化时重新计算。

---

### 题目 41：`LaunchedEffect`、`DisposableEffect`、`SideEffect` 用法

**题目描述**  
解释三个副作用 API。

<details>
<summary>点击查看代码</summary>

```kotlin
@Composable
fun MyScreen(userId: String) {
    LaunchedEffect(userId) {
        fetchUser(userId)
    }

    DisposableEffect(Unit) {
        val listener = registerListener()
        onDispose {
            unregisterListener(listener)
        }
    }

    SideEffect {
        analytics.trackScreenView()
    }
}
```
</details>

**关键点**：`LaunchedEffect` 启动协程；`DisposableEffect` 清理；`SideEffect` 每次重组后执行。

**追问与答案**  
1. **`LaunchedEffect` 和 `rememberCoroutineScope` 区别？**  
   答：`LaunchedEffect` 自动管理生命周期，key 变化重启；`rememberCoroutineScope` 手动控制。  
2. **`DisposableEffect` 的 key？**  
   答：key 变化时触发 `onDispose` 并重新执行。  
3. **`SideEffect` 和 `LaunchedEffect` 区别？**  
   答：`SideEffect` 非挂起，每次重组执行；`LaunchedEffect` 挂起，key 变化重启。

---

## 八、多平台与测试

### 题目 42：Kotlin 多平台：`expect/actual` 机制

**题目描述**  
用 `expect/actual` 实现多平台共享。

<details>
<summary>点击查看代码</summary>

```kotlin
// commonMain
expect fun platformName(): String

expect class PlatformLogger() {
    fun log(message: String)
}

// androidMain
actual fun platformName(): String = "Android"

actual class PlatformLogger actual constructor() {
    actual fun log(message: String) {
        Log.d("PlatformLogger", message)
    }
}

// iosMain
actual fun platformName(): String = "iOS"

actual class PlatformLogger actual constructor() {
    actual fun log(message: String) {
        println(message)
    }
}
```
</details>

**关键点**：`expect` 声明，`actual` 实现；编译期绑定。

**追问与答案**  
1. **`expect/actual` 和接口区别？**  
   答：`expect/actual` 是编译期绑定，各平台实现；接口是运行时多态。  
2. **KMM 和 Flutter 区别？**  
   答：KMM 共享逻辑，UI 原生；Flutter 共享 UI。  
3. **`expect` 能用于顶层函数吗？**  
   答：能。

---

### 题目 43：Kotlin 测试：`runTest`、`TestDispatcher`、`Turbine`

**题目描述**  
用 `runTest` 测试协程，用 `Turbine` 测试 Flow。

<details>
<summary>点击查看代码</summary>

```kotlin
class MyTest {
    @Test
    fun testCoroutine() = runTest {
        val result = withContext(StandardTestDispatcher(testScheduler)) {
            delay(1000)
            "done"
        }
        assertEquals("done", result)
    }

    @Test
    fun testFlow() = runTest {
        val flow = flowOf(1, 2, 3)
        flow.test {
            assertEquals(1, awaitItem())
            assertEquals(2, awaitItem())
            assertEquals(3, awaitItem())
            awaitComplete()
        }
    }
}
```
</details>

**关键点**：`runTest` 虚拟时间；`Turbine` 提供 `awaitItem` 等。

**追问与答案**  
1. **`runTest` 和 `runBlocking` 区别？**  
   答：`runTest` 使用虚拟时间，`delay` 立即跳过；`runBlocking` 真实阻塞。  
2. **`UnconfinedTestDispatcher` 和 `StandardTestDispatcher` 区别？**  
   答：前者立即执行，后者需要 `advanceUntilIdle`。  
3. **Turbine 如何测试异常？**  
   答：用 `awaitError()`。

---

## 九、集合与类型系统

### 题目 44：集合高级操作：`groupBy`、`associate`、`fold`、`reduce`

**题目描述**  
用这些操作处理集合。

<details>
<summary>点击查看代码</summary>

```kotlin
data class Person(val name: String, val age: Int, val city: String)

val people = listOf(
    Person("Alice", 30, "Beijing"),
    Person("Bob", 25, "Shanghai"),
    Person("Charlie", 35, "Beijing")
)

val byCity: Map<String, List<Person>> = people.groupBy { it.city }
val nameToAge: Map<String, Int> = people.associate { it.name to it.age }
val totalAge = people.fold(0) { acc, person -> acc + person.age }
val maxAge = people.map { it.age }.reduce { acc, age -> maxOf(acc, age) }
```
</details>

**关键点**：`groupBy` 分组；`associate` 转 Map；`fold` 有初始值；`reduce` 无初始值。

**追问与答案**  
1. **`fold` 和 `reduce` 区别？**  
   答：`fold` 有初始值；`reduce` 无初始值，空集合抛异常。  
2. **`associateBy` 和 `associate` 区别？**  
   答：`associateBy` 指定 key 选择器，value 是元素本身；`associate` 自定义键值对。  
3. **`groupBy` 返回的 Map 可变吗？**  
   答：不可变。

---

### 题目 45：`Nothing`、`Unit`、`Any` 的区别与使用场景

**题目描述**  
解释三者区别。

<details>
<summary>点击查看代码</summary>

```kotlin
fun printHello(): Unit {
    println("Hello")
}

fun fail(message: String): Nothing {
    throw IllegalArgumentException(message)
}

fun log(obj: Any) {
    println(obj.toString())
}

val nullValue: Nothing? = null
```
</details>

**关键点**：`Unit` 无返回值；`Nothing` 永不返回；`Any` 非空根类型。

**追问与答案**  
1. **`Nothing` 和 `Unit` 区别？**  
   答：`Unit` 有返回值（单例）；`Nothing` 永不返回。  
2. **`Nothing` 能作为泛型参数吗？**  
   答：能，如 `Result<Nothing>`。  
3. **`Any` 和 `Object` 区别？**  
   答：`Any` 非空；`Any?` 可空；`Object` 是 Java 的。

---

## 十、Java 互操作与 Android 集成

### 题目 46：Java 友好 API

**题目描述**  
用 `@JvmStatic`、`@JvmOverloads`、`@Throws` 提供 Java 友好 API。

<details>
<summary>点击查看代码</summary>

```kotlin
class UserRepository {
    companion object {
        @JvmStatic
        fun create(): UserRepository = UserRepository()

        @JvmField
        val DEFAULT_NAME = "unknown"
    }

    @JvmOverloads
    fun fetch(id: Long, name: String = DEFAULT_NAME) { }

    @Throws(IOException::class)
    fun loadFile(path: String): String { ... }
}
```
</details>

**关键点**：`@JvmStatic` 生成静态方法；`@JvmField` 暴露字段；`@JvmOverloads` 生成重载。

**追问与答案**  
1. **`@JvmStatic` 和 `@JvmField` 区别？**  
   答：`@JvmStatic` 用于方法，生成静态方法；`@JvmField` 用于属性，直接暴露字段。  
2. **`@JvmOverloads` 对构造函数有效吗？**  
   答：有效。

---

### 题目 47：平台类型安全封装

**题目描述**  
封装 Java 平台类型，安全处理 `null`。

<details>
<summary>点击查看代码</summary>

```java
// Java
public class JavaApi {
    public String getName() { return null; }
}
```

```kotlin
fun JavaApi.safeName(): String = name ?: ""
fun JavaApi.safeName2(): String = requireNotNull(name) { "name is null" }
```
</details>

**关键点**：平台类型 `String!` 可空性未知；用 `?:` 或 `requireNotNull` 兜底。

**追问与答案**  
1. **`!!` 和 `requireNotNull` 区别？**  
   答：`!!` 抛 NPE；`requireNotNull` 可自定义消息。  
2. **平台类型能显式声明吗？**  
   答：不能。

---

### 题目 48：`viewModelScope` + `StateFlow` MVVM

**题目描述**  
用 `viewModelScope` + `StateFlow` 实现 MVVM。

<details>
<summary>点击查看代码</summary>

```kotlin
class UserViewModel(
    private val repo: UserRepository
) : ViewModel() {

    private val _state = MutableStateFlow(UserState())
    val state: StateFlow<UserState> = _state.asStateFlow()

    init { load() }

    fun load() {
        viewModelScope.launch {
            _state.update { it.copy(loading = true) }
            runCatching { repo.fetchUser() }
                .onSuccess { user ->
                    _state.update { it.copy(loading = false, user = user) }
                }
                .onFailure { e ->
                    _state.update { it.copy(loading = false, error = e.message) }
                }
        }
    }
}

// Activity
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.state.collect { render(it) }
    }
}
```
</details>

**关键点**：`viewModelScope` 生命周期绑定；`StateFlow` 无生命周期感知，需 `repeatOnLifecycle`。

**追问与答案**  
1. **`viewModelScope` 底层？**  
   答：`CloseableCoroutineScope`，在 `onCleared` 时取消。  
2. **`repeatOnLifecycle` 和 `flowWithLifecycle` 区别？**  
   答：`repeatOnLifecycle` 是通用块；`flowWithLifecycle` 是 Flow 操作符。

---

### 题目 49：`repeatOnLifecycle` 简化版

**题目描述**  
手写简化版 `repeatOnLifecycle`。

<details>
<summary>点击查看代码</summary>

```kotlin
fun LifecycleOwner.myRepeatOnLifecycle(
    state: Lifecycle.State,
    block: suspend CoroutineScope.() -> Unit
): Job = lifecycleScope.launch {
    var job: Job? = null
    lifecycle.whenStateAtLeast(state) {
        job?.cancel()
        job = launch(block = block)
    }
}
```
</details>

**关键点**：生命周期达到目标状态启动，低于则取消。

**追问与答案**  
1. **`repeatOnLifecycle` 和 `flowWithLifecycle` 区别？**  
   答：前者是通用块，后者是 Flow 操作符。  
2. **为什么需要它？**  
   答：`StateFlow` 无生命周期感知，避免后台收集导致泄漏。

---

### 题目 50：上下文接收者（Context Receivers）与 `@JvmInline` 深入

**题目描述**  
介绍上下文接收者与 `@JvmInline`。

<details>
<summary>点击查看代码</summary>

```kotlin
// 上下文接收者（Kotlin 2.0 实验性）
context(Logger, Database)
fun saveUser(user: User) {
    log("Saving user ${user.name}")
    db.insert(user)
}

class Logger { fun log(msg: String) = println(msg) }
class Database { fun insert(user: User) = println("inserted") }

with(Logger()) {
    with(Database()) {
        saveUser(User("Alice"))
    }
}

// @JvmInline 深入
@JvmInline
value class Password(val value: String) {
    init {
        require(value.length >= 6) { "Password too short" }
    }
}

fun login(password: Password) { /* ... */ }
```
</details>

**关键点**：上下文接收者用于依赖注入；`@JvmInline` 减少装箱。

**追问与答案**  
1. **上下文接收者和扩展函数区别？**  
   答：上下文接收者可有多个，显式声明依赖；扩展函数只有一个接收者。  
2. **`@JvmInline` 限制？**  
   答：只能一个属性，不能继承类，不能有 `init` 块？可以有 `init` 块（如示例）。  
3. **值类何时装箱？**  
   答：作为可空、泛型、接口时装箱。

---
