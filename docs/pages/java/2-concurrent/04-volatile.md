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

## 参考

[volatile详解](https://www.pdai.tech/md/java/thread/java-thread-x-key-volatile.html)
[理解Java关键字volatile](https://zhuanlan.zhihu.com/p/633426082)
