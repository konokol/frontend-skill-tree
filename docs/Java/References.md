# Java中的四种引用

## 强引用(StrongReference)
强引用是最普遍的引用，当内存不足时，即使抛出OutOfMemoryError也不会回收。
## 软引用(SoftReference)
软引用的对象，当内存充足时，就不会回收对象，当内存不足的时候，垃圾回收期就会回收它。可以用来构建内存敏感的高速缓存。
## 弱引用(WeakReference)
弱引用对象和软引用对象类似，但是当垃圾回收器扫描到弱引用时，不管内存够不够，都会回收它。
## 虚引用(PhantomReference)
虚引用对象，就和没有引用一样，垃圾回收器在随时都可以回收它。虚引用一般用来追踪对象被垃圾回收器回收的情况。

*参考*
[Java中的四种引用类型](http://www.cnblogs.com/linghu-java/p/5691804.html)
