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

优点：

- 反射能够使Java在运行时获取到分析类的信息，让Java具备了动态语言的特性。

缺点:

- 性能，由于动态调用，虚拟机的各种优化都不会生效，对各种类型的包装会造成内存的额外开销，因此反射比普通的API性能更差。
- 安全性，在运行时调用需要有权限，会产生权限问题以及异常
- 开放性，反射可以调用任何API，破坏了封装性，使得任意私有的API都能对外暴露。

*参考*  
[Trail: The Reflection API](https://docs.oracle.com/javase/tutorial/reflect/TOC.html)