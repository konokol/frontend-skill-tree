# 注解

## 注解的用法

### 注解的格式

```@Entry```

```@Entry(name = 'entry')```

@符号告诉编译器这是一个注解，@后面是注解的名字，注解也可以带参数，参数只有一个时，参数key可以省略。

### 可以使用注解的地方

注解可以应用在类、变量、方法、方法参数的声明中。Java 8之后，注解还可以应用在使用类型上：

- 对类实例化对象的注解
  
   :new @Interned MyObject();

- 类型转换
  
  :str = (@NonNull String) strings;

- implements语句
  
  :class UnmodifiableList<T> implements
        @Readonly List<@Readonly T> { ... }

- 异常声明
  
  : void monitorTemperature() throws
        @Critical TemperatureException { ... }

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

## 自定义注解

## Java预置注解

### 元注解

## 获取注解