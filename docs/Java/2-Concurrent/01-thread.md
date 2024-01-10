
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

- NEW 新创建的线程，还未开始执行
- RUNNABLE 运行态，在Jvm中正处于运行状态，但是可能在等待操作系统中其他的资源；
- BLOCKED 阻塞状态，在等待监视器锁(monitor lock)，调用wait之后，等代码进入synchronized或者锁代码块中；
- WAITING 等待状态，等待另一个线程执行操作，调用Object.wait、Thread.join、LockSupport.park都能进入这种状态
- TIMED_WAITING 等待超时，和WAITING类似，但是有超时时间，除了带超时参数调用上面的3个方法外，调用Thread.sleep、LockSupport.parkNano、LockSupport.parkUtil也会进入这种状态
- TERMINATED 终态，运行结束

## 线程停止

推荐使用标志来标记线程结束，让线程自行执行完run方法。

调用stop()方法也可以结束线程，这种方式是通过抛出一个ThreadDeath的错误来结束线程，会使线程持有的锁全部释放，有可能造成状态不一致，出现一些异常的行为，因此不建议使用，从Java 1.2开始，这个方式被弃用了。同样和stop配合使用的suspend()和resume()方法也被弃用了。

interrupted()方法，只是给线程增加一个中断的状态，并不会真正停止线程的运行。如果线程调用了wait、join、sleep等方法，会抛出一个InterruptedException同时清空中断的标识。

# 线程池