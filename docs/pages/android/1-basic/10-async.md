
# 异步

## AsyncTask

### AsyncTask使用限制

- 4.1之前，AsyncTask类必须在UI线程中加载，4.1之后，系统处理过，在ActivityThread中加载；
- AsyncTask对象必须在UI线程中创建；
- execute()方法也必须在UI线程中调用；
- onXXX方法不能手动调用；
- 不能够处理太耗时的任务；
- execute()方法只能调用一次；
- 1.6之前，任务是串行执行的，之后直到3.0是并行的，之后由改成了串行；

### AsyncTask源码解析

- AsyncTask的构造方法中初始化了一个WorkerRunnable<Params, Result>和FutureTask<Task>对象，分别是mWorker和mFuture。

  其中，mWorker实现了Callable接口，用来执行doInBackground()方法中的代码，通过Process.setThreadPriority()设置为后台执行，Worker作为FutureTask的范型参数，实际上是FutureTask对Worker进行了一次包装；

- 执行execute()方法时，会调用executeOnExecutor()方法并传入sDefaultExecutor；sDefaultExecutor是一个SerialExecutor，是AsyncTask内部的一个串行的线程池；

- 执行executeOnExecutor方法时，会把Params参数复制给mWorker对象，在把mFuture对象放入参数中的线程池中开始执行任务；

- AsyncTask内部还有一个InternalHandler，是一个单例，通过getHandler获得，它的handleMessage方法中处理MESSAGE_POST_PROGRESS和MESSAGE_POST_RESULT两种消息；

- 调用publishProgress()方法时，会通过handler发送MESSAGE_POST_PROGRESS消息，更新进度；mWorker中doInBackground方法的返回值通过handler分发到主线程中


## Callable、Future和FutureTask

在Java多线程中，继承Thread和实现Runnable接口都可以实现多线程，但是没办法获取返回的结果，Future可以实现获取结果。

- Callable，接口，有一个call方法；
- Future<V>，接口，有cancel，isCanceled，isDone，get等方法；
- FutureTask<V>，实现了RunnableFuture接口，RunnableFuture接口继承了Future和Runnable接口。

Future，Callable一般和ExecutorService一起使用，ExecutorService.submit(...)方法会返回Future对象。




## HandlerThread与IntentService

**HandlerThread**

HandlerThread是Thread的子类，其中自带一个Looper，还可以设置优先级，运行run方法之前会调用Looper的prepare()方法设置线程，之后开始loop(). 在HandlerThread的run()方法中会调用onLooperPrepare()方法，在这个方法中，可以执行自定义的操作。

**IntentService**

IntentService是Service的子类，与普通Service所不同的是，在IntentService的onCreate()方法中，实例化了一个HandlerThread，然后获取它的Looper，并通过它的Looper实例化一个handler，在onStart()方法中，利用Handler发送消息，在handleMessage()中处理消息。也就是说IntentService中的操作是在子线程中完成的。

*参考*

[深入理解AsyncTask原理](http://www.cnblogs.com/absfree/p/5357678.html)  
[Android源码分析—带你认识不一样的AsyncTask](http://blog.csdn.net/singwhatiwanna/article/details/17596225)  
[Java并发编程：Callable、Future和FutureTask](http://www.cnblogs.com/dolphin0520/p/3949310.html)  
[ IntentService——Handler与Service的结合](http://blog.csdn.net/ljd2038/article/details/50922853)  
