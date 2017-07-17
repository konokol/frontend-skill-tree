# AsyncTask原理解析

## AsyncTask使用限制

- 4.1之前，AsyncTask类必须在UI线程中加载，4.1之后，系统处理过，在ActivityThread中加载；
- AsyncTask对象必须在UI线程中创建；
- execute()方法也必须在UI线程中调用；
- onXXX方法不能手动调用；
- 不能够处理太耗时的任务；
- execute()方法只能调用一次；
- 1.6之前，任务是串行执行的，之后直到3.0是并行的，之后由改成了串行；

## AsyncTask源码解析

- AsyncTask的构造方法中初始化了一个WorkerRunnable<Params, Result>和FutureTask<Task>对象，分别是mWorker和mFuture。

 其中，mWorker实现了Callable接口，用来执行doInBackground()方法中的代码，通过Process.setThreadPriority()设置为后台执行，Worker作为FutureTask的范型参数，实际上是FutureTask对Worker进行了一次包装；

- 执行execute()方法时，会调用executeOnExecutor()方法并传入sDefaultExecutor；sDefaultExecutor是一个SerialExecutor，是AsyncTask内部的一个串行的线程池；

- 执行executeOnExecutor方法时，会把Params参数复制给mWorker对象，在把mFuture对象放入参数中的线程池中开始执行任务；

- AsyncTask内部还有一个InternalHandler，是一个单例，通过getHandler获得，它的handleMessage方法中处理MESSAGE_POST_PROGRESS和MESSAGE_POST_RESULT两种消息；

- 调用publishProgress()方法时，会通过handler发送MESSAGE_POST_PROGRESS消息，更新进度；mWorker中doInBackground方法的返回值通过handler分发到主线程中

[深入理解AsyncTask原理](http://www.cnblogs.com/absfree/p/5357678.html)
</br>
[Android源码分析—带你认识不一样的AsyncTask](http://blog.csdn.net/singwhatiwanna/article/details/17596225)
