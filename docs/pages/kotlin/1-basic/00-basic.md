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

- `const`，声明常量

`const`关键字用于修饰val类型的变量，表明该'变量'是一个常量。只能修饰顶层属性和类属性，且值必须在编译期就确定，类型只能是String和基本类型。

总结：

- `val`和`var`可以修饰顶层属性、类属性、局部变量
- `val`修饰类属性，可以生成`getter`方法，`var`修饰类属性可以生成`getter`和`setter`方法。
- 局部变量不会有`getter`和`setter`，`val`修饰局部变量相当于Java中的final
- `const`只能修饰顶层属性和类属性，值必须在编译期确定，值的类型只能是String和final类型。

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

**类型判断**

`is`和`!is`可以用来做类型判断，相当于Java中的instanceof，用is判断了类型之后，在代码块中可以自动调用对应类型的方法，例如：

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

`as`可以用来做类型转换，相当于Java中的强制类型转换。不安全的转换会在编译期报错。

```kotlin
val x: String = y as String
```

`as?`可以做安全的类型转换，当转换失败是返回null。

```kotlin
val x: String? = y as? String
```

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

简单的函数声明可以省略{}，例如：

```kotlin
fun sum(n : Int, m : Int) = n + m // 省略了花括号和返回值，因为可以根据类型推断出返回类型
```

### 匿名函数

匿名函数没有函数名，可以将其赋值给变量，变量的类型为 `(参数类型, 参数类型) -> 返回值类型`，调用的时候加上括号，例如：

```java 
// 声明匿名函数
val multi: (Double, Double) -> Double = { x, y ->
    x + y
}

// 使用匿名函数
multi(2.0, 3.0)
val mm = multi
mm(2.0, 3.0)
```

### 高阶函数

高阶函数指的是函数的参数也是函数，例如：

```java
fun advancedFunc(m: Int, mapper: (Int) -> String) : String{
    return mapper(m)
}

advancedFunc(10, { num -> "$num"})
```

高阶函数的最后一个参数如果是匿名函数，可以把这个匿名函数放在调用的圆括号外面，gradle的kotlin DSL中有很多这种用法。例如上面的调用可以写成：

```
advancedFunc(10) { num ->
  "$num"
}
```

高阶函数会有一些运行时上的开销，因为函数是一个对象，在函数的实现中，会访问局部变量，因此在内存占用和虚拟调用都会有一定的开销。

### 内联函数

内联函数通过inline关键字修饰，会将调用函数的地方内联成函数的实现。内联函数会引入额外的代码，不过使用得当也能提升性能。

```kotlin
inline fun inlineFun(m: Int, mapper: (Int) -> String) : String {
    return mapper.invoke(m)
}
```

如果不希望传给函数的参数被内联，也可以用noinline参数修复函数参数。noinline关键字不能修饰函数，可以修饰函数参数。

```kotlin
inline fun inlineParams(m: Int, mapper: (Int) -> String, noinline reducer: (Int) -> Int): String {
    return mapper.invoke(reducer.invoke(m))
}
```

## 类


*参考*

1. [学习 Kotlin 编程语言](https://developer.android.google.cn/kotlin/learn?hl=zh-cn)
2. [关键字与操作符](https://book.kotlincn.net/text/keyword-reference.html)