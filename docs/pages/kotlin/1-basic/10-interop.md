# Kotlin-Java 互操作

Kotlin 和 Java 在 JVM 层面是 100% 兼容，完全支持互相操作，但是日常混着开发中也需要一些注意点。

## Kotlin 调用 Java

**1. 空安全**  

Java 中的变量没有是否可空，不带 `Nullable` 和 `NonNull`注解的变量， 在 Kotlin 中都是平台类型 `T!`，Kotlin 不会强校验空。比较安全的做法是都当做可空类型来用。

**2. 集合可变性**  

Java 中的集合不区分是否可修改，返回给 Kotlin 的集合被视为 `List<T!>!`，如果 Java 侧返回的是 `Collections.unmodifiableList()`、`Collections.emptyList`、`Arrays.asList()` 这类不允许修改的集合，Kotlin 侧尝试去修改元素，运行时会抛异常。

安全的做法是把 Java 侧返回的集合都当做是只读集合，如果确实需要修改，要拷贝一份。

**3. 异常捕获**  

Kotlin 没有受检查异常机制，即使 Java 中方面签名上有 throw 关键字声明了受检查异常(CheckedExceptions)抛出，编译器也不会有任何的警告。

调用 Java 的 IO、反射等存在异常的 API 时，应当主动去添加 try-catch.

**4. 关键字冲突**  

Java中的变量或者方法有可能是 Kotlin 中的关键字，这类调用的时候，需要用反引号 `` 来转义。

```kotlin

val node: TreeNode = TreeNode(1)
println("node.val is ${node.`val`}")

```

**5. lambda 参数**  

如果符合 SAM 转换的参数可以用lambda，如果lambda参数在最后，还可以简化写法，把 lambda 放在()外面。

比如 RxJava2 中的 `Flowable.create`：

```java
public static <T> Flowable<T> create(
    FlowableOnSubscribe<T> source,
    BackpressureStrategy mode) { /* … */ }
```

FlowableOnSubscribe 就可以用 lambda

```kotlin
Flowable.create({ /* … */ }, BackpressureStrategy.LATEST)
```

如果 `Flowable.create` 的两个参数换个顺序，还能继续简写：

```kotlin
Flowable.create(BackpressureStrategy.LATEST) { /* … */ }
```

**6. 属性前缀**  

如果 Java 中的属性的 getter/setter 方法严格按照 bean 样式的写法，即 getXXX、setXXX、isXXX，在 kotlin 中使用的时候，可以省略掉掉前缀。

```java
public final class User {
  public String getName() { /* … */ }
  public void setName(String name) { /* … */ }
  public boolean isActive() { /* … */ }
  public void setActive(boolean active) { /* … */ }
}
```

```kotlin
user.name = "Bob" // 调用 user.setName(String)
user.isActive = true // 调用 user.setActive(boolean)
```

**7. 运算符重载**  

如果 Java 中的方法名符合 kotlin 中运算符重载的写法，kotlin 中调用时，可以直接用重载的运算符调用。

例如：

```java
public final class IntBox {
  private final int value;
  public IntBox(int value) {
    this.value = value;
  }
  public IntBox plus(IntBox other) {
    return new IntBox(value + other.value);
  }
}
```

```kotlin
val one = IntBox(1)
val two = IntBox(2)
val three = one + two // 相当于调用 one.plus(two)
```

## Java 调用 Kotlin

**1. 默认参数**  

Java 中没有默认参数，调用 Kotlin 时，需要把参数都补全。或者加上 `@JvmOverloads` 注解，生成重载的函数。

**2. 伴生对象**  

Kotlin 伴生对象的方法，Java 必须通过 MyClass.Companion.foo() 访问。也可以加上 `@JvmStatic` 使其生成静态方法。

**3. 类属性**  

Kotlin 中的类属性，Java 中调用要补全 get 和 set 前缀，通过 getXXX 和 setXXX 来访问。加上 `@JvmField` 会取消生成 getter 和 setter 方法。

**4. 顶层函数和变量**  

Java 中所有的方法和属性都需要写在类中，Kotlin 中的顶级函数和属性，需要通过文件名访问，比如 Utils.kt 中的顶层函数和变量，需要通过 `UtilsKt.foo()` 来访问。也可以通过 `@file:JvmName("StringUtils")` 让文件生成特定的类名。

对于函数，使用 `@JvmName("foo")` 可以对其重命名，在 Java 中通过重命名的名字访问。

**5. 异常**  

Kotlin 函数中没有 `throw` 关键字用来声明该函数会抛出异常，Java 里调用方没法在 catch 中捕获对应的异常（编译报错）。需要在 Kotlin 函数上增加 `@Throws(IOException::class)` 注解。

## 调用限制

**1. Java 无法调用带 `reified` 的内联函数**  

带 `reified` 的内联函数，依赖编译器在调用时将泛型替换成具体类型，Java 调用时编译期没法解析，所以无法调用。

```kotlin
// Functions.kt
inline fun <reified T> getType() {
    println("type is ${T::class.java}")
}
```

```java
FunctionsKt.getType<>(); // ❌ 编译报错
```

**2. Kotlin internal 成员对 Java 是 public 的**  

JVM 字节码里没有模块可见的概念，生成的 internal 成员还是 public 的，只不过名字被混淆，并且带上的模块后缀。

**3. 基本类型数组映射差异**  

基本类型的数组在 Kotlin 中都有特定的类，比如 `int[] --> IntArray`，`char[] --> CharArray`。如果直接使用 `Array<Int>`，对应的是包装类型，如果对性能敏感，需要注意。

**参考**  

1.[Kotlin-Java 互操作指南](https://developer.android.google.cn/kotlin/interop?hl=zh-cn). Android Developer
