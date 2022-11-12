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
Box<String> b3 = intBox; //error: 
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

## 通配符

## 泛型擦除

*参考*

1. [The Java™ Tutorials -- Generics](https://docs.oracle.com/javase/tutorial/java/generics/wildcards.html)

