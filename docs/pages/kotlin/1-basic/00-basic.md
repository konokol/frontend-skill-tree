# Kotlin 入门

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
- `==` 与 `!=` 值相等比较，等同于Java中的equals
- `===` 与 `!==` 引用比较，比较的是内存地址，等同于Java中的==
- `$` 字符串模板中引用变量或表达式
- `_` 在lambda或解构中代替未使用的参数

## 条件语句

**if-else**

常规用法和Java一样，但是可以Kotlin中的if-else可以用来当条件表达式，例如：

```kotlin
val String message = if (code == 400) {
  "client error"
} else if (code == 500) {
  "server error"
} else {
  "known error
}
```

Kotlin中没有Java中的三目运算符 ?:，类似的用法都可以用三元表达式来实现。

**when**

当条件较多时，也可以用`when`关键字来做条件判断，示例：

```kotlin
var message: String

when {
  code == 400 -> "client error"
  code == 500 -> "server errro"
  else -> "known error"
}
```

## 函数

### 匿名函数

### 高阶函数

### 内联函数

## 类


*参考*

1. [学习 Kotlin 编程语言](https://developer.android.google.cn/kotlin/learn?hl=zh-cn)
2. [关键字与操作符](https://book.kotlincn.net/text/keyword-reference.html)