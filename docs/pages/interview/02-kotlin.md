# Kotlin知识点速记

## Kotlin 基础语法(P0)

1. Kotlin 与 Java 的主要语法差异有哪些？[💡][kotlin-syntax]  
2. Kotlin 中有哪些基础类型，和 Java 有何不同？[💡][kotlin-data-type]  
3. `val` 和 `var` 有什么区别？[💡][kotlin-var-val]  
4. `const val` 和 `val` 区别？[💡][kotlin-const-val]  
5. Kotlin 如何处理可空类型？[💡][kotlin-null-safety]  
6. Kotlin 空安全实现原理？[💡][kotlin-null-safety-principle]  
7. `is` 和 `as` 用来做什么？[💡][kotlin-is-as]
8. `!!` 和 `?.` 区别？[💡][kotlin-nullable-if]
9. `?:`(Elvis操作符) 的作用？[💡][kotlin-elvis]
10. 平台类型 `T!` 是什么？[💡][kotlin-platform-type]  
11. `lateinit` 和 `by lazy` 区别？[💡][kotlin-lazy-lateinit]  
12. `==` 和 `===` 区别？[💡][kotlin-equals]  
13. `Nothing`、`Unit`、`Any` 区别？[💡][kotlin-nothing-unit-any]  
14. `Nothing?` 有什么用？[💡][kotlin-nullable-nothing]  
15. Kotlin 如何写字符串模板？[💡][kotlin-string-template]  
16. Kotlin 数组和集合有什么区别？[💡][kotlin-array-list]  
17. Kotlin 如何对集合进行函数式操作？[💡][kotlin-collection]  
18. Kotlin 的类型系统支持关系类型吗？[💡][kotlin-type-relation]  
19. Kotlin 中的关键字 inline / crossinline / noinline 有什么用？[💡][kotlin-function-inline]
20. Kotlin 中什么是高阶函数？[💡][kotlin-advanced-function]  
21. Kotlin 中如何定义 Lambda 表达式？[💡][kotlin-lambda]  
22. Kotlin 中的匿名函数与 Lambda 有什么区别？[💡][kotlin-anonymous-function]  
23. Kotlin 的闭包特性是什么？[💡][kotlin-closure]  
24. Kotlin 中的 `with`、`let`、`apply`、`run`、`also` 有何区别？[💡][kotlin-internal-function]  
25. `takeIf` 和 `takeUnless` 的作用是什么？[💡][kotlin-take]  
26. 什么是尾递归优化（tailrec）？[💡][kotlin-tailrec]  
27. Kotlin 如何支持函数类型声明？[💡][kotlin-function-type-declaration]
28. Kotlin 函数默认参数和命名参数如何使用？[💡][kotlin-function-default-params]  
29. Kotlin 如何调用 Java 代码？[💡][kotlin-calls-java]  
30. Java 如何调用 Kotlin？有哪些限制？[💡][kotlin-called-from-java]  
31. Kotlin 如何处理 Java 的 `null` 值？[💡][kotlin-java-null]  
32. Kotlin 如何兼容 Java 的 `SAM` 接口？[💡][kotlin-java-sam]  
33. Kotlin 中的 `@JvmStatic`、`@JvmField`、`@JvmOverloads` 有什么作用？[💡][kotlin-java-annotation]  
34. 如何使用 Kotlin 写工具类供 Java 调用？[💡][kotlin-java-utils]
35. Kotlin 写的 API 对 Java 开发者的友好建议？[💡][kotlin-java-api]  

