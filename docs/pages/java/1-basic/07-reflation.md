# 反射

Java中在运行时动态获取类的信息和动态调用对象方法的机制叫反射。

## 基本原理

正常的类加载机制中，创建对象时，先加载class文件到JVM内存中，在JVM中创建一个class对象，相同的类只有一个class对象。反射的原理即从class对象中读取实例的信息。

[Java反射的原理](../../../img/java-reflection.png)

## 基本使用

### 获取class的方式

 - 通过实例getClass()方法，object.getClass()
 - 通过类型，SomeClass.class
 - 通过Class.forName()传入完整类名
 - 通过classloader.load()传入完整类名

## 优缺点