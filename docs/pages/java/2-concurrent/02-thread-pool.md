# 线程池

## 使用线程池的原因

- 降低资源消耗。通过复用已存在的线程和降低线程关闭的次数来尽可能降低系统性能损耗；
- 提高响应速度。通过复用线程，省去创建线程的过程，因此整体上提升了系统的响应速度；
- 提高线程的可管理性。线程是稀缺资源，如果无限制的创建，不仅会消耗系统资源，还会降低系统的稳定性，因此，需要使用线程池来管理线程。

## 线程池的基本使用

1、使用JDK自带的线程池

```Java
ExecutorService service = Excutors.newFixedThreadPool(nThreads);
service.submit(() -> { ... });
```

2、自定义线程池

```Java
ExecutorService service = new ThreadPoolExecutor(
                                corePoolSize,
                                maximumPoolSize,
                                keepAliveTime,
                                TimeUnit.SECONDS,
                                workQueue,
                                threadFactory,
                                handler
                                );
service.submit(() -> { ... });
```

## 线程池的工作原理

### 创建线程池的核心参数

- `int corePoolSize`，核心线程数，需要大于0；
- `int maximumPoolSize`，最大线程数，需要大于0；
- `long keepAliveTime`，线程存活的时间；
- `TimeUnit unit`，时间单位，从纳秒到天，非空；
- `BlockingQueue<Runnable> workQueue`，等待队列，非空；
- `ThreadFactory threadFactory`，创建线程的工厂方法，非空；
- `RejectedExecutionHandler handler`，执行拒绝策略时的处理器，非空。

### 各参数意义

- corePoolSize  
  向线程池中提交一个线程时，如果线程池中已有线程的数小于corePoolSize，即使存在空闲的线程，也会创建新的线程，创建新的线程使用的是threadFactory.newThread()来创建。如果线程数已经超过corePoolSize，看是否有空闲的线程，存在空闲的线程，则用空闲线程执行任务，如果没有，则根据maximumPoolSize来决定是否创建线程。
- maximumPoolSize   
  提交任务时，如果线程池中线程数量超过corePoolSize，且没有空闲的线程，检查线程数量是否超过了maximumPoolSize，超过了则会执行拒绝策略，交由handle处理，没超过最大线程数，将线程放入等待队列。如workQueue为无界队列，这个参数会被忽略。
- workQueue     
  等待队列，工作线程超过corePoolSize后，会被放入等待队列。
- threadFactory 
  创建线程的工厂方法，可以指定线程的分组，线程优先级，线程名等。
- rejectedExecutionHandler  
  提交的线程数量超过了最大线程数，交给rejectedExecutionHandler处理，参数包括Runnable和executor。JDK中默认内置了4种处理策略：  
    - ThreadPoolExecutor.AbortPolicy，拒绝执行任务，并抛出RejectedExecutionException异常；
    - ThreadPoolExecutor.DiscardPolicy，丢弃任务，什么也不做；
    - ThreadPoolExecutor.DiscardOldestPolicy，丢弃排队最久的任务，重试执行，如果线程池已经关闭，直接丢弃任务；
    - ThreadPoolExecutor.CallerRunsPolicy，由调用者所在的线程执行该任务，如果线程池已经关闭了，直接丢弃任务；

## JDK常用的线程池

Excutors中有几个静态方法newXXXPool，用来创建线程池:

|   线程池方法                     | corePoolSize | maximumPoolSize   |   workQueue      | keepAliveTime | rejectedExecutionHandler  | 
| :------------------------------| :            | :                 | :----------------| :             |:-------------------------- |
|newCachedThreadPool             |      0       | Integer.MAX_VALUE | SynchronousQueue |      60s      |   AbortPolicy              |
|newSingleThreadScheduledExecutor|      1       | Integer.MAX_VALUE | DelayedWorkQueue |     10min     |   AbortPolicy              |
|newScheduledThreadPool          |     参数传入  | Integer.MAX_VALUE | DelayedWorkQueue |     10min     |   AbortPolicy              |
|newSingleThreadExecutor         |      1       | 1                 | LinkedBlockingQueue |     0min   |   AbortPolicy             |
|newFixedThreadPool              |     参数传入   | 参数传入           | LinkedBlockingQueue |     0min   |   AbortPolicy             |
 
- **newCachedThreadPool** 该线程池无限大，只要不存在空闲线程，可以一直创建新线程。
- **newSingleThreadScheduledExecutor**，只有一个线程，周期性执行任务。
- **newScheduledThreadPool**，周期性执行任务，核心线程数可以通过参数指定。
- **newSingleThreadExecutor**，单线程的线程池，所有任务都是串行执行。
- **newFixedThreadPool**，大小固定，即限定最大并发数，超过这个数量，会排队执行。

## 线程池参数配置最佳实践

CPU密集型任务，限制线程的数量，一般设置为CPU的核数；    
IO密集型，由于IO的速度远低于CPU速度，可以多配置线程，提升CPU的利用率。


*参考*  
[java线程池使用最全详解](https://blog.csdn.net/qq_40093255/article/details/116990431)