# Java 知识点速记

## Java基础(P0)

1. Java中==和equals的区别，hashCode什么作用？  
2. Object类的equal和hashCode方法为什么需要一起重写？  
3. int和Integer的区别？缓存池  
4. Java多态的理解？  
5. Java中多态的底层实现机制是什么？  
6. String、StringBuffer、StringBuilder的区别？  
7. String为什么不可变？  
8. 什么是内部类、内部类的作用
9. 为什么Java中匿名内部类只能访问final修饰的外部变量？    
10. 抽象类和接口的区别、应用场景  
11. 泛型中extends和super的区别  
12. 静态属性、方法能否被重写  
13. final/finally/finalize的区别  
14. 什么是序列化、为什么要序列化？  
15. Serializable、Parcelable的区别？  
16. 静态内部类的设计意图？  
17. 成员内部类、静态内部类、方法内部类（局部内部类）和匿名内部类的区别和应用场景？  
18. 闭包和局部内部类的区别？  
19. String转换成Integer的方式和原理？  
20. 对象拷贝中深拷贝和浅拷贝的区别？  
21. Enumeration和Iterator的区别？  
22. 常见的编码方式有哪些？  
23. UTF-8编码一个中文占几个字节，int型占几个字节？  

## 集合框架(P0)

1. ArrayList 和 LinkedList 区别？  
2. HashMap 底层结构？  
3. HashMap 扩容机制？  
4. HashMap 为什么线程不安全？  
5. ConcurrentHashMap 如何保证线程安全？  
6. HashMap 和 HashTable 区别？  
7. HashMap 非线程安全、允许 null 键值；HashTable 线程安全、不允许 null、已过时。  
8. HashMap 和 TreeMap 区别？  
9. HashSet 实现原理？  
10. 集合框架介绍  

## 多线程与并发(P0)

1. 开启线程的几种方式  
2. 线程和进程的区别？为什么要有线程，而不仅仅有进程？  
3. run和start方法的区别  
4. 线程的生命周期  
5. 线程如何关闭或取消  
6. 什么导致线程阻塞  
7. synchronized 和 Lock 区别  
8. volatile 作用？和 synchronized 的区别  
9. ThreadLocal 原理？  
10. 线程池的核心参数？  
11. 线程池的工作原理？  
13. 线程池的拒接策略有哪些？  
14. JDK 中默认的几种线程池？  
15. ThreadPoolExecutor 如何设置核心线程数？
16. wait和sleep的区别  
17. 谈谈wait和notify关键字的理解  
18. AtomicInteger 原理？
19. CAS 缺点？
20. AQS 是什么？
21. 常见的锁，应用场景
22. ReentrantLock 公平锁和非公平锁区别？
23. CountDownLatch 和 CyclicBarrier 区别？
24. 如何控制某个方法允许并发访问线程的个数？Semaphore
25. 如何让多个线程串行执行？

## 异常、泛型(P0)、反射、注解

1. Error 和 Exception 区别？  
2. Java 中的异常体系？ 
3. 受检异常和非受检异常？  
4. try-with-resources 作用？  
5. 泛型擦除是什么？  
6. 泛型通配符 ? extends 和 ? super？  
7. 反射优缺点？  
8. 反射的原理？
9. 获取 Class 的方式？
10. 注解保留策略？

## IO (P1)
1. BIO、NIO、AIO 区别？
2. NIO 三大核心？
3. select、poll、epoll 区别？
4. 如何将一个Java对象序列化到文件中？  

## JVM (P0)

1. JVM 的内存分区?  
2. 堆和栈区别?  
3. 对象创建过程？  
5. 引用类型？
6. 垃圾回收算法？  
7. 如何判断对象可回收？  
8. 垃圾收集器有哪些？  
9. CMS 和 G1 区别？
10. 类加载机制？  
11. 双亲委派模型？  
12. 打破双亲委派场景？  
13. 内存泄漏和内存溢出区别？  
14. 常见 OOM 场景？  
15. JVM 调优参数？
16. 静态代理和动态代理的区别，什么场景使用？   

## Java 8 新特性 (P1)

1. Lambda 表达式本质？
2. 函数式接口？
3. Stream 中间操作和终端操作？
4. Optional 作用？
5. 接口默认方法作用？

## 设计模式(P1)

1. 单例模式的写法? 双重检查锁为什么加 volatile ?  
2. 工厂模式和抽象工厂区别？  
3. 代理模式应用？Spring AOP、Retrofit、动态代理  
4. 观察者模式应用？EventBus、LiveData、RxJava

## 手写代码

1. 手写单例（双重检查锁）  
2. 手写 LRU  
3. 手写生产者消费者  
4. 手写线程池核心逻辑  
5. 手写快速排序  