[kotlin-syntax]: . "1. 无分号、变量空安全、类型推断、没有static(伴生对象替代)、when 表达式&#10; 2. 方法默认public、类默认不可继承、内部类不持有外部类引用&#10; 3. 高阶函数、扩展函数、委托、类扩展函数、类型别名&#10; 4. 数据类、密封类、枚举类&#10; 5.*本质是语法糖，编译成class和 Java 完全互通"
[kotlin-data-type]: . "1、Byte/Short/Int/Long/Float/Double/Boolean/Char&#10; 2、编译后映射基本类型，可空/泛型映射包装类型&#10; 3. *语法相同，自动拆装箱"
[kotlin-var-val]: . "var可变，val不可变；初始化差异； *val非常量，对象仍然可变"
[kotlin-const-val]: . "const val是编译期常量，只能在顶层或类属性，会内联，val可以有自定义的getter"
[kotlin-null-safety]: . "编译期检查，T?和T，?. ?: !! requireNotNull()/checkNotNull() 类型转换as/as? 扩展函数 平台类型T!和Java互操作"
[kotlin-null-safety-principle]: . "注解、函数入口处Intrinsics检查、?.等操作符变成条件判断、*平台类型不校验"
[kotlin-is-as]: . "is类型检查，as类型转换。&#10;is可以做自动类型推断*"
[kotlin-nullable-if]: . "!!是断言抛异常、?.安全调用"
[kotlin-elvis]: . "左值null返回右值，否则返回左值"
[kotlin-platform-type]: . "Java 中的类型在 Kotlin 中未知，Kotlin中可空非空都有可能。Kotlin中空指针主要来源"
[kotlin-lazy-lateinit]: . "lateinit用于var，非空属性，延迟手动赋值&#10; by lazy是属性委托，在第一次被使用时执行代码块，可指定线程安全模式"
[kotlin-equals]: . "==是值比较等同于 Java 的equals&#10;===是引用比较，等同于 Java 的=="
[kotlin-nothing-unit-any]: . "Nothing：任意类型的子类型，无法实例化，常用于函数标记异常&#10;Unit 类似于 Java 中的void，表示函数无返回值，全局单例&#10; Any：所有非空类型的父类，类似于 Java 的 Object 类"
[kotlin-nullable-nothing]: . "表示值只能是null的类型"
[kotlin-string-template]: . "用$符号，${name}"
[kotlin-array-list]: . "数组定长、对应Java原生数组，基本类型&#10;集合分可变和不可变、可变集合可扩容、通常装箱、只读集合编译后仍然是可变"
[kotlin-collection]: . "map、flatMap、filter、forEach、fold、reduce、groupBy、sortedBy、associate"
[kotlin-type-relation]: . "不支持类似于TS中的 String|Number，但是支持泛型的型变"
[kotlin-function-inline]: . "inline，内联函数，只能修饰函数，支持reified保留泛型，*会暴漏私有成员，编译期有限制&#10;noinline，只能修饰lambda参数，禁用内联&#10;crossinline，禁止非局部返回"
[kotlin-advanced-function]: . "函数参数或返回值是函数的函数"
[kotlin-lambda]: . "{n: Int -> n + 1}"
[kotlin-anonymous-function]: . "写法差异，lambda不能指定返回值类型，只能用带标签的return，匿名函数不能拖尾，单参数不能简写"
[kotlin-closure]: . "lambda或匿名函数类访问修改外部变量，Java 不能修改。&#10;原理：Ref包装实现跨栈修改&#10; 核心特性：非捕获生成单例、捕获型生成 Function 对象，内联消除中间对象&#10;隐患：内存泄漏、线程安全"
[kotlin-internal-function]: . "let: it，返回最后一行&#10;also: it，本身;&#10;with: 多一个参数，this，最后一行&#10;run:this，返回最后一行；&#10;apply: this，返回本身"
[kotlin-take]: . "takeIf正取，takeUnless反取"
[kotlin-tailrec]: . "递归语句在最后，编译器优化成循环，*仅限直接尾递归"
[kotlin-function-type-declaration]: . "普通函数、匿名函数、可空函数类型、带接受者函数类型、挂起函数类型、高阶返回类型"
[kotlin-function-default-params]: . "fun foo(x: Int = 0, y: Int = 100)，使用 foo(b = 10)"
[kotlin-calls-java]: . "字节码层面100%兼容，注意：平台类型的空安全、集合的可变性、主动捕获异常、关键字冲突、符合SAM替换成lambda、属性前缀setter/getter、运算符重载"
[kotlin-called-from-java]: . "默认参数、伴生对象、类属性补全、顶层成员、异常处理、数组类型、异常加注解。内联函数带reified参数无法调用"
[kotlin-java-null]: . "平台类型 T!，用可空类型接收"
[kotlin-java-sam]: . "Java接口，在Kotlin中用lambda；Kotlin接口用fun interface"
[kotlin-java-annotation]: . "@JvmStatic: 伴生对象生成静态方法&#10;@JvmField: 不生成getter/setter&#10;@JvmOverloads:函数默认值重载"
[kotlin-java-utils]: . "object 或者 companion object + @JvmStatic、顶层函数用@JvmName、避免暴露 value class和默认参数"
[kotlin-java-api]: . "伴生对象@JvmStatic、函数默认参数@JvmOverloads、异常@Throw、函数别名@JvmName&#10;避免value class、默认参数、内联函数、顶层函数直接暴露"

