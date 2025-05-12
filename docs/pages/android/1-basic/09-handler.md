# 消息机制

## 基本用法

通过自定义Handler，重写handleMessage方法，根据message来处理消息。

```Java
private class MyHandler extends Handler {

    void handleMessage(Message message) {
        // 处理消息
        if (message.what == 1) {
            // ...
        }
    }
}

Handler handler = new MyHandler();
Message message = Message.obtain(hanlder, 1);
handler.sendMessage(message);
```

直接通过Handler.post(runnable)来处理消息。

```Java
Handler handle = new Handler(Looper.mainLooper());
handler.post(() -> {
    // ...
});
```

## 相关概念

Handler相关的类有4个，Handler，Looper，Message，MessageQueue. 简单来说，消息机制就是Handler发送消息，将Message放到MessageQueue中，通过Looper进行死循环，不断从MessageQueue中取Message，然后通过Message.target.dispatchMessage()处理消息。

- Looper  
Looper持有一个Thread对象和一个MessageQueue，在构造方法中会初始化MessageQueue，把当前Thread的引用指向当前线程。  
此外，Looper中还有一个静态的ThreadLocal对象保存当前线程的Looper对象，调用prepare()方法，会新建一个Looper对象，存入ThreadLocal中。调用Looper.myLooper()方法时，返回当前线程对应的Looper实例。主线程Looper.prepare()是在ActivityThread中调用的，子线程需要自己调用。
Looper中还有一个loop()方法，loop()方法中是一个死循环，不断从MessageQueue中取出消息，通过target.dispatchMessage()方法分发消息。

- Handler  
Handler持有一个Looper实例的引用，还有一个MessageQueue，MessageQueue即Looper的queue，发送消息时，最终都会走到sendMessageAtTime()将Message放入消息队列中。  
post(Runnable)方法会先执行，因为handleMessage时会先判断Callback，先执行Callback的方法。  
取消消息可以通过removeMessage(what)和removeMessage(Runnable)

- Message  
消息对象，持有Handler的引用，以及what，arg1，arg2一个Object对象，复杂的值可以放在Bundle中传递

- MessageQueue  
消息队列，实际上是一个单向链表，Message作为节点，通过Looper.myQueue()可以获得。

## 线程间通信原理

综上，每一个线程都是形成Handler-Looper-Message-MessageQueue的形式，可以说是Handler是和某个线程对应的，通过哪个线程的Handler发送消息，最终消息处理也就在哪一个线程中。

## 同步消息与异步消息

## 同步屏障

消息处理时先判断此消息是否为屏障消息，如果是屏障消息，则去循环遍历，直到寻找到异步消息为止。通过这种方式跳过了普通消息，直接执行异步消息。也就是说同步屏障为handler消息机制提供了一种优先级策略，异步消息的优先级要高于同步消息。

## IdelHandler

## native方法

Message的构造方法，。

Looper的loop方法中调用MessageQueue.next取下一条消息，调用nativePollOnce

## epoll机制

epoll是Linux内核提供的一种I/O多路复用机制，用于监听文件描述符的变化。

核心机制跟3个系统调用有关：

- epoll_create 创建epoll实例，返回fd对象
- epoll_ctl 向epoll实例注册、修改、删除需要监控的fd
- epoll_wait 阻塞等待注册注册的fd发生事件

## (黑科技)保证APP永远不会Crash

MainHandler.post一个死循环的Runnable，主动调用Lopper.loop()，并把它的异常捕获了。

*参考*  

[Android 异步消息处理机制 让你深入理解 Looper、Handler、Message三者关系](http://blog.csdn.net/lmj623565791/article/details/38377229)
[Handler原理解析，玩转同步屏障](https://juejin.cn/post/7342420969879175219?searchId=20240530235309A0B8DB497A314390ADB0)
