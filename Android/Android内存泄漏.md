# Android内存泄漏

## 概念

Android内存泄漏是指某些对象实际已经没有了使用价值，但是还是间接或直接引用GC Roots，导致对象无法被回收，一直占用着内存空间。

## 常见的内存泄漏

1. **单例模式的不当使用**

  静态的单例模式会在应用的生命周期内一直存在，如果穿入Activity的Context对象，会导致Activity对象一直得不到释放，造成内存泄漏。

  ***解决办法：*** 单例模式必要的时候才使用，使用单例的时候，如果需要传入Context，尽量使用Application的Context.

2. **非静态内部类**

  非静态内部类会隐式持有外部类的引用，如果内部类的存活周期比较长，也会造成外部类的对象得不到释放。

  ***解决办法：*** 必要时使用静态内部类或者外部类代替

3. **Handler，Thread，Timer等**

  原理和非静态内部类的原理类似，在Activity中定义Handler，Thread，Timer等，它们会隐式持有Activity的引用，如果有延时操作，会造成Activity结束以后，内存得不到释放。

  ***解决办法：*** 使用弱引用获取Activity实例，在Activity的onDestory()方法中取消Handler的消息，关闭线程池，取消Timer.

4. **WebView造成的泄漏**

  WebView加载网页会开启异步线程，页面结束之后，线程没有结束，造成内存泄漏。

  ***解决办法：*** 1. 手动调用WebView的onStop()和onDestory()方法，在页面结束的时候，移除WebView所有的子View; 2. 使用多进程，将加载网页的Activity放在单独的进程中。

5. **资源对象未关闭**

  Cursor，IO流等对象使用完之后必须关闭，未关闭会造成内存泄漏。

  ***解决办法：*** 及时关闭资源对象。

6. **BroadCastReceiver，EventBus等没有及时解注册**

   ***解决办法：*** 适当的时候解注册。

## 检查内存泄漏的方法

1. Android Studio自带的Device Monitor观察内存状况，手动GC，dump出堆的hprof文件，分析内存状况。

2. 使用DDMS和MAT工具分析堆的状况；

3. 使用第三方工具，LeakCanary.

  **LeakCanary的原理：**

  WeakReference加ReferenceQueue，调用watch方法时，会构造一个弱引用，并指定一个ReferenceQueue，当弱引用指向的对象被回收时，将其加入ReferenceQueue，因此如果期望一个对象被回收，那么在预期的时间内，在ReferenceQueue中应该可以找到它，没找到，则表示有内存泄漏。

  *参考:*

  [Android性能优化-内存泄露的检查与处理](https://mp.weixin.qq.com/s?__biz=MzI0MjE3OTYwMg==&mid=2649547284&idx=1&sn=78b6b1e07680ae9898ff65c5ca24f8db&scene=21#wechat_redirect)</br>
  [LeakCanary 内存泄露监测原理研究](http://www.jianshu.com/p/5ee6b471970e)