## 类、对象、委托(P0)

1. Kotlin 中类的默认修饰符是什么？[💡][kotlin-class-access]  
2. Kotlin 支持多类继承吗？[💡][kotlin-inherit]  
3. Kotlin 如何实现方法重写？[💡][kotlin-override]  
4. Kotlin 是否支持方法重载（函数重载）？[💡][kotlin-overload]  
5. Kotlin 中如何定义抽象类和接口？[💡][kotlin-abstact-class-interface]  
6. 什么是 `data class`？[💡][kotlin-data-class]
7. `data class`编译后能自动生成什么方法？[💡][kotlin-data-class-method]
8. `data class` 有什么要求？[💡][kotlin-data-class-require]  
9. 什么是 `sealed class`？适合什么场景？[💡] [kotlin-sealed-class] 
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

[kotlin-class-access]: . "默认public，还有internal、protected、private，internal是模块可见，但是有个例外是test能访问main"
[kotlin-inherit]: . "和 Java 一样，类仅支持单继承，支持实现多个接口。接口可以继承多个接口。"
[kotlin-override]: . "open类，方法前加override（强制），加 final 禁止子类重写。属性也可以重写"
[kotlin-overload]: . "方法名相同，参数不同"
[kotlin-abstact-class-interface]: . "abstrace class 和 interface，抽象类不加open子类可以继承，接口可以有默认实现"
[kotlin-data-class]: . "数据类，主构造函数中声明的属性自动生成equals/hashCode/copy/toString/componentN方法"
[kotlin-data-class-method]: . "equals/hashCode/copy/toString/componentN，仅主构造函数中声明的属性生成"
[kotlin-data-class-require]: . "主构造函数至少有一个属性，全部是val/var，不能abstract/open/innner/sealed"
[kotlin-sealed-class]: . "密封类，所有的子类必须在编译期确定且在同一个包内。适用有限状态：网络请求结果状态、UI 状态、when枚举"

## 扩展、内联、泛型（P0/P1）

1. 扩展函数原理？  
2. 扩展函数能访问私有成员吗？  
3. `inline` 作用？  
4. `noinline` 和 `crossinline` 区别？  
5. `reified` 作用？  
6. `reified` 限制？  
7. 什么是 Kotlin 逆变 `in`、协变  `out`?  
8. 为什么协变限制写入，逆变限制读取 ?
9. `List<out T>` 为什么协变？  
10. `MutableList` 型变？  
11. 泛型擦除是什么？  

## 协程 Coroutine

