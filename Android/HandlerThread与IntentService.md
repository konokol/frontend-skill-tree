# HandlerThread与IntentService

**HandlerThread**

HandlerThread是Thread的子类，其中自带一个Looper，还可以设置优先级，运行run方法之前会调用Looper的prepare()方法设置线程，之后开始loop(). 在HandlerThread的run()方法中会调用onLooperPrepare()方法，在这个方法中，可以执行自定义的操作。

**IntentService**

IntentService是Service的子类，与普通Service所不同的是，在IntentService的onCreate()方法中，实例化了一个HandlerThread，然后获取它的Looper，并通过它的Looper实例化一个handler，在onStart()方法中，利用Handler发送消息，在handleMessage()中处理消息。也就是说IntentService中的操作是在子线程中完成的。


[ IntentService——Handler与Service的结合](http://blog.csdn.net/ljd2038/article/details/50922853)
