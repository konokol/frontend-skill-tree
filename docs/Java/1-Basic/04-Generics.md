# 泛型

泛型是JDK 1.5引入的特性，使用泛型可以使得在定义类、接口以及方法的时候，将“类型”作为参数传递，从而可以实现代码的复用。

## 使用泛型的原因

- 编译期类型检查
- 省略类型转换的代码
- 复用代码

## 泛型的使用

泛型可以应用在类、接口和方法上，通过<T, R>声明类型，声明了泛型类型之后，在编译期对对涉及到泛型的参数进行类型检查，在使用泛型的参数时也不必进行类型的转换。

### 泛型类型(类和接口)

**泛型类型的使用**

泛型类和泛型接口声明的格式：

```Java
class name<T1, T2, ..., Tn> { /* ... */ }
```
这里的T可以是除基本类型的任意的类型，不过一般不用Object，因为Object和没加泛型的效果是一样的。

泛型参数一般的命名格式为大小的单个字母，不过这并不是强制要求，写成其他的也不会编译报错。一些约定俗称的简称如下：

- E - 元素，一般在集合相关的类中用
- K - Key
- N - Number
- T - Type
- V - Value
- S,U,V 等等. - 第2、3、4个泛型

一个类上可以声明多个泛型，用,分开，泛型中也可以包含泛型，比如：

```Java
Pair<Integer, List<Interger>> paier = new Pair<>(i, list);
```

**实例化泛型**

```Java
//Java 7
Box<Integer> box1 = new Box<Integer>();
// Java 8
Box<Integer> box2 = new Box<>();
```

Java 7之前，实例化泛型要在new关键字后面<>也声明泛型的类型，Java 8之后可以省略。

**原始类型**

类上带有泛型时，不带泛型的类称为原始类型，比如上面的Box就是原始类型。

实例化泛型对象时，泛型类的实例可以赋值给原始类，但是反过来就会有一个unchecked警告，因为编译器没有足够的信息推断出泛型的类型。

```Java
Box<Integer> intBox = new Box<>();
Box rawBox = new Box();

Box b1 = intBox; //OK
Box<Integer> b2 = rawBox; //warning: unchecked conversion
Box<String> b3 = intBox; //error: incompatable type found
```
对于unchecked类型的警告，可以通过在当前语句、方法、类上加注解 @SuppressWarnings("unchecked")消除，也可以在javac命令的参数中加上-Xlint:unchecked消除警告。

### 泛型方法

泛型方法的类型的声明一般放在返回值的前面，方法的返回值、参数都可以是泛型。

```Java
public static <T, R> R func(T param1, Integer param2) {
    // ...

    R r = ...
    return r;
}

```

## 泛型的边界

泛型边界分为上界和下界，分别用extends和super表示。

**上界**

```<T extends Number>```，表示使用泛型时的类型只能是Number或其子类。这里的extends不是代表继承的意思，泛型的上界可以是接口，如```<T extends Consumer>```表示泛型的类型必须要实现Consumer接口。

**下界**

```<T super Integer>```，表示使用泛型时的类型只能是Interger的超类，比如可以是Number，或者Objective。

**多个上界**

```<T extends A & B & C>```，表示类型必须是A的子类并实现B、C接口，由于Java不支持多继承，A、B、C实际上至多有一个是类其他的必须是接口，如下代码会编译失败:

```Java
class G<T extends Number & String> {} //compile error: Interface expected here
```

特殊要求，当泛型有多个上界时，如果有类，通过&连接时，必须将类放在最前面，否则会编译失败，比如上面的例子，如果有类，则只能A是类，其他的只能是接口。

```Java
class G<T extends Comparable & Number>{} //compile error: Interface expected here
```

## 类型推断

Java编译器可以根据类型声明以调用的上下文来推断具体的类型，比如官网上的例子：

```Java
static <T> T pick(T a1, T a2) { return a2; }
Serializable s = pick("d", new ArrayList<String>());
```

pick方法中的调用中，传入参数分别是String和ArrayList<String>，而方法声明中两个参数的泛型类型是一样的，因此这里的泛型T就应该是String和ArrayList<String>，即Serializable，如果两个参数没有公共的父类，则编译会失败。

## 通配符

泛型中的通配符用?表示，在使用通配符时，一般与extends和super一起使用，也可以单独使用。

**上界通配符**

```<? extends Foo>```，表示可以泛型是Foo的任意子类(如果Foo是接口，表示任意实现了Foo接口的类)。

有一种说法是，上界通配符时读安全的，例如，对于集合```List<? extends Foo> list```，从中读出来的元素赋值给Foo是安全的，可以放心的做类型转换。

```<? extends Foo>```与```<T extends Foo>```都涉及到泛型的上界，其区别是带通配符的泛型，其上界有限，下界无限，意味着泛型可以接收很多种符合上界条件的类型的赋值，但是不带通配符的泛型，其类型是唯一确定的，只能是T，可以接收的类型也是唯一的。

**下界通配符**

```<? super Foo>```，和上界通配符类似，下界通配符表示泛型是Foo的父类的任意类型。

类似的。下界通配符是写安全的，比如，对于集合```List<? super Foo>```，将Foo类型的数据插入到集合中是安全的。

**无限定通配符**

?单独使用的时候就是无限定通配符，表示泛型的类型不确定。

无限定通配符虽然表示类型不确定，但他并不表示是没有泛型，它对类型还是有约束的，例如：

```Java
List list1 = new ArrayList<A>();
List<?> list2 = new ArrayList<A>();
List<A> list3 = new ArrayList<A>();
```
list2、list3、list4都可以赋值给list1，因为list1没有声明泛型，是原始类型。

list3不能赋值给list2，尽管list2中泛型类型是不确定的，但是它还是有泛型的，只不过其泛型我们不知道是什么，有可能是A，也可能是B、C、D等其它类型，因此将```List<A>```类型的变量直接赋值给

**?与T的区别**

- T表示的泛型类型是唯一确定的，?表示泛型的类型是不确定的，其范围更广
- T可以作为函数的参数，?不行
- 作为类型使用时，T作用类似于class，可以声明一个T类型的变量，？就不行

**泛型捕获**

某些场景下，编译器推断出通配符类型，如List<?>，但当判断表达式的时候，又推断出具体的类型，这种现象叫泛型捕获，此时会产生编译异常。例如：

```Java
void foo(List<?> list) {
    list.set(0, list.get(0));
}
```
这段代码会产生泛型捕获的编译错误，原因是编译器将方法参数list处理成Object类型，但在调用list.set(int, E)时，又无法推断出E的类型。为了解决这个问题，一般可以重新定义一个Helper方法，如：

```Java
void foo(List<?> list) {
    fooHelper(list);
}

void <T> fooHelper(List<T> list) {
    list.set(0, list.get(0));
}
```

## 泛型擦除

*参考*

1. [The Java™ Tutorials -- Generics](https://docs.oracle.com/javase/tutorial/java/generics/wildcards.html)