1. Kotlin 中的协程是什么？基本使用方式有哪些？  
2. Kotlin 中的协程和线程的区别？
3. Kotlin 协程的核心概念有哪些？  
4. 什么是结构化并发（Structured Concurrency）？有什么优点？
5. Kotlin 的协程是基于什么实现的？是语言层面的语法糖还是库层实现？  
6. 协程和线程使用场景？  
7. 如何取消协程？ `Job.cancel()` 的原理是什么？
8. `NonCancellable` 作用？
9. 协程取消是协作式的吗？
10. 如何将协程切换到主线程？协程是怎么在多线程间切换上下文的？  
11. CoroutineDispatcher 有哪些常用实现？它们适合什么场景？  
12. 什么是 `CoroutineContext`？你是否自定义过上下文元素？  
13. 协程作用域 `CoroutineScope`是什么？为什么建议在适当作用域中启动协程？  
14. `supervisorScope` 和 `coroutineScope` 的区别？  
15. 什么是 `ViewModelScope`？为何要使用它？  
16. 什么是挂起函数（suspend function）？它和普通函数的本质区别是什么？  
17. `suspend` 修饰函数能否独立调用？  
18. 挂起函数执行过程中如果不检查取消，会发生什么？如何改进？  
19. `suspend` 原理是什么？
20. 协程是如何实现挂起和恢复的？底层原理知道多少？  
21. 协程和线程、线程池之间的关系？是如何调度执行的？  
22. 如何优雅地做协程任务的并发控制？  
23. `launch`、`async`、`runBlocking` 有什么区别？使用场景？
24. 如何用 `async` 并发执行两个耗时任务，并收集它们的结果？  
25. `runBlocking` 在 Android 中能否用？什么时候用它是合理的？  
26. `async`、`await`、`join`的区别是什么？  
27. 什么是 `SupervisorJob`？与普通 `Job` 有何区别？何时用它？  
28. Job、Deferred区别是什么？  
29. `withContext` 和 `launch` 的区别？ 用法场景如何区分？  
30. 怎么写一个能自动超时的协程操作？你用过 `withTimeout()` 吗？  
31. `withTimeout` 和 `withTimeoutOrNull` 区别？
32. `Mutex` 和 `synchronized` 区别？
33. `Channel` 和 `Flow` 区别？
34. 如何处理协程中的异常？协程中的异常是如何传播的？如何捕获？
35. 如何在 Android 中优雅处理协程异常？
36. `CoroutineExceptionHandler` 是如何工作的？在哪些场景有效？
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
3. Flow 的异常处理方式？  
4. Flow 默认在哪个线程执行？如何切换上下文？  
5. 冷流（cold flow）与热流（hot flow）的区别？  
6. 什么是 `SharedFlow` 和 `StateFlow`？它们的区别？  
7. `StateFlow` 和 `LiveData` 区别？
8. 如何取消 Flow 的收集？  
9. Flow 的背压策略如何控制？  
10. 什么是 `Channel`? 与 `Flow` 的区别？  
11. 如何用 `Channel` 实现并发消息处理？
12. `SharedFlow` 和 `Channel` 区别？  
13. `flatMapLatest` 和 `flatMapMerge` 区别？  
14. `buffer`、`conflate`、`collectLatest` 区别？  
15. `flowOn` 和 `buffer` 区别？  
16. `shareIn` 和 `stateIn` 区别？  
17. `SharingStarted` 策略？  
18. `callbackFlow` 作用？  
19. `retry` 和 `retryWhen` 区别？  
20. `catch` 能捕获下游异常吗？  
21. 如何使用 Kotlin Flow 结合 LiveData？  
22. 在 Jetpack Compose 中如何使用协程与 Flow？  
23. Android 中为何 prefer Flow over LiveData？
24. Jetpack Compose 中如何实现 UI 与 State 解耦？  

## DSL (P2)

1. DSL 核心？带接收者 lambda + apply，链式配置
2. @DslMarker 作用  
3. apply 和 also 区别？  
4. let、run、with 区别？  
5. Kotlin DSL 在 Android 中有哪些应用？  

## 集合与标准函数（P1）

