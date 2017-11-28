# Java 8函数式编程–––Lambda表达式

## 1. 介绍
### 1.1 匿名内部类

设计匿名内部类的目的，是为了方便开发者将代码作为数据传递。举个栗子，在Android中，为一个按钮设置一个点击事件的监听器：

```java
button.setOnClickListener(new View.OnClickListener() {
     public void onClick(View view) {
          Log.v(TAG, "button is clicked!");
     }
});
```

### 1.2 Lambda表达式

Lambda表达式的作用和匿名内部类相似，也是为了将代码作为数据来传递，从某种意义上讲，Lambda表达式也可以理解为匿名函数，在其他的一些语言中则把称为闭包，实际上意义都差不多的。上面的例子，用Lambda表达式来改写，可以表示为：

```java
button.setOnClickListener(view -> Log.v(TAG, "button is clicked!"));
```

和使用匿名内部类传入实现了某个接口的对象不同，Lambda传入的参数是一段代码快，即匿名函数(注意这里已经不在叫方法而叫函数了)。这个匿名函数中，->将参数和Lambda表达式的主体分开，view是函数的参数，Log.v(TAG, "button is clicked!")是这个函数的具体实现。

![lambda表达式形式](../image/lambda.png)

lambda表达式语法：

```java
(parameters) -> expression
```
或者

```java
(parameters) -> {statemens;}
```

Lambda表达式中，参数的类型不需要显式指明，因为javac会根据程序的上下文来推断出参数的类型，这一点和kotlin很相似。

几个Lambda表达式的例子：

1、没有参数

```java
Runnable runnable = () -> Log.v(TAG, "run");
``` 
2、一个参数

```java
View.OnClickListener listener = view -> Log.v(TAG, "onClick");
```

3、一个参数包含代码块

```java
Runnable runnable = () -> {
     Log.v(TAG, "run first step");
     Log.v(TAG, "run second step");   
}
```

4、多个参数,不指定参数类型

```java
Callback<String> callback = (arg1, arg2) -> arg1 + arg2;
```

5、多个参数指定类型

```java
Callback<String> callback = (String str1, String str2) -> str1 + str2;
```

Lambda表达式的参数类型虽然可以由编译器推断出来, 但是在某些情况下, 也可能会推断不出来, 这时候就需要显式声明参数的类型了.

### 1.3 引用值而非变量

在匿名内部类中，如果需要引用外部的局部变量，则必须将这个变量设置成final类型，比如

```java
final String name = getUserName();
button.setOnClickListener(new View.OnClickListener() {
     public void onClick() {
          Toast.make(context, "hi, " + name, Toast.LENGTH_LONG).show();
     }
});
```

为什么匿名内部类访问局部变量必须是final类型的呢？简单来说，是为了保证数值的一致性。局部变量和匿名内部类的生命周期是不一样的，如果匿名内部类直接使用局部变量的引用并修改其值，则有可能造成内外值不一致的情况，所以Java规定了匿名内部类只能引用final类型的局部变量，这样一来，值不会被真正改变，匿名内部类中，也就保证了值的一致性。

在Java 8中，放松了这一限制，可以引用非final类型的变量，然而，该变量在既成事实上也必须是final类型的。

在Lambda表达式中，实际上也只能使用final类型的局部变量，即便不加final关键字，这个变量也还是final类型的。如果试图给Lambda表达式中使用一个非final类型的变量，编译器将会报错。

```java
//这段代码不能通过编译
String name = getFirstName();
name = "Mr. " + name;
button.setOnClickListener(view -> Toast.make(context, "Hi, " + name, Toast.LENGTH_LONG).show());
```

## 2 Lambda表达式的应用
### 2.1 函数式接口

**函数接口（Functional Interface）**是只有一个抽象方法的接口。例如：

```java
public interface Comparator<T> {
	int compare(T o1, T o2);
}
```
及

```java
public interface Runnable {
	void run();
}
```
*注意：Java 8中，接口可以有默认方法，即便一个接口定义了多个默认方法，只要它的抽象方法只有一个，它仍然是一个函数式接口。*

Lambda表达式与函数式接口有什么关系呢？引用书中的一句话：
> Lambda表达式允许你直接以内联的形式为函数式接口的抽象方法提供实现，并把整个表达式作为函数式接口的实例（具体来说，是函数式接口一个具体实现的实例）。

通俗一点来讲，Lambda表达式为函数式接口提供了具体的实现，从而来实现Java方法的传递（或者说是代码块传递）。当然，匿名内部类也可以实现同样的功能，只不过使用匿名内部类使用起来非常笨拙。

