# 消息机制

Handler相关的类有4个，Handler，Looper，Message，MessageQueue. 简单来说，消息机制就是Handler发送消息，将Message放到MessageQueue中，通过Looper进行死循环，不断从MessageQueue中取Message，然后通过Message.target.dispatchMessage()处理消息。

- Looper</br>
Looper中存有一个Thread对象和一个MessageQueue，在构造方法中会初始化，新建一个MessageQueue，把当前Thread的引用指向当前线程。</br>此外，Looper中还有一个静态的ThreadLocal对象，在prepare()方法中，会新建一个Looper对象，存入ThreadLocal中。</br>
Looper中还有一个loop()方法，loop()方法中是一个死循环，不断从MessageQueue中取出消息，通过target.dispatchMessage()方法分发消息。

- Handler</br>
Handler有一个Looper实例，还有一个MessageQueue，MessageQueue即Looper的queue，发送消息时，最终都会走到sendMessageAtTime()将Message放入消息队列中。</br>
post(Runnable)方法会先执行，因为handleMessage时会先判断Callback，先执行Callback的方法。</br>
取消消息可以通过removeMessage(what)和removeMessage(Runnable)

- Message</br>
消息对象，持有Handler的引用，以及what，arg1，arg2一个Object对象，复杂的值可以放在Bundle中传递


- MessageQueue</br>
消息队列，通过Looper.myQueue()可以获得
