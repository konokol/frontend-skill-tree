# Kotlin知识点速记

## Kotlin 基础语法(P0)

1. Kotlin 与 Java 的主要语法差异有哪些？  
2. Kotlin 中有哪些基础类型？和 Java 有何不同？  
3. `val` 和 `var` 有什么区别？  
4. `const val` 和 `val` 区别?  
4. Kotlin 如何处理可空类型？  
5. Kotlin空安全实现原理?  
6. `is` 和 `as` 用来做什么？
7. `!!` 和 `?.` 区别？ 
8. `?:`(Elvis操作符) 的作用？ 
9. 平台类型 `T!` 是什么？  
10. `lateinit` 和 `by lazy` 区别？  
11. `==` 和 `===` 区别？  
12. `Nothing`、`Unit`、`Any` 区别？ 
13. `Nothing?` 有什么用？ 
15. Kotlin 如何写字符串模板？  
17. Kotlin 数组和集合有什么区别？  
18. Kotlin 如何对集合进行函数式操作？  
19. Kotlin 的类型系统支持关系类型吗？  
20. Kotlin 中的关键字 inline / crossinline / noinline 有什么用？     
21. Kotlin 中什么是高阶函数？  
22. Kotlin 中如何定义 Lambda 表达式？  
23. Kotlin 中的匿名函数与 Lambda 有什么区别？  
24. Kotlin 的闭包特性是什么？  
25. Kotlin 中的 `with`、`let`、`apply`、`run`、`also` 有何区别？  
26. `takeIf` 和 `takeUnless` 的作用是什么？  
27. 什么是尾递归优化（tailrec）？  
28. Kotlin 如何支持函数类型声明？  
29. Kotlin 函数默认参数和命名参数如何使用？  
32. Kotlin 如何调用 Java 代码？  
33. Java 如何调用 Kotlin？有哪些限制？  
34. Kotlin 如何处理 Java 的 `null` 值？  
35. Kotlin 如何兼容 Java 的 `SAM` 接口？  
36. Kotlin 中的 `@JvmStatic`、`@JvmField`、`@JvmOverloads` `const val` 有什么作用？  
37. 如何使用 Kotlin 写工具类供 Java 调用？ 
38. Kotlin 写的 API 对 Java 开发者的友好建议？  
 
## 类、对象、委托(P0)

1. Kotlin 中类的默认修饰符是什么？  
2. Kotlin 支持多类继承吗？  
3. Kotlin 如何实现方法重写？  
4. Kotlin 是否支持方法重载（函数重载）？  
5. Kotlin 中如何定义抽象类和接口？  
6. 什么是 `data class`？
7. `data class`编译后能自动生成什么方法？
8. `data class` 有什么要求？  
9. 什么是 `sealed class`？适合什么场景？  
10. `data object` 和 `object` 区别？
11. `object` 声明和对象表达式区别？
12. 伴生对象(`companion object`)有什么用？  
13. Kotlin 如何定义单例？  
14. Kotlin 中是否支持内部类？  
15. 嵌套类和内部类有什么区别？  
16. `inner class` 如何访问外部类？
17. `value class` 是什么？  
18. `value class` 何时装箱？  
19. `typealias` 和 `value class` 区别？
20. Kotlin 支持委托机制吗？
21. 属性委托需要实现什么？  
22. `by lazy` 线程安全模式有哪几种？  
23. `observable` 和 `vetoable` 区别？ 
24. `provideDelegate` 作用？  
25. 类委托底层实现原理？  
26. 密封类和枚举区别？  
27. 密封接口和密封类选择？
28. Java 的枚举与 Kotlin 的 `enum class`、`sealed class` 有何差异？  

## 扩展、内联、泛型（P0/P1）

1. 扩展函数原理？  
2. 扩展函数能访问私有成员吗？  
3. `inline` 作用？  
4. `noinline` 和 `crossinline` 区别？  
5. `reified` 作用？  
6. `reified` 限制？  
7.  什么是 Kotlin 逆变 `in`、协变  `out`?  
8.  为什么协变限制写入，逆变限制读取 ?   
9.  `List<out T>` 为什么协变？  
10. `MutableList` 型变？  
11. 泛型擦除是什么？  

## 协程 Coroutine