@FunctionalInterface注解用于表示一个接口被设计为了函数式接口。如果自定义的接口加了这个注解，但确不是函数式接口，IDE会在编译时报错，“Multiple non-overriding abstract methods found in interface Foo”，意思是Foo这个接口中有多个抽象方法。

对于函数式接口的设计，@FunctionalInterface并非是必须的，但是加上它是一个好习惯。

### 2.2 函数描述符

函数式接口中抽象方法的签名基本上也就是Lambda表达式的签名，我们把这种抽象方法叫做函数描述符。

比如Runnable接口可以看作是一个什么也不接收，什么也不返回的方法的签名，它的run()方法不接收任何参数，最终返回void.

Lambda和函数式接口的方法签名的一种记法：

```java
() -> void
```
这里表示的是Runnable接口所代表的方法。

到此为止，关于Lambda表达式，我们需要记住的是：

**1. Lambda表达式可以赋值给一个变量；**</br>
**2. Lambda表达式可以传递给一个接收函数式接口的方法。**

**例子：**
Lambda表达式的有效使用方式：

(1) Lambda表达式传给一个接收函数式接口的方法

```java
execute(() -> {});

public void execute(Runnable r){
	r.run(); 
}
```
这里的Lambda表达式的签名是```() -> void```，这是Runnable接口所代表的方法。

(2) Lambda表达式作为返回值

```java
public Callable<String> fetch() {
 	return () -> "Tricky example ;-)";
}

interface Callable<T> {
	T call();
}
```
fetch()方法返回一个Callable<String>对象，Callable<String>所代表的方法是```() -> String```，这和例中所用的签名是一致的。

(3) 一种错误的用法

```java
Predicate<Apple> p = (Apple a) -> a.getWeight();

interface Predicate<T> {
	boolean test(T t);
}
```
例中Lambda表达式的签名是```(Apple) -> Double```，Predicate<Apple>所代表的方法是```(Apple) -> boolean```，不一致。


### 2.3 函数式接口的使用

上面介绍了函数式接口和函数描述符的概念，为了应用不同的Lambda表达式，就需要一套能够描述常见函数描述符的函数式接口。Java 8的java.util.function包中为我们引入了很多函数式接口。几个典型的函数式接口如下：

#### 2.3.1 Predicate

```java
@FunctionalInterface
public interface Predicate<T>{
	boolean test(T t);
	...
}

```

涉及到返回值是boolean类型的表达式时，可以用Predicate<T>，例如：

```java
Predicate<String> p = (s) -> !s.isTempty();
```

#### 2.3.2 Consumer

```java
@FunctionalInterface
public interface Consumer<T>{
	void accept(T t);
	...
}
```
需要对一个对象进行访问可以用Consumer<T>，例如：

```java
//定义一个forEach方法
public void <T> forEach(List<T> list, Consumer<T> consumer) {
	for (Integer i : list) {
		consumer.consume(i);
	}
}

//使用
forEach(Arrays.asList(1,2,3,4,5), (Integer i) -> System.out.print(i));
```
2.3.3 Function

```java
@FunctionalInterface
public interface Function<T, R>{
	R apply(T t);
	...
}
```

创建映射关系或者从一个对象中提取信息可以用Function<T, R>。



## 3 类型检查与类型推断

上面提到，Lambda表达式为函数式接口提供了实现，但是Lambda表达式本身并不包含实现了哪个函数式接口的任何信息，所以需要了解Lambda表达式的实际类型。

### 3.1 类型检查

Lambda表达式需要的类型称为**目标类型**。只要函数签名一致，Lambda表达式可以与很多函数式接口相关联。

一张图说明类型检查的过程：

```java
List<Apple> heavierThan150g = filter(inventory, (Apple a) -> a.getWeight() > 150);
```

![type check](../image/type_check.png)

### 3.2 类型推断

类型推断是Java 7引入的概念，<>操作符可使编译器在编译时根据上下文推断出参数类型。

```java
HashMap<String, Integer> map = new HashMap<>();
```
这里，声明map时，已经明确指定了范型的类型，所以在new出HashMap对象时，编译器已经知道HashMap的具体范型。

Java 8中，Lambda表达式可以省略所有参数的类型。因为函数描述符可以通过目标类型来得到，所以Java编译器就可以通过上下文信息来推断出正确的参数类型，从而确定使用什么函数式接口来配合Lambda表达式。

当然，Lambda表达式也可以不省略参数类型，显式指定。至于这两种方式哪一种更好呢，则取决于不同的场景，有时候省略参数类型代码更易读，有的时候显式指明参数类型则比较好。

