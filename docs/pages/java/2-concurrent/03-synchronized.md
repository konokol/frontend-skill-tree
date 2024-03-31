# Synchronized详解

## 基本使用

1、**对象锁**

使用在普通方法上，锁的对象时当前的实例，即this。

```Java
class Instance {
    public synchronized void foo() { ... }
}
```

在代码块中使用，锁的对象可以是当前实例，也可以是自定义的其他对象。

```Java
class Instance {
    private Object lock = new Object();

    public void foo() { 
        // 方式一 使用当前对象
        synchronized(this) {
            ...
        }
        // 方式二 使用自定义对象
        synchronized(lock) {
            ...
        }
    }
}
```

2、**类锁**

使用在静态方法上或者锁定的对象是Class对象。

```Java
class Instance {

    // 锁定静态方法
    public synchronized static void foo() { ... }

    public void foo1() {
        synchronized(Instance.class) { ... }
    }
}
```

## 原理

synchronized作用在代码块上和方法上，底层的原理不一样。

作用在方法上时，是通过Monitor来实现的，每一个对象都有一个monitor，当一个monitor被持有后，对象即处于锁定状态。synchronized代码块中，在字节码前后分别会插入一个monitorenter和monitorexit。

当线程进入monitorenter时，会尝试获取monitor的所有权，过程如下：

1、当monitor的计数为0，则当前线程进入monitor，同时计数加1，即该线程持有了monitor；  
2、如果当前线程已经持有的monitor，重新进入monitor，计数也加1；  
3、如果其他线程已经持有了monitor，则线程进入阻塞状态，直至monitor的计数变为0，再尝试重新获取monitor。

monitorexit：执行monitorexit的线程必须是持有monitorenter的线程，当进入monitorexit时，monitor的计数减1，如果减1后变成了0，则当前线程退出monitor，其他的线程可以尝试进入monitor。

作用在方法上时，在方法常量池中会有一个ACC_SYNCHRONIZED，表明该方法是一个同步方法。当JVM调用到该方法时，会先尝试获取monitor，获取成功之后才可以执行该方法，执行结束之后释放monitor。在同步方法执行期间，其他任何方法都无法获取monitor。

## JVM对synchronized的优化

*参考*
[synchhronized](https://www.pdai.tech/md/java/thread/java-thread-x-key-synchronized.html)