1. Kotlin 协程是什么？基本使用方式有哪些？  
2. Kotlin 中的协程和线程的区别？  
3. Kotlin 的协程是基于什么实现的？是语言层面的语法糖还是库层实现？  
4. 协程和线程使用场景？  
5. 如何取消协程？ `Job.cancel()` 的原理是什么？ 
6. `NonCancellable` 作用？
7. 协程取消是协作式的吗？
8. 如何将协程切换到主线程？协程是怎么在多线程间切换上下文的？  
9. Kotlin 协程的核心概念有哪些？   
10. CoroutineDispatcher 有哪些常用实现？它们适合什么场景？  
11. 什么是 `CoroutineContext`？你是否自定义过上下文元素？  
12. 协程作用域 `CoroutineScope`是什么？为什么建议在适当作用域中启动协程？  
13. `supervisorScope` 和 `coroutineScope` 的区别？  
14. 什么是 `ViewModelScope`？为何要使用它？  
15. 什么是挂起函数（suspend function）？它和普通函数的本质区别是什么？  
16. `suspend` 修饰函数能否独立调用？  
17. 挂起函数执行过程中如果不检查取消，会发生什么？如何改进？  
18. `suspend` 原理是什么？
19. 协程是如何实现挂起和恢复的？底层原理知道多少？  
20. 协程和线程、线程池之间的关系？是如何调度执行的？  
21. 如何优雅地做协程任务的并发控制？  
22. `launch`、`async`、`runBlocking` 有什么区别？使用场景？   
23. 如何用 `async` 并发执行两个耗时任务，并收集它们的结果？  
24. `runBlocking` 在 Android 中能否用？什么时候用它是合理的？  
25. `async`、`await`、`join`的区别是什么？  
26. 什么是 `SupervisorJob`？与普通 `Job` 有何区别？何时用它？  
27. Job、Deferred区别是什么？  
28. `withContext` 和 `launch` 的区别？ 用法场景如何区分？  
29. 怎么写一个能自动超时的协程操作？你用过 `withTimeout()` 吗？  
30. `withTimeout` 和 `withTimeoutOrNull` 区别？
31. `Mutex` 和 `synchronized` 区别？
32. `Channel` 和 `Flow` 区别？
33. 如何处理协程中的异常？协程中的异常是如何传播的？如何捕获？ 
34. 如何在 Android 中优雅处理协程异常？   
35. `CoroutineExceptionHandler` 是如何工作的？在哪些场景有效？
36. 什么是结构化并发（Structured Concurrency）？有什么优点？ 
37. `isActive()`、`ensureActive()`、`yield()` 这些函数你用过吗？各自作用？  
38. 你在项目中是如何使用协程的？是否与 `ViewModel`、`LiveData`、`Flow` 结合使用？  
39. `viewModelScope` 和 `lifecycleScope` 分别是什么？为何推荐使用它们？  
40. 你用过 `LiveData` + `Coroutine` 的组合吗？如何处理生命周期？  
41. 协程在 `Activity` 被销毁后仍在运行，会发生什么问题？如何避免？  
42. 你有一个网络请求 + 本地缓存的场景，怎么用协程实现？需要考虑并发和取消。  
43. 启动多个协程，如果其中某个失败，其他协程怎么办？如何控制它们的取消策略？  
44. 协程为什么可能导致内存泄漏？你遇到过吗？  
45. 为什么说协程虽然轻量，但不是免费线程？过度使用有什么风险？  
46. 协程在 Android 中的常见坑有哪些？   
47. Kotlin 的协程如何从 Java 调用？ 
48. 如何在 Activity / Fragment 中感知协程生命周期？ 
49. Kotlin 协程 + Retrofit 请求方式是怎样的？  

## Flow（P0）