## 4 方法引用

### 4.1 方法引用简介

既然Lambda表达式可以与函数式接口相关联，作为函数式接口的函数描述符的引用，那么一个对象的方法有没有类似的表示方法呢？答案是有的，Java 8提供了方法引用(Method Referen)的表示方法。（在C语言或者是其他一些编程语言中，也有类似的概念，比如，C语言中的指向函数的指针，Python中把一个函数赋值给变量）

方法引用可以重复使用现有的方法定义，并像Lambda表达式一样传递它们。

方法引用通过一个::来表示，需要使用方法引用时，目标引用放在分隔符::前，方法名放在后面。

一些例子：

| Lambda | 方法引用 |
|----|----|
| () -> Thread.currentThread().dumpStack() | Thread.currentThread()::dumpStack |
| (str, i) -> str.substring(i) | String::substring |
| (String s) -> System.out.print(s) | System.out::print|

### 4.2 构建方法引用

#### 4.2.1 方法引用主要分为3类：

1. 指向静态方法引用

	例如Integer.parseInt()方法，写作Integer::parseInt
	
2. 指向任意类型方法实例的方法引用

	如String中的length方法，写作String::length

3. 指向已有对象的实例方法的方法引用

	比如有一个Student的实例stu，有一个方法是getName，就可以写成stu::getName
	
**区别：**

静态方法引用是直接引用类的静态方法，通过 "类名::方法名"的方式引用；

第二种方法引用中，引用了一个对象的方法，但是这个对象本身是Lambda表达式的一个参数，不如上面的例子中，对应的Lambda表达式是(String s) -> s.length()；

第三种中，是在Lambda表达式中调用一个已经存在的对象的方法，上面的例子改写成Lambda表达式就是() -> stu.getName()，和第二种的区别就是调用的对象的方法不是Lambda的参数。

#### 4.1.2 构造方法引用

对于一个现有的构造方法，可以利用它的名称和关键字new来创建一个方法引用：ClassName::new.

它的功能和静态方法的引用类似，比如有一个无参构造方法，适合Supplier的签名，() -> Apple，那么可以这样写：

```Java
Supplier<Apple> constuctor = Apple::new;
Apple apple = constructor.get();
```

它等价于Lambda表达式的写法：

```Java
Supplier<Apple> constuctor = () -> new Apple();
Apple apple = constructor.get();
```

## 5 实践

有一些菜品，存在```List<Dish> dishes```中，现在要将它们按照价格升序排序。

1. 在Java 8之前

	Java 8之前，List没有sort方法，需要借助Collection类。

	```Java
	public class DishComparator implements Comparator<Dish> {
		public int compare(Dish d1, Dish d2) {
			return d1.getPrice() - d2.getPrice();
		}
	}
	Collection.sort(list, new DishComparator());
	```

2. Java 8中，使用来排序list

	Java 8之前，List没有sort方法，需要借助Collection类。

	```Java
	public class DishComparator implements Comparator<Dish> {
		public int compare(Dish d1, Dish d2) {
			return d1.getPrice() - d2.getPrice();
		}
	}
	list.sort(new DishComparator());
	```

3. 使用匿名内部类

	```Java
	list.sort(new Comparator<Dish> {
		public int compare(Dish d1, Dish d2) {
			return d1.getPrice() - d2.getPrice();
		}
	});
	```

4. 使用Lambda表达式

	```Java
	list.sort((Dish d1, Dish d2) -> d1.getPrice() - d2.getPrice());
	```

5. 使用方法引用

	```Java
	list.sort(Comparator.comparating(Dish::getPrice))
	```

## 6 小结

- **Lambda表达式**可以理解为一种匿名函数：没有名称，但有参数列表、函数主体、返回值；
- Lambda表达式可以让你更简洁的传递代码；
- **函数式接口**就是仅仅声明了一个抽象方法的接口；
- 只有在接收函数式接口的地方才可以使用Lambda表达式；
- Lambda表达式允许你直接内联，为函数式接口的抽象方法提供实现，并且将整个表达式作为函数式接口的的一个实例；
- Java 8自带一些常用的函数式接口，在java.util.function包里，包括Predicate<T>、Function<T,R>、Supplier<T>、Consumer<T>等；
- Lambda表达式所需要的代表的类型成为目标类型；
- 方法引用让你重复使用现有的方法实现并直接传递它们；
- Comparator、Predicate、和Function等函数式接口有几个可以结合Lambda表达式的默认方法。

--

作者：Ivan J. Lee</br>
时间：2017-11-28 00:40