1. Sequence 和 Iterable 区别？[💡][kotlin-sequence-iterable]  
2. fold 和 reduce 区别？[💡][kotlin-fold-reduce]  
3. associate 和 associateBy 区别？[💡][kotlin-associate]  
4. groupBy 返回什么？[💡][kotlin-group-by]  

[kotlin-sequence-iterable]: . "Sequence是惰性求值，Iterable 是每一步都生成中间集合"
[kotlin-fold-reduce]: . "fold有初始值，reduce无初始值，空集合会抛异常"
[kotlin-associate]: . "associate 自定义键值对；associateBy 指定 key，value 是元素本身"
[kotlin-group-by]: . "Map<K, List<T>>，按 key 分组。"

## Java 互操作（P1）

1. Kotlin 调 Java 平台类型风险？[💡][kotlin-platform-type-risk]  
2. Java 调 Kotlin 非空参数传 null？[💡][kotlin-java-call-null]  
3. Kotlin 可空性如何传给 Java？[💡][kotlin-parse-nullable-to-java]
4. @JvmOverloads 作用？[💡][kotlin-jvm-overloads-annotation]
5. @Throws 作用？[💡][kotlin-jvm-throws-annotation]
6. @JvmName 作用？[💡][kotlin-javmname-annotation]  
7. @JvmSuppressWildcards 作用？[💡][kotlin-jvm-supress-wildcards-annotation]  
8. `fun interface` 作用？[灯泡][kotlin-fun-interface]  

[kotlin-platform-type-risk]: . "可空性未知，当非空用可能 NPE。"
[kotlin-java-call-null]: . "编译通过，运行时抛异常 Intrinsics.checkNotNullParameter()"
[kotlin-parse-nullable-to-java]: . "生成 @Nullable/@NotNull 注解，Java IDE 可见但不强制。"
[kotlin-jvm-overloads-annotation]: . "默认参数生成重载方法，方便 Java 调用。"
[kotlin-jvm-throws-annotation]: . "Kotlin函数没有throws，声明受检异常，Java 强制捕获。"
[kotlin-javmname-annotation]: . "修改生成的类名、方法名、getter/setter 名。"
[kotlin-jvm-supress-wildcards-annotation]: . "抑制泛型通配符生成。"
[kotlin-fun-interface]: . "让 Kotlin 接口支持 SAM 转换，Java 可用 lambda。"

## 反射、KSP、编译期（P2）

1. Kotlin 反射和 Java 反射区别？

- Kotlin 反射需 kotlin-reflect，支持可空性、默认参数；性能更低。

1. KSP 和 KAPT 区别？

- KSP 直接分析 Kotlin 不生成存根，快 2-5 倍；KAPT 生成 Java 存根。

1. K2 编译器是什么？

- Kotlin 2.0 新编译器，前端重写，性能更好。

1. value class 编译后字节码？

- 多数场景内联为底层类型，方法名修饰。

1. inline 函数字节码？

- 函数体展开到调用处，lambda 内联，无对象分配。

## Compose (P1)

1. 声明式 UI 和命令式区别？

- 声明式描述状态对应 UI，状态变化重组；命令式手动更新 View。

1. 重组是什么？

- 状态变化时重新执行 Composable，只更新变化部分。

1. remember 和 rememberSaveable 区别？

- remember 配置变更丢失；rememberSaveable 保存到 Bundle 恢复。

1. derivedStateOf 作用？

- 从其他状态派生，减少重组。

1. LaunchedEffect、DisposableEffect、SideEffect 区别？

- LaunchedEffect 启动协程 key 变化重启；DisposableEffect 清理；SideEffect 每次重组后执行。

## 手写代码

1. 手写 `safeCase` 类型转换  
2. 手写 `by lazy` 线程安全  
3. 手写 `observable` 委托  
4. 手写 `startActivity<T>`
5. 手写 `debounce` 简化版  
6. 手写 `repeatOnLifecycle` 简化版
