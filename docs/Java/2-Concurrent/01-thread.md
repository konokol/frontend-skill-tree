
# 线程

## 实现多线程线程的方法

1. 直接new Thread()，重写run方法，调用start()执行;
2. 实现Runnable接口，传入到Thread的构造方法中；
3. 实现Callable接口，包装成FutureTask，传入到Thread的构造方法中。

3种方式本质上都是通过Thread类的start方法实现的多线程。

## 线程的优先级

Java中线程优先级默认有3个，MIN_PRIORITY(1)、NORMAL_PRIORITY(5)、MAX_PRIORITY(10)，新创建线程时，优先级继承自父线程(即创建线程对象的当前线程Thread.currentThread())，默认的优先级是NORMAL_PRIORITY. 设置线程的优先级的数值必须在1~10之间，优先级更高的线程会有更大的几率被调度，但是高优先级的线程并不一定会被低优先级的线程先调度，这取决于操作系统对线程调度的实现。

Android中，设置线程优先级有2种方式：

- Thread.setPriority(int)，Java中的方法；
- Process.setThreadPiority(int)，Android原生的方法；

Process.setThreadPiority(int)是一个native方法，通过修改Linux原生线程的nice值来确定线程的优先级，取值在-20~19(Linux原生的nice值为-20~19)，数值越小优先级越高。Android中线程默认的优先级是0，和用户交互的线程优先级是-2. 

## 线程的状态

# 线程池