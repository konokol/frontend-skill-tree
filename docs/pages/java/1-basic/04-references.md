# Java中的四种引用

## 强引用(StrongReference)

使用new关键字创建出来的对象都是强引用。

强引用是最普遍的引用，当内存不足时，即使抛出OutOfMemoryError也不会回收。

## 软引用(SoftReference)

软引用的对象，当内存充足时，就不会回收对象，当内存不足的时候，垃圾回收器就会回收它。

可以用来构建内存敏感的高速缓存，图片加载等，在内存不足时释放一些非必要的对象，节约空间。

## 弱引用(WeakReference)

弱引用对象和软引用对象类似，只要遇上GC就会被回收。弱引用被回收时，JVM会自动将其加入到该弱引用对应的ReferenceQueue中。

弱引用一般用在非关键的缓存场景，当需要立即释放对象时，用弱引用。

## 虚引用(PhantomReference)

虚引用无法直接访问到引用的对象，get()方法始终返回null。和弱引用一样，虚引用被回收时会被加入到其关联的ReferenceQueue中。

一般虚引用来感知对象被垃圾回收，实现方法是创建虚引用时，传入一个ReferenceQueue，监听到队列非空即发生了垃圾回收。
```java
public PhantomReference(T referent, ReferenceQueue<? super T> q) {
    super(referent, q);
}
```

NIO中使用了虚引用来管理堆外内存。

*参考*
[Java中的四种引用类型](http://www.cnblogs.com/linghu-java/p/5691804.html)
