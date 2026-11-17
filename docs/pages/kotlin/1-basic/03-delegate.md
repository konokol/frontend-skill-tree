# 委托

委托通过 by 关键字来实现。

## 属性委托

### 类的属性委托

在类中，可以将一个属性的 setter 和 getter 委托给另一个属性，委托的属性可以是：

- 顶层属性
- 同一个类实例中的其他属性
- 另一个类中的其他属性
  
把属性委托给别的属性时，需要加 :: 限定符实现。这种用法在对属性废弃非常有用。

```kotlin
var topLevelInt: Int = 0
class ClassWithDelegate(val anotherClassInt: Int)

class MyClass(var memberInt: Int, val anotherClassInstance: ClassWithDelegate) {
    var delegatedToMember: Int by this::memberInt // 委托给顶层属性
    var delegatedToTopLevel: Int by ::topLevelInt // 委托给同一个类中的其他属性

    val delegatedToAnotherClass: Int by anotherClassInstance::anotherClassInt // 委托给另一个类的属性
}
var MyClass.extDelegated: Int by ::topLevelInt
```

除了类型相同的属性委托，还可以把属性委托给map，在类的属性很多时很实用。

```kotlin
class User(val map: Map<String, Any?>) {
    val name: String by map
    val age: Int     by map
}

fun main() {
    val user = User(mapOf(
        "name" to "John Doe",
        "age"  to 25
    ))
//sampleStart
    println(user.name) // Prints "John Doe"
    println(user.age)  // Prints 25
//sampleEnd
}

```

### 内置标准委托

将属性的赋值委托给另一个方法，Kotlin 内置了一些默认的委托。

**1、延迟属性 by lazy**  

通过 `by lazy` 实现，当第一次读变量时，执行 lazy 代码块中的代码。

```kotlin
    val lazyVal: String by lazy {
        println("lazy init")
        "msg"
    }

    println(lazyVal)
    println(lazyVal)
```

lazy 还可以有一个线程安全参数：

- LazyThreadSafetyMode.SYNCHRONIZED 同步初始化，使用锁保证线程安全，代码块只会执行一次
- LazyThreadSafetyMode.PUBLICATION 并发场景下，代码块可能执行多次，多个线程都可以执行，最终只会保留第一次的值
- LazyThreadSafetyMode.NONE 无锁

```kotlin
    val lazyValue by lazy(LazyThreadSafetyMode.SYNCHRONIZED) {
        println("synchronized lazy init")
        "lazy msg"
    }
```

**2. 可观测属性 by Delegates.observable**  

属性变化时可以收到一个回调

```kotlin
var name: String by Delegates.observable("init") { property, old, new ->
    println("${property.name}: $old -> $new")
}

name = "Alice" // name: init -> Alice
```

**3. 条件赋值属性 by Delegates.vetoble**  

可以在代码块中对赋值做拦截

```kotlin
var age: Int by Delegates.vetoable(0) { _, old, new ->
    new >= 0 // 负数拒绝赋值
}
```

**4. 可空变量空值检查 by Delegates.notNull**  

当可空变量是空值时，读变量值会抛一个异常

```kotlin
var name: String by Delegates.notNull()
// println(name) // 抛 IllegalStateException
```

### 自定义委托

自己实现委托的方法，可以通过实现 ReadWriteProperty 或 ReadOnlyProperty 接口来实现。

```kotlin
class LoggingProperty<T>(
    private var value: T
) : ReadWriteProperty<Any?, T> {

    override fun getValue(thisRef: Any?, property: KProperty<*>): T {
        println("get ${property.name}: $value")
        return value
    }

    override fun setValue(thisRef: Any?, property: KProperty<*>, newValue: T) {
        println("set ${property.name}: $value -> $newValue")
        value = newValue
    }
}

var name: String by LoggingProperty("init")
```

也可以直接写 setValue 和 getValue 的 operator 方法

```kotlin
class SimpleDelegate<T>(private var value: T) {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): T = value
    operator fun setValue(thisRef: Any?, property: KProperty<*>, newValue: T) {
        value = newValue
    }
}

```

### provideDelegate

provideDelegate 是 Kotlin 属性委托中的一个拦截器操作符（operator fun provideDelegate），它的核心作用是：在“创建并绑定委托对象”的那一刻（类初始化阶段）介入，让你有机会根据属性的元数据（如属性名、注解）动态校验规则，或动态创建、配置并返回最终的委托实例。

**原理**  

对于属性委托 `val myProp by DelegateFactory()` ，如果 DelegateFactory 定义了 `operator fun provideDelegate(thisRef: T, prop: KProperty<*>): ReadOnlyProperty<T, V>`，编译器在底层会将其展开为类似如下的逻辑：

```kotlin
// 编译器生成的等效逻辑：
private val myProp$delegate = DelegateFactory().provideDelegate(this, ::myProp)
val myProp: Type
    get() = myProp$delegate.getValue(this, ::myProp)
```

`provideDelegate` 在宿主对象实例化（属性初始化）时就会立刻执行，并且它能直接拿到宿主对象（thisRef）和属性的反射元数据（prop: KProperty<*>）。

**应用场景**  

1. 动态自动获取属性名
2. 对象创建时进行规则校验（Fail-Fast）

## 类委托

类委托就是将一个类要实现的方法委托给另一个类实现。

```kotlin
interface Base {
    fun print()
}

class BaseImpl(val x: Int) : Base {
    override fun print() { 
        print(x) 
    }
}

class Derived(b: Base) : Base by b

fun main() {
    val base = BaseImpl(10)
    Derived(base).print()
}
```

在当前类中增加 override 方法之后，会覆盖委托中的实现。

类委托的实现原理是在生成的字节码中创建一个隐藏的private final字段来保存委托对象，调用方法时，如果没有加 override，调用委托对象的方法。

比如代码：

```kotlin
interface Printer {
    fun printMessage(msg: String)
    fun printLine()
}

class ConsolePrinter : Printer {
    override fun printMessage(msg: String) = println(msg)
    override fun printLine() = println("----")
}

// 使用 by 关键字将 Printer 接口委托给 p 实例
class EnhancedPrinter(p: Printer) : Printer by p {
    // 自己重写其中一个方法
    override fun printMessage(msg: String) {
        println("前缀: $msg")
    }
}

```

生成的字节码：

```java
public final class EnhancedPrinter implements Printer {
    // 1. 编译器自动生成的隐藏字段（命名通常为 $$delegate_0）
    private final Printer $$delegate_0;

    public EnhancedPrinter(@NotNull Printer p) {
        super();
        this.$$delegate_0 = p; // 2. 在构造函数中保存传入的委托实例
    }

    // 3. 开发者手动重写的方法：保留开发者自己的实现
    @Override
    public void printMessage(@NotNull String msg) {
        System.out.println("前缀: " + msg);
    }

    // 4. 开发者未重写的方法：编译器自动生成转发调用，直接委托给 $$delegate_0
    @Override
    public void printLine() {
        this.$$delegate_0.printLine();
    }
}
```

----

*参考*  

[1] Kotlin 中文文档. [属性委托](https://book.kotlincn.net/text/delegated-properties.html). Accessed 2026-11-17.  
