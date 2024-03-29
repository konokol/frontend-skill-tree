# 注解

## 注解的用法

### 注解的格式

```@Entry```

```@Entry(name = 'entry')```

@符号告诉编译器这是一个注解，@后面是注解的名字，注解也可以带参数，参数只有一个时，参数key可以省略。

### 可以使用注解的地方

注解可以应用在类、变量、方法、方法参数的声明中。Java 8之后，注解还可以应用在使用类型上：

- 对类实例化对象的注解  
  `new @Interned MyObject();`

- 类型转换  
  `str = (@NonNull String) strings;`

- implements语句  
   ` class UnmodifiableList<T> implements @Readonly List<@Readonly T> {  ... } `

- 异常声明  
  ` void monitorTemperature() throws @Critical TemperatureException { ... } `

### 注解类型

有的时候注解可以用来当注释用，如定义一个ClassPreamble注解：

```Java
@Documented
@interface ClassPreamble {
   String author();
   String date();
   int currentRevision() default 1;
   String lastModified() default "N/A";
   String lastModifiedBy() default "N/A";
   // Note use of array
   String[] reviewers();
}
```

使用时，将注解使用在类上：

```Java
@ClassPreamble (
   author = "John Doe",
   date = "3/17/2002",
   currentRevision = 6,
   lastModified = "4/12/2004",
   lastModifiedBy = "Jane Doe",
   // Note array notation
   reviewers = {"Alice", "Bob", "Cindy"}
)
public class Generation3List extends Generation2List {

// class code goes here

}
当自定义的注解带有```@Documented```注解时，javadoc生成的文档也会带上注解。

```

## Java预置注解

### 常见的注解

- ```@Deprecated```，表明已经被弃用了，可以用在类、方法、成员变量上；
- ```@Override```，重写父类的方法时需要加上，不过也可以不加，但是，在父类没有的方法上加上了这个注解编译就会报错；
- ```@SuppressWarnings```，用来忽略编译器的警告；
- ```@SafeVarargs```，用在构造方法或普通方法上，可以用来忽略unchecked警告；
- ```@FunctionalInterface```，Java 8才有的注解，用来表明类型是函数式接口（即只有一个方法的接口）。

### 元注解

元注解是用于声明其他注解的注解，Java中的注解一共有5个：

 ```@Retention```
  
表明注解保留策略的：

- RetentionPolicy.SOURCE – 只在编译期保留，生成class文件之后就没了；
- RetentionPolicy.CLASS – 在编译期保留，保留到class文件，运行时是获取不到这种注解的；
- RetentionPolicy.RUNTIME – 这种注解会保留到运行时，在运行时可以通过getAnnotation()方法获取到；

```@Documented```

表明用javadoc生成文档的时候该注解是否会被保留。如自定义注解@Service，如果加上了@Documented，那么有@Service注解的类，在生成docs文件时，类上的@Service就会被保留。

```@Target```

表明注解可以应用在哪些地方，可以有多个值：

- ElementType.ANNOTATION_TYPE 可以对应用在注解上
- ElementType.CONSTRUCTOR 可以应用在构造方法上
- ElementType.FIELD 可以应用在成员变量上
- ElementType.LOCAL_VARIABLE 可以应用在局部变量上
- ElementType.METHOD 可以应用在方法上
- ElementType.PACKAGE 可以应用在包上
- ElementType.PARAMETER 可以应用在方法的参数及返回值上
- ElementType.TYPE 可以应用在任何类型上

```@Inherited```

表示注解是否可以继承，如果父类有注解，子类也可以继承

```@Repeatable```

Java 8才支持的注解，表明注解可以注解多次。

## 自定义注解

```java
   @Retention(RetentionPolicy.RUNTIME)
   @Target(ElementType.METHOD)
   public @interface MyAnnotation { 
      String value() default = "a";
   }
```

**自定义注解的要点：**  

- 必须用@interface类声明注解
- 可以用元注解对自定义注解来标记注解的声明周期，作用等
- 注解的值可以是任意类型，如8种基本类型、String、Class、枚举、数组等

**自定义注解应用的场景：**

一般在AOP中用的比较多，比如登录拦截校验，通过AnnotationPcessor在编译期做切面打印日志、统计耗时等。

## 获取注解

通过反射获取，拿到Class、Method、Field后，调用`<T extends Annotation> T getAnnotation(Class<T> annotationClass);`方法，可以获取到对应的注解。

## 注解的原理

注解是一种特殊的接口，javac编译后，@annotaion声明的注解会继承接口`java.lang.annotation.Annotation`。

```java
public interface MyAnnotation extends java.lang.annotation.Annotation
```

由于注解是一种特殊的接口，所以通过getAnnotatoin获取到的注解实际是一个动态代理的类。

```java
public class $Proxy1 extends Proxy implements MyAnnotation {
   String value() { ...}
}
```

通过AnnotationParser来生成代理对象，用AnnotationInvocationHandler来处理注解的取值，注解的值都存在memberValues中，取值时以注解的方法作为key。

```java
public static Annotation annotationForMap(
   Class type, Map<String, Object> memberValues) {
     return (Annotation) Proxy.newProxyInstance(
         type.getClassLoader(), new Class[] { type },
         new AnnotationInvocationHandler(type, memberValues));
}
```

*参考*  
[The Java™ Tutorials - Annotations](https://docs.oracle.com/javase/tutorial/java/annotations/QandE/questions.html)
