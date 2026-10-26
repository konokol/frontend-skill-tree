
# 类和对象

## 类

### 类的构造

Kotlin 中类实例化不需要使用 new 关键字。

**构造函数**

类有一个主构造函数，和多个次构造函数。当主构造函数没有修饰符时，可以省略constructor关键字。

```kotlin
// 主构造函数
class Person constructor(firstName: String) { /*……*/ }

// 可省略constructor参数
class Person(firstName: String) { /*……*/ }

// 次级构造函数
class Person(val name: String) {
    val children: MutableList<Person> = mutableListOf()
    constructor(name: String, parent: Person) : this(name) {
        parent.children.add(this)
    }
}
```

### 可见性

Kotlin 中类默认都是不可继承的(抽象类除外)，如需继承，需要加 `open` 关键字。

### 特殊的类

**密封类**

密封类通过 `sealed` 关键字修饰，所有直接继承自密封类的子类都必须在**编译期**确定。1.5 之前，密封类只能定义在同一个文件中，1.5 之后放宽了限制，密封类的子类可以定义在相同包的任意文件中，但是超出对应包之后，还是会编译失败。1.5 中还引入了密封接口，用法类似。

```kotlin
// SealedClass.kt
package com.kotlin.classes

sealed class Expr

data class Const(val number: Double) : Expr()

object NotNumber: Expr()

// SealedClassOtherFile.kt -- 同一个包下的其他文件也可以定义密封类的子类
package com.kotlin.classes

class Empty(string: String): Expr()

// SealedClassOtherModule.kt -- 其他包中类不可以直接继承密封类
package com.kotlin.class2

import com.kotlin.classes.Expr

package com.kotlin.class2

// 编译失败，因为Expr在另一个包中
class Empty(string: String): Expr()
```

Java 15 中新增了一个新的关键字 `sealed`，和 Kotlin 中的密封类用法一样

密封类的使用场景：

- 只想要有限的继承：想要在编译期知道全部的类型。
- 对类型安全有诉求：状态管理、复杂逻辑处理等场景，可以用when表达式，枚举出所有的场景，保重不出现意料之外的类型。
- 封闭API：例如开发SDK时，只期望对外暴露有限的接口

**数据类**

数据类型通过 `data` 关键字修饰，编译器会自动生成 `equals()`、`hashCode()`、`toString()`、`copy()`、`componentN` 等方法。

```kotlin
data class User(val name: String, var age: Int)
```

**嵌套类和内部类**

Kotlin 中的**嵌套类**默认不可以访问外部的成员变量，等同于 Java 中的静态内部类，但是可以访问外部类的伴生对象。  
如需访问外部类的成员变量或方法，需要用**内部类**，加 `inner` 关键字修饰。

```kotlin
class Outer {
    val outerProp = "outer"
    companion object { val COMPANION = "companion" }

    /**嵌套类**/
    class Nested {
        fun foo() {
            // println(outerProp) // 编译错误：不能访问外部类实例成员
            println(COMPANION)    // 可以访问伴生对象
        }
    }

    /**内部类**/
    inner class Inner {
        fun foo() {
            println(outerProp)          // 直接访问外部类成员
            println(this@Outer.outerProp) // 显式引用
        }
    }
}
```

匿名内部类用`object`表达式创建，会持有外部类的引用。如果不需要持有外部类的引用，要用 lambda 表达式。

```kotlin
button.setOnClickListener(object : View.OnClickListener {
    override fun onClick(v: View?) {
        // 如果是内部类，会持有外部类引用
    }
})

button.setOnClickListener { v -> ... } // 不持有外部类的引用。
```

**枚举类**

枚举类的每一个枚举值都是一个枚举类的实例，因此枚举值可以实现枚举类的抽象方法和接口。

**内联类**

```kotlin
@JvmInline
value class UserId(val id: Long)
```
内联类(inline class)是 Kotlin 1.3 引入的实验性特性，在 1.5 之后修改成了值类(data class)，并要求使用 JvmInline 注解。内联类相当于是对类型做了一层包装，用来保证类型安全。比如 Android 中常用的单位dp、sp、px 都是 Float 类型，容易误传，可以使用内联内包装。

内联类有一些要求：

- 主构造函数只能有一个 `val` 属性
- 不能有 `var` 属性
- 可以实现接口，但不能继承其他类（除了 Any），也不能被其他类继承（是 final 的）
- 可以有 `init` 块、方法、伴生对象

原理：内联类编译之后会可能会变成基本类型，能够减少类型包装带来的开销。如果内联类有函数，会被编译成 final 类型的，同时在字节码中会加上后缀，因此如果要提供给 Java 调用，不要使用内联类。

内联类典型的使用场景：Compose中大量使用dp、sp。协程内部用 value class 包装 CoroutineContext.Key，减少开销。

```kotlin
@JvmInline value class Dp(val value: Float)
@JvmInline value class Sp(val value: Float)
@JvmInline value class Px(val value: Float)
```

## 对象

### 对象声明

对象声明使用 `object` 关键字。对应的 Java 代码是静态内部类实现的单例。由于是静态内部类实现的单例，也是线程安全的（由 JVM 的类加载机制保证）。

```kotlin
object Singleton {
    val name = "Singleton"
    fun doSomething() { println("Doing") }
}

// 使用
Singleton.doSomething()
println(Singleton.name)
```

常见的对象声明：

- 普通对象：`object Foo {}`。
- 伴生对象：`companion object {}`，与外部类关联，成员可以通过外部类访问。
- 数据对象：`data object Foo { }`，自动生成 `toString/equals/hashCode`，常用于密封类。和数据类的差异是数据对象是单例的、不会生成 `copy/componentN` 方法，不能解构。

数据对象常见的使用场景：

- 单例模式的实现
- 工具类和常量集合
- 伴生对象
- 接口的默认实现对象
- 密封类的无状态子类(data object)

### 对象表达式

```kotlin
// 实现接口
val listener = object : View.OnClickListener {
    override fun onClick(v: View?) {
        println("Clicked")
    }
}

// 继承类
val runnable = object : Thread() {
    override fun run() {
        println("Running")
    }
}

// 无继承，纯匿名对象
val obj = object {
    val x = 1
    fun foo() = "foo"
}
```

对象表达式也用 `object` 关键字，相当于是 Java 中的匿名内部类，可以实现接口、继承抽象类，也可以单纯写一个匿名对象。每次声明，都会创建一个新的示例。对象表达式内部也会持有外部类的引用。

### 伴生对象

```kotlin
class User {
    companion object {
        const val MAX_AGE = 150
        fun create(): User = User()
    }
}

// 通过类名直接访问
val user = User.create()
println(User.MAX_AGE)
```

伴生对象用 `companion` 关键字声明，相当于 Java 中静态内部类。每个类只能有一个伴生对象。

伴生对象的方法或属性用 `@JvmStatic、@JvmField、const val` 修饰之后，可以通过外部类的类名直接访问。

伴生对象的常见使用场景：

- 工厂方法 `User.create()`
- 常量 `User.MAX_AGE`
- 工具函数
- 单例
- 替代 Java 中的静态内部类

--- 

**参考**

[1] [嵌套类和内部类](https://book.kotlincn.net/text/nested-classes.html).Kotlin 官方文档 中文版  
[2] [枚举类](https://book.kotlincn.net/text/enum-classes.html).Kotlin 官方文档 中文版  
[3] [内联类](https://book.kotlincn.net/text/inline-classes.html).Kotlin 官方文档 中文版  
