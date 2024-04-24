# volatile

## 作用

- 保证可见性，当变量的值在一个线程更新后，另一个线程有可能从内存中读到的是更新前的值，volatile变量保证了每次从内存中读到的值都是最新的；
- 禁止重排序，在不影响程序运行结果的前提下，JVM会对指令的重排序，多线程情况下重排序可能会导致异常。volatile变量可以保证写操作一定在读操作之后完成；
- 保证原子性，32位机器上，long和double的赋值不是原子的，会分2步完成，volatile保证了赋值操作的原子性。但是当前各平台的JVM都已经把64位数据的读写设计成原子性操作了，不加volatile也不会出错。

## 应用场景

- 多线程下的标志位
- 双重校验，如单例
- CAS无锁同步的变量声明

## 实现原理

volatile的可见性是基于内存屏障(Memory Barrier)来实现的。

内存屏障是一个CPU指令。为了提升性能，编译器和CPU会对指令进行重排序，JMM为了保证在不同编译器和CPU上都有相同的执行结果，会插入特定的内存屏障的指令来禁止编译器和CPU进行进行指令重排。

JVM中volatile是通过lock指令来实现内存屏障的。为了提高处理器的速度，处理器内都带有高速缓存。当对volatile修饰的变量进行写操作时，会生成一条带有lock的指令，同时将缓存中的值写入主存中，其他CPU在总线上感知到这个写操作之后，会让缓存这个变量的值失效，当读取到这个值时，发现缓存无效，就会先从主存中先读出值放入缓存中。

volatile有序性的实现是通过happens-before来保证的，对一个volatile变量的写，happens-before于任意后续会这个变量的读。

## 参考

[volatile详解](https://www.pdai.tech/md/java/thread/java-thread-x-key-volatile.html)
[理解Java关键字volatile](https://zhuanlan.zhihu.com/p/633426082)
