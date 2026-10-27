# 空安全

Kotlin 空安全的目标是把 NPE 从运行时尽可能提前到编译期来发现，最核心的思路就是在数据类型上强制区分「可空类型」和「非空类型」，强制要求在编译期处理可能存在的 null。

## 数据类型

数据类型默认是非空，需要为可空类型时，在类型后加?。

```kotlin
var name: String = "Alice"  // 非空类型
var name: String? = "Alice" // 可空类型
```

## lateinit 与 by lazy

变量需要初始化的时候，可以用 `lateinit` 和 `by lazy`，用法上有些差异

| 特性     | `lateinit`  | `by lazy` |
|---------|--------------|-----------|
| 适用类型  |  非空引用类型 | 任意       |
| 可变性   |   `var`      | `val`     |
| 初始化   |  手动         | 首次访问   |
| 线程安全 |   否          | 可配置     |
| 可重置   |        否     |  否 |

## 安全调用操作符 ?.

如果调用的对象是 null，返回值也是 null，用来简化 if else 的调用。尤其在链式调用中，任何一个对象是 null，返回结果都是null。

## Elvis 操作符 ?:

类似于 js 中的 `||` ，当左边的值为空时，返回右边的值或者执行右边的表达式。也可以与 `return`、`throw`结合起来用。

```kotlin
fun process(name: String?) {
    val n = name ?: return
    val m = name ?: throw IllegalArgumentException("name is null")
}
```

## 非空断言 !!

断言一个表达式非空，如果为空会抛 KotlinNullPointerException 异常。

```kotlin
val name: String? = null
val length = name!!.length // 运行时抛 NPE
```

只有当确定非空的时候才使用，否则优先用`?.`、`?:`、`requireNotNull`。

## requireNotNull、checkNotNull

会抛出不同的异常。

```kotlin
fun process(name: String?) {
    val n = requireNotNull(name) { "name is null" } // 抛 IllegalArgumentException
    val m = checkNotNull(name) { "name is null" }   // 抛 IllegalStateException
}
```

对比 `!!` 可以自定义异常信息。

## 安全的类型转换 as?

当类型不匹配转换失败时，直接返回 null，如果直接用 as，则会抛异常。

## 可空类型扩展函数

给可空类型定义扩展函数时，可以在函数对 null 进行处理，比如：

```kotlin
fun String?.orEmpty(): String = this ?: ""

val s: String? = null
println(s.orEmpty()) // ""
```

## let、run、also、apply 处理可空

调用时加一个安全操作符?

```kotlin
val name: String? = "Alice"

// let：非空时执行
name?.let { println(it.length) }

// run：非空时执行并返回结果
val length = name?.run { this.length } ?: 0

// also：非空时执行副作用
name?.also { println("name: $it") }
```

## when表达式
 
when 表达式可以直接判断 null，而不是像 Java 中的 switch 一样抛出异常。

```kotlin
fun describe(name: String?): String = when (name) {
    null -> "no name"
    else -> "name: $name"
}
```

## 平台类型 T! 和 Java 的互操作

Java 中的类型在 Kotlin 中无法确定是否可空，用 `T!` 表示。比较安全的做法是，对没有 `NonNull` 注解的类型，都当做可空类型来处理。

## 智能转换

Kotlin 中在类型已经明确为不为空时，可以将可空类型智能转换非空类型：

```kotlin
fun process(name: String?) {
    if (name != null) {
        println(name.length) // String? 智能转换为 String
    }
}
```
支持：

- if (x != null)
- x?.let { }
- when (x) { is Type -> }
- requireNotNull(x)

不支持：

- var 属性（可能被其他线程修改）。
- 自定义 getter 属性。

## 集合与可空元素

集合中的泛型可以是非空类型也可以是可空类型，可以用 `list.filterNotNull()` 将集合处理成元素都是非空的。

- `List<String?>`: 集合非空，集合中的元素可空
- `List<String>?`: 集合可空，集合中的元素非空
- `List<String?>?`: 集合可空，集合中的元素可空

## 泛型中的空安全

```kotlin
fun <T> List<T>.firstOrNull(): T? = if (isEmpty()) null else this[0]
```
泛型中的 `T` 默认非空，`T?` 是可空。

## 反射中的空安全

```kotlin
val kClass = String::class
println(kClass.isMarkedNullable) // false
val nullableClass = String::class.createType(nullable = true)
println(nullableClass.isMarkedNullable) // true
```

**参考**

1. [空安全](https://book.kotlincn.net/text/null-safety.html).Kotlin 官方文档 中文版