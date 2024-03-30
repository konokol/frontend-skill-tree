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

*参考*
[synchhronized](https://www.pdai.tech/md/java/thread/java-thread-x-key-synchronized.html)
