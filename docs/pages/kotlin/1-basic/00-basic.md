# Kotlin 基础

## 变量

**变量声明**

- `val`，赋值后不可改变变量的值，和Java中的final修饰的变量相似
- `var`，赋值后可以改变值

```kotlin
val count: Int = 10
count = 11 // 编译报错

var sum: Int = 20
sum = count + sum // sum的值变为30
```

- `const`，声明常量

`const` 关键字用于修饰 val 类型的变量，表明该 **变量** 是一个常量。只能修饰顶层属性和类属性，且值必须在编译期就确定，类型只能是 String 和基本类型。

总结：

- `val` 和`var` 可以修饰顶层属性、类属性、局部变量
- `val` 修饰类属性，可以生成 `getter` 方法，`var` 修饰类属性可以生成 `getter` 和`setter` 方法。
- 局部变量不会有 `getter` 和 `setter`，`val` 修饰局部变量相当于 Java 中的 final
- `const` 只能修饰顶层属性和类属性，**值必须在编译期确定**，值的类型只能是 String 和final 类型。编译之后，`const` 修饰的变量都被内联替换了。

**类型推断**

声明变量时同时赋值，即使不显式声明变量的类型，编译器也可以推断出变量的类型。

```kotlin
val count = 10  // Int
val name = 'Tom' // String 

name.inc() // 编译报错，String没有inc()方法
```

**空安全**

Kotlin中，默认类型是非空的，给非空类型变量赋值会编译错误。如果期望变量时可空的，需要在类型后加上`?`

```
val name: String = null // 编译报错

val name: String? = null
```

## 常见操作符

与Java中不一样的操作符

- `?` 表明类型是可空的，如 `val name: String? = null`
- `?:` Elvis操作符，表明左值为空时，取右值，如 `val firstName = name?:'unknown'`，firstName的值是unknown
- `?.` 安全调用，左值为空时，值也返回空，如 `val length = name?.length`，length的值也为null
- `!!` 断言一个表达式非空，如果为空会抛异常
- `==` 与 `!=` 值相等比较，等同于Java中的equals，但是 == 是线程安全的，null == "abc" 不会报错
- `===` 与 `!==` 引用比较，比较的是内存地址，等同于Java中的==
- `$` 字符串模板中引用变量或表达式
- `_` 在lambda或解构中代替未使用的参数

**类型判断**

`is` 和 `!is` 可以用来做类型判断，相当于 Java 中的 instanceof，用 is 判断了类型之后，在代码块中可以自动调用对应类型的方法，例如：

```kotlin
if (obj is String) {
    print(obj.length)
}

if (obj !is String) { // 与 !(obj is String) 相同
    print("Not a String")
} else {
    print(obj.length) // 智能转换
}
```

**类型转换**

`as` 可以用来做类型转换，相当于 Java 中的强制类型转换。不安全的转换会在编译期报错。

```kotlin
val x: String = y as String
```

`as?` 可以做安全的类型转换，当转换失败是返回 null 。

```kotlin
val x: String? = y as? String
```


## 数据类型

### 基本的数据类型

Kotlin 不像 Java 一样，没有原始类型（primitive types），一切都是对象。但是编译器会优化编译产物，根据可空或者非空，编译成原始类型或者包装类型：

- 可空类型被编译成包装类型，例如 `Int? --> Integer`
- 非空类型被编译成原始类型，例如 `Int --> int`

### Unit、Any、Nothing

- `Any` 所有非空类型的父类，类似于 Java 中的 Object;
- `Nothing` 表示“永远不会返回，或者不存在的值”，不能被实例化，通常把一个函数的返回值设置为 Nothing 表明这个函数不会返回会抛异常。由于 Nothing 可以赋值给任意类型，也可以将它看做是任意类型的子类型。
- `Unit` 表示“无意义的返回值”，但是Unit有一个实例

```
         Any          ← 所有非空类型的根类型
        / | \
     Int  String  ...
       \  |  /
       Nothing        ← 所有类型的子类型（底类型）

         Any?         ← 所有类型的根类型（包括可空）
        / | \
     Int? String? ...
       \  |  /
       Nothing?       ← 唯一的值是 null
```

```kotlin
// 抛一个异常
fun fail(message: String): Nothing {
    throw IllegalArgumentException(message)
}

val name: String = user.name ?: fail() // 赋值给String类型的变量
val age: String = if user.age > 0 user.age else fail() // 赋值给Int类型的变量
```

## 类型转换 as 和 as?

as 是非安全的类型转换，等同于 Java 中的 `()`，转换失败会抛异常。

```kotlin
val aaa = "aaa"

val bbb = aaa as String
val ccc = aaa as Int // ❌ 会抛出ClassCastException
```

as? 是安全的类型转换，当转换失败会返回 null。

```kotlin
val aaa = "aaa"

val ddd = aaa as? String
val eee = aaa as? Int // ✅ eee 的值会是 null
```

## 条件语句

**if-else**

常规用法和 Java 一样，但是可以 Kotlin 中的 if-else 可以用来当条件表达式，例如：

```kotlin
val String message = if (code == 400) {
  "client error"
} else if (code == 500) {
  "server error"
} else {
  "known error
}
```

Kotlin 中没有 Java 中的三目运算符 ?:，类似的用法都可以用三元表达式来实现。

**when**

当条件较多时，也可以用 `when` 关键字来做条件判断，示例：

```kotlin
var message: String

when {
  code == 400 -> "client error"
  code == 500 -> "server errro"
  else -> "known error"
}
```

`when` 可以带参数也可以不带参数，带参数时，when 的每个条件的返回值都是参数的类型，例如：

```kotlin
var message: String

when (code) {
  200 -> "ok"
  400 -> "client error"
  500 -> "server errro"
  else -> "known error"
}
```

----

*参考*

[1] [学习 Kotlin 编程语言](https://developer.android.google.cn/kotlin/learn?hl=zh-cn).Android Developers  
[2] [关键字与操作符](https://book.kotlincn.net/text/keyword-reference.html).Kotlin 官方文档 中文版  
[4] [Get started with Kotlin](https://kotlinlang.org/docs/getting-started.html)  
[5] 阿正的梦工坊.[Kotlin 面试题全面解析：从基础到进阶](https://blog.csdn.net/shizheng_Li/article/details/161193265).CSDN.2026-05-18