1. 什么是 Flow？与传统协程有何区别？  
2. Flow 的基本使用方式有哪些？  
4.  Flow 的异常处理方式？  
5.  Flow 默认在哪个线程执行？如何切换上下文？  
6.  冷流（cold flow）与热流（hot flow）的区别？  
7.  什么是 `SharedFlow` 和 `StateFlow`？它们的区别？  
8.  `StateFlow` 和 `LiveData` 区别？
9.  如何取消 Flow 的收集？  
10. Flow 的背压策略如何控制？  
11. 什么是 `Channel`? 与 `Flow` 的区别？  
12. 如何用 `Channel` 实现并发消息处理？ 
13. `SharedFlow` 和 `Channel` 区别？  
14. `flatMapLatest` 和 `flatMapMerge` 区别？  
15. `buffer`、`conflate`、`collectLatest` 区别？  
16. `flowOn` 和 `buffer` 区别？  
17. `shareIn` 和 `stateIn` 区别？  
18. `SharingStarted` 策略？  
19. `callbackFlow` 作用？  
20. `retry` 和 `retryWhen` 区别？  
21. `catch` 能捕获下游异常吗？  
22. 如何使用 Kotlin Flow 结合 LiveData？  
23. 在 Jetpack Compose 中如何使用协程与 Flow？  
24. Android 中为何 prefer Flow over LiveData？    
25. Jetpack Compose 中如何实现 UI 与 State 解耦？  

## DSL (P2)

1. DSL 核心？带接收者 lambda + apply，链式配置
2. @DslMarker 作用  
3. apply 和 also 区别？  
4. let、run、with 区别？  
5. Kotlin DSL 在 Android 中有哪些应用？  

## 集合与标准函数（P1）

1. Sequence 和 Iterable 区别？  
  - Iterable 立即求值生成中间集合；Sequence 惰性逐元素。
2. fold 和 reduce 区别？  
  - fold 有初始值；reduce 无初始值，空集合抛异常。
3.  associate 和 associateBy 区别？  
  - associate 自定义键值对；associateBy 指定 key，value 是元素本身。
4.  groupBy 返回什么？  
  - Map<K, List<T>>，按 key 分组。
5.  let/run/with/apply/also 速记？
  - let it 返回；run this 返回；with this 返回；apply this 自身；also it 自身。

## Java 互操作（P1）

1. Kotlin 调 Java 平台类型风险？
  - 可空性未知，当非空用可能 NPE。  
2. Java 调 Kotlin 非空参数传 null？
  - 编译通过，运行时抛 NPE（Intrinsics.checkNotNullParameter）。  
3. Kotlin 可空性如何传给 Java？
   - 生成 @Nullable/@NotNull 注解，Java IDE 可见但不强制。  
4. @JvmOverloads 作用？
  - 默认参数生成重载方法，方便 Java 调用。
5. @Throws 作用？
  - 声明受检异常，Java 强制捕获。
6. @JvmName 作用？
  - 修改生成的类名、方法名、getter/setter 名。
7. @JvmSuppressWildcards 作用？
  - 抑制泛型通配符生成。
8. fun interface 作用？
  - 让 Kotlin 接口支持 SAM 转换，Java 可用 lambda。

## 反射、KSP、编译期（P2）

1. Kotlin 反射和 Java 反射区别？
  - Kotlin 反射需 kotlin-reflect，支持可空性、默认参数；性能更低。
2. KSP 和 KAPT 区别？
  - KSP 直接分析 Kotlin 不生成存根，快 2-5 倍；KAPT 生成 Java 存根。
3. K2 编译器是什么？
  - Kotlin 2.0 新编译器，前端重写，性能更好。
4. value class 编译后字节码？
  - 多数场景内联为底层类型，方法名修饰。
5. inline 函数字节码？
  - 函数体展开到调用处，lambda 内联，无对象分配。

## Compose (P1)

1. 声明式 UI 和命令式区别？
  - 声明式描述状态对应 UI，状态变化重组；命令式手动更新 View。
2. 重组是什么？
  - 状态变化时重新执行 Composable，只更新变化部分。
3. remember 和 rememberSaveable 区别？
  - remember 配置变更丢失；rememberSaveable 保存到 Bundle 恢复。
4. derivedStateOf 作用？
  - 从其他状态派生，减少重组。
5. LaunchedEffect、DisposableEffect、SideEffect 区别？
  - LaunchedEffect 启动协程 key 变化重启；DisposableEffect 清理；SideEffect 每次重组后执行。

## 手写代码

1. 手写 `safeCase` 类型转换  
2. 手写 `by lazy` 线程安全  
3. 手写 `observable` 委托  
4. 手写 `startActivity<T>`
5. 手写 `debounce` 简化版  
6. 手写 `repeatOnLifecycle` 简化版