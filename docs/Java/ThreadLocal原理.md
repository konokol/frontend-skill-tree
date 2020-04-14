# ThreadLocal原理

ThreadLocal可以创建线程私有的变量，在线程外声明，每个线程修改值只在本线程内起作用，不会被其他线程修改。

**原理**

在每个Thread中，都有一个ThreadLocalMap，在线程中给每个ThreadLocal赋值时，都会以ThreadLocal为key，将值存入到ThreadLocalMap中，这样在每个线程中取值和赋值时，取出的和修改的都是是自己的ThreadLocalMap的值，这样就确保了不会影响其他线程中的值。

**InheritableThreadLocal**

可继承的ThreadLocal值，在新建子线程时，InheritableThreadLocal的值会被传递给子线程，之后两个线程可以各自独立修改值。原因是，在线程实例化时，会检查当前父线程的InheritableThreadLocal值，会以它来构造子线程的InheritableThreadLocal。

**内存泄漏**

Thread中保存ThreadLocal值，key使用的是弱引用，如果ThreadLocal被回收了，但是线程还存活，比如使用线程池的时候，ThreadLocalMap的key就会有空值，如果一直存在就会导致内存泄漏。

ThreadLocal的get(), set(), remove()方法都会清空key为null的值，但是如果分配了ThreadLocal是静态的，或者ThreadLocal分配了值，又没调用get()等方法，就会造成泄漏。

*参考：*</br>
[深入理解ThreadLocal](http://blog.csdn.net/fishle123/article/details/48087753)</br>
[深入分析 ThreadLocal 内存泄漏问题](http://blog.xiaohansong.com/2016/08/06/ThreadLocal-memory-leak/)
