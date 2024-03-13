# Java异常详解

## 异常结构

![异常结构图](../../../img/java-exception.png)

Throwable是所有异常的父类。异常分为两个大类，Error和Exception。

- Error，是运行时环境出现了错误，一般由Java虚拟机抛出，发生之后一般不希望程序自己恢复过来，常见的两个是OOM和StackOverFlow.
- Exception，子类的异常是可以捕获到的，常见的两大类是IOException和RuntimeException。

异常也可以分为检查异常和非检查异常，检查异常在编码时强制要求捕获，否则编译不通过，非检查异常包括Error，RuntimeException和它们的子类，不必强制捕获，理论上都是可以避免的。

- try        -- 用于监听。将要被监听的代码(可能抛出异常的代码)放在try语句块之内，当try语句块内发生异常时，异常就被抛出。
- catch   -- 用于捕获异常。catch用来捕获try语句块中发生的异常。

- finally  -- finally语句块总是会被执行。它主要用于回收在try块里打开的物力资源(如数据库连接、网络连接和磁盘文件)。只有finally块，执行完成之后，才会回来执行try或者catch块中的return或者throw语句，如果finally中使用了return或者throw等终止方法的语句，则就不会跳回执行，直接停止。
- throw   -- 用于抛出异常。
- throws -- 用在方法签名中，用于声明该方法可能抛出的异常。

## JVM处理异常的流程

当发生异常时，应用程序会创建一个异常对象，包含了异常名称，异常描述以及发生异常时应用程序的状态，将对象传递给JVM。当JVM收到异常时，会顺着调用栈去查找是否有能处理异常的代码，如果有则将异常交给对应的代码处理。如果没有，JVM会将异常交给默认的异常处理器处理。默认的异常处理器是打印异常日志并终止应用程序。

可以通过Thread.setUncaughtExceptionHandler()来设置异常处理器。

## 异常处理的最佳实践

- finally 块中清理资源或者使用 try-with-resource 语句
- 优先捕获具体的异常，如捕获NumberFormatException而不是Exception
- 不要捕获Throwable，Throwable是异常的超类，捕获Throwable既会捕获到普通的异常，也会捕获到Error
- 尽量使用内置的异常，除非是内置的异常满足不了
- 异常处理很耗时，不要使用异常来做流程控制。创建和抛出异常会花费几毫秒的时间。

[Java提高篇-Java异常处理](http://www.cnblogs.com/Qian123/p/5715402.html)

