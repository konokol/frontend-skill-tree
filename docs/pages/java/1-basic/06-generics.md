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

Java 7之前，实例化泛型要在new关键字后面<>来声明泛型的类型，Java 8之后可以省略。

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

Java中的泛型实际是伪泛型，在编译过程中，泛型的类型都会被擦除，生成的字节码中，不会保留泛型的信息，只会有原始类的信息。

在传递类型参数时，对于无界的泛型（不论是T还是?），都会被替换成Object类型，对于有界的参数，则会被替换成边界类型。

为了保留类型安全，必要的时候会进行类型转换。

### 类型擦除与桥方法

有如下的代码：

```Java
public class Node<T> {
    protected T data;

    public Node(T data) {
        this.data = data;
    }

    public void setData(T data) {
        this.data = data;
    }
}

public class IntNode extends Node<Integer> {

    public IntNode(Integer data) {
        super(data);
    }

    @Override
    public void setData(Integer data) {
        this.data = data;
    }

}

```

在这个例子中，IntNode继承了Node，并将其泛型具化成Integer，此时问题就来了，IntNode继承Node之后，重载了setData方法，但是重载改变了setData的方法签名，由于泛型擦除父类中参数类型是Object，子类参数确变成了Integer，这显然不符合重载的规则，为了解决这种问题编译器会生成一个桥方法，如下：

```Java
public class Node {
    protected T data;

    public Node(Object data) {
        this.data = data;
    }

    public void setData(Object data) {
        this.data = data;
    }
}

public class IntNode extends Node {

    public IntNode(Integer data) {
        super(data);
    }

    // 编译器生成的桥方法，真正重载了父类的方法，同时做类型转换，调用子类的方法
    public void setData(Object data) {
        setData((Integer)data);
    }

    public void setData(Integer data) {
        this.data = data;
    }

}

```

在子类继承父类方法的实现中，真正继承父类并和setData方法签名一致的桥方法，我们在写代码时是看不到的，编译器在编译期会为我们自动处理。

基于此，在调用泛型时，如果参数和泛型规定的不一致，会产生ClassCastException，如：

```Java
IntNode intNode = new IntNode(5);
Node node = intNode;
node.set("123"); //ClassCasetException
```

### 运行时获取泛型

由于泛型的擦除，在运行时理论上是拿不到泛型的类型的，想要获取泛型的类型，必须要满足条件：

- 必须要有真实的类型，既必须能拿到class；
- 泛型的类型是明确的，如List<String>类型是明确的，List<T>是不明确的。

拿到class之后，可以通过getGenericInterfaces()和getgetGenericSuperclass()两个方法获取泛型。

getGenericInterfaces()获取到的是类实现的接口，返回结果是一个数组，即实现的接口的类型：

```Java

interface Service<T> {
}

class ServiceImpl implements Service<String> {

    public Type getType() {
        Type[] genericInterfaces = ServiceImpl.class.getGenericInterfaces();
        ParameterizedType parameterizedType = (ParameterizedType) genericInterfaces[0];
        return parameterizedType.getActualTypeArguments()[0];
    }

}

```

getgetGenericSuperclass()获取到的是父类的类型，如果泛型明确也是可以获取到泛型：

```Java

abstract Service<T> {
}

class ServiceImpl extends Service<String> {

    public Type getType() {
        Type genericSuperclass = ServiceImpl.class.getgetGenericSuperclass();
        return ((ParameterizedType) genericSuperclass).getActualTypeArguments()[0];
    }

}

```

gson中可以利用TypeToken来获取泛型，但是泛型要是明确的如：

```Java
Type type1 = new TypeToken<String>(){}.getType();//✅
Type type2 = new TypeToken<T>(){}.getType();//❌ 泛型不明确
Type type3 = new TypeToken<String>().getType();//❌ 获取不到父类
```

TypeToken是使用了和getgetGenericSuperclass()实现的获取类型，其默认构造方法中，获取父类的类型并保存下来，因此利用Token获取泛型实际是实现了一个TypeToken的匿名子类，然后在子类中获取父类的泛型，如果不带```{}```，就是直接使用TypeToken，其并无父类，因此无法获取泛型。

```Java
public class TypeToken<T> {
  final Class<? super T> rawType;
  final Type type;

    protected TypeToken() {
        this.type = getSuperclassTypeParameter(getClass());
        this.rawType = (Class<? super T>) $Gson$Types.getRawType(type);
        this.hashCode = type.hashCode();
    }
}
```

## 使用泛型的限制

- 带泛型的类实例化时，泛型不能是基础类型，要用包装类型

:

```Java
Pair<int, String> pair = new Pair(1, "123456"); //compile-time error
```

- 类型参数不能直接用new关键字实例化

:

```Java
public <T> void foo(T val) {
    T t = new T(); // compile-time error
}
```

- 静态变量不能是泛型带泛型。

:
静态变量是类级别的，是所有非静态成员变量共享的，不能

```Java
public class MobileDevice<T> {
    private static T os; // compile-time error

    // ...
}

```

- 由于泛型擦除，带类型参数时，不能类型强转也不能用instanceof来判断参数的具体类型

```Java
public static <E> void rtti(List<E> list) {
    if (list instanceof ArrayList<Integer>) {  // compile-time error
        // ...
    }
}
```

- 数组不能带泛型参数

```Java
List<Integer>[] arrayOfLists = new List<Integer>[2];  // compile-time error

```

- 异常处理时不能带泛型

:
继承Exception或Throwable的类，带泛型会编译出错

```Java
// Extends Throwable indirectly
class MathException<T> extends Exception { /* ... */ }    // compile-time error

// Extends Throwable directly
class QueueFullException<T> extends Throwable { /* ... */ // compile-time error

```

泛型方法中如果泛型是异常，不能直接catch住

```Java
public static <T extends Exception, J> void execute(List<J> jobs) {
    try {
        for (J job : jobs)
            // ...
    } catch (T e) {   // compile-time error
        // ...
    }
}
```

但是可以throw出来：

```Java
class Parser<T extends Exception> {
    public void parse(File file) throws T {     // OK
        // ...
    }
}
```

- 原始类型一样的方法，不能重载

: 类型擦除后，两个方法的签名一模一样，因此不可以重载

```Java
public class Example {
    public void print(Set<String> strSet) { }
    public void print(Set<Integer> intSet) { }
}

```

*参考*  
[The Java™ Tutorials -- Generics](https://docs.oracle.com/javase/tutorial/java/generics/wildcards.html)
