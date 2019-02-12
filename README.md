<style>
img {
    margin-left: auto; 
    margin-right:auto; 
    display:block;
}
</style>

# Android学习笔记

Android常用知识点汇总，不提供详细原理，只提供大致的思路，更详细的内容可以参考每一个知识点后链接的文章，所有文章的版权属于原作者所有，此处只提炼要点。


## Activity相关

- [Activity异常情况下的生命周期](./Android/Activity相关.md)
- 隐式Intent匹配
-  Activity的启动模式 
- 理解Activity，View，Window三者关系

这个问题真的很不好回答。所以这里先来个算是比较恰当的比喻来形容下它们的关系吧。Activity像一个工匠（控制单元），Window像窗户（承载模型），View像窗花（显示视图）LayoutInflater像剪刀，Xml配置像窗花图纸。


1. Activity构造的时候会初始化一个Window，即PhoneWindow。
2. 这个PhoneWindow有一个“ViewRoot”，这个“ViewRoot”是一个View或者说ViewGroup，是最初始的根视图。
3. “ViewRoot”通过addView方法来一个个的添加View。比如TextView，Button等
4. 这些View的事件监听，是由WindowManagerService来接受消息，并且回调Activity函数。比如onClickListener，onKeyDown等。

[Activity Window View之间的三角关系](http://www.jianshu.com/p/a533467f5af5)

[理清Activity、View及Window之间关系](http://blog.csdn.net/huachao1001/article/details/51866287) 
 
## Fragment相关

### Fragment的生命周期

<img src="https://ws1.sinaimg.cn/large/afdaace3gy1g03svynbq3j208t0nj0ui.jpg"/>

## Activoty与Fragment的通信方式

1. **单向通信**

  Activity通过设置setArgument()方法向Fragment方法传值，Fragment通过getActivity()的方式调用Activity的方法。

2. **使用接口**
  Activity和Fragment分别实现接口，在Activity中获取Fragment的实例，调用接口方法，Fragment中同理；

3. **广播的方式**

  略

4. EventBus

  略

### Fragment中的坑

[Fragment全解析系列（一）：那些年踩过的坑](http://www.jianshu.com/p/d9143a92ad94)

## Service相关


## View相关

## 虚拟机相关

### 方法64K的限制

- **64K原因**

 打包之后Java代码被编译成dex文件，通过short类型（2字节）引用dex文件中的方法，不能超过2<sup>32</sup>，即64K方法。

- **不同的运行时**

 Android 5.0之前，使用Dalvik虚拟机，使用JIT(Just-in-time)方式运行，即在运行时才编译dex字节码，而且每个apk中只支持一个dex文件。

Android 5.0之后，使用ART虚拟机，ART原生支持加载多个文件，使用AOT(Ahead-of-time)方式运行，即在应用安装的时候，将所有的dex文件编译成一个.oat文件，因此安装的时候会比较慢。

- **Mutidex应用**

 minSdkVersion < 20的应用：</br>
 1. 使用support-mutidex插件，gradle开启multiDexEnabled选项；
 2. 没有使用过自定义的Application: 自定义Application继承MutiDexApplication或者在自定义的Application中的attachBaseContext方法中安装MultiDex

 minSdkVersion > 20的应用，ART原生支持多dex加载，无需额外配置

- **局限性**

 - dex安装过程复杂，dex文件过大会ANR，应该尽量压缩和移除无用代码
 - Dalvik linearAlloc 原因，在4.0之前的设备上可能无法运行
 - Dalvik linearAlloc 可能会申请很大内存，在运行时可能会崩溃，4.0提高了分配限制，但仍然有可能出现。

- **保留某些类在主dex文件**

 应用启动过程中，某些类是必须要的，使用multiDexKeepFile使这些类保留在主dex文件中

- **主dex超过64K方法数**

 dex自动分包过程中策略很保守，主dex仍然有可能超过64K方法。</br>
 解决办法: 自定义分包过程，maindexlist，比如用dexknife

*参考:* </br>[Android Developer 配置方法数超过 64K 的应用](https://developer.android.com/studio/build/multidex.html#)</br>
[亦枫-Android 突破 DEX 文件的 64K 方法数限制](http://yifeng.studio/2016/10/26/android-64k-methods-count/)

### JVM GC算法

- ##### 标记回收算法(Mark and Sweep)

 从GC根节点开始，遍历一遍内存空间，保留可以被GC根节点直接或间接引用的对象，剩下的对象都可以被回收。遍历过程中，
需要中断进程内其他组件的执行，容易产生内存碎片。

- #### 复制(Copying)
 将内存划分为两块，每次只使用其中的一块，GC时，把存活的对象拷贝到另一块内存中，然后回收当前内存块中的所有对象。

- #### 标记压缩(Mark-Compat)
 从根节点开始，对所有可达对象做一次标记，GC时，把存活的对象压缩到内存的一边，然后清除边界之外的对象。

- #### 分代
 新建的对象都放在年轻代的内存区，年轻代的对象都很容易被回收。一个对象经过几次GC之后仍然存活，就把它放入到老生代的内存区。年轻代采用复制算法，老生代采用标记压缩算法。

 //todo to be completed


*参考*</br>
[Android GC原理探析](https://zhuanlan.zhihu.com/p/24835977)</br>
[JAVA垃圾回收机制](http://www.wxtlife.com/2016/04/25/java-jvm-gc/)


## Android多中的多线程

## 动画

## 图片加载相关

## 序列化

## 各版本新特性

### Android 5.0(Lollipop)

[Android 5.0 行为变更](https://developer.android.com/about/versions/android-5.0-changes.html?hl=zh-cn#BehaviorNotifications)

1. Android Runtime (ART)替代了Dalvik
2. 通知行为变更
   - Material Design
   - 声音和震动的设置方式变动
   - 锁定屏幕可见性，用户可以选择保护敏感信息不公开，缩减显示的文本
   - 多媒体播放，不建议使用自定义的RemoteView
   - 浮动通知
   - 媒体控件和 RemoteControlClient
3. getRecentTasks()弃用，如果您的应用使用此方法检索它自己的任务，则改用 getAppTasks() 检索该信息。

4. Android NDK 中的 64 位支持
5. 绑定到服务，Context.bindService() 方法现在需要显式 Intent
6. WebView，默认会阻止第三方Cookie和混合内容，系统现在可以智能地选择要绘制的 HTML 文档部分
7. 自定义权限唯一性要求，只有一个应用可以定义给定自定义权限，除非使用与定义权限的其他应用相同的密钥进行签名
8. TLS/SSL 默认配置变更
9. 支持托管配置文件

### Android 6.0(Mushroom)

[Android 6.0行为变更](https://developer.android.com/about/versions/marshmallow/android-6.0-changes.html)

1. 运行时权限
2. 低电耗模式和应用待机模式
3. 取消支持 Apache HTTP 客户端
4. 由OpenSSL转到BoringSSL
5. 硬件标识符访问权
6. 通知
7. 音频管理器变更
8. 文本选择
9. 浏览器书签变更
10. Android 密钥库变更
11. WLAN 和网络连接变更
12. 相机服务变更
13. 运行时
14. APK 验证
15. USB 连接
16. 指纹身份验证
17. 可采用的存储设备，动态返回文件路径

### Andorid 7.0(Nougat)
[Android 7.0 开发者版本](https://developer.android.com/about/versions/nougat/android-7.0-changes.html)

1. 电池和内存，移除了一些隐式广播
2. 权限更改，私有文件的安全性，分享私有文件内容的推荐方法是使用 FileProvider。DownloadManager 不再按文件名分享私人存储的文件。Android 框架执行的 StrictMode API 政策禁止在您的应用外部公开 file:// URI。
3. 多窗口支持
4. 配置文件指导的 JIT/AOT 编译，快速的应用安装路径
5. 随时随地低电耗模式...
6. Android 中的 ICU4J API
7. WebView，Chrome 和 WebView 配合使用，多进程，Javascript 在页面加载之前运行

### Android 8.0(Oreo)

[具透 | Android O 突然就来了，首个开发者预览版都有哪些新东西？](https://zhuanlan.zhihu.com/p/25938526)

1. 更激进的后台管理策略
2. 支持更高阶的蓝牙音频解码协议
3. 多渠道通知分类, 通知延后功能, 状态标记（应用角标）
4. XML 字体支持
5. 导航栏自定义功能

### Android 9.0(Pie)

//todo

## 常用框架原理

## 性能相关

### Android内存泄漏

#### 概念

   Android内存泄漏是指某些对象实际已经没有了使用价值，但是还是间接或直接引用GC Roots，导致对象无法被回收，一直占用着内存空间。

#### 常见的内存泄漏

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

   ***解决办法：*** 1. 手动调用WebView的onStop()和onDestroy()方法，在页面结束的时候，移除WebView所有的子View; 2. 使用多进程，将加载网页的Activity放在单独的进程中。

5. **资源对象未关闭**

   Cursor，IO流等对象使用完之后必须关闭，未关闭会造成内存泄漏。

   ***解决办法：*** 及时关闭资源对象。

6. **BroadCastReceiver，EventBus等没有及时解注册**

    ***解决办法：*** 适当的时候解注册。

#### 检查内存泄漏的方法

1. Android Studio自带的Device Monitor观察内存状况，手动GC，dump出堆的hprof文件，分析内存状况。

2. 使用DDMS和MAT工具分析堆的状况；

3. 使用第三方工具，LeakCanary.

  **LeakCanary的原理：**

  WeakReference加ReferenceQueue，调用watch方法时，会构造一个弱引用，并指定一个ReferenceQueue，当弱引用指向的对象被回收时，将其加入ReferenceQueue，因此如果期望一个对象被回收，那么在预期的时间内，在ReferenceQueue中应该可以找到它，没找到，则表示有内存泄漏。

  *参考:*

  [Android性能优化-内存泄露的检查与处理](https://mp.weixin.qq.com/s?__biz=MzI0MjE3OTYwMg==&mid=2649547284&idx=1&sn=78b6b1e07680ae9898ff65c5ca24f8db&scene=21#wechat_redirect)</br>
  [LeakCanary 内存泄露监测原理研究](http://www.jianshu.com/p/5ee6b471970e)


## 其他

### Android中对集合的优化

在Android中，为了节约内存，使用了SparseArray来代替key是Int的HashMap，除此之外，还有ArrayMap和ArraySet.

- #### SparseArray

 `SparseArray<V>`可以用来代替`HashMap<Integer,V>`，使用SparseArray可以节省内存空间，但是并不能提高查找效率。

 SparseArray内部，使用两个数组来分别存储key和value，插入时，如果如果key存在，直接覆盖，没有则新插入key和value. 查找时，先从key的数组中用二分查找找到key，然后直接根据key的index去查找value数组中的value值。删除时，还是先查找到key的index，然后把相应位置的value标记为DELETED，其中DELETED是一个Object对象，并标记可以GC。gc方法中，遍历数组，遇到有位置的元素被删除了，就把后面未删除的元素前移。

- `SparseArray<V>`     --> `Map<Integer, V>`
- `SparseIntArray`     --> `Map<Integer, Integer>`
- `SparseBooleanArray` --> `Map<Integer, Boolean>`
- `SparseLongArray`    --> `Map<Integer, Long>`

- #### ArrayMap

 ArrayMap可以用来代替`ArrayMap<K,V>`，和SparseArray类似，ArrayMap中也有两个数组，一个是int类型mHashes，专门用来存key的hash值，有序排列，另外还有一个Object类型的数组mArray，用来放真正的key和value，其中根据key的hash值算出一个index，然后，把key放在mArray[index]的位置，把value放在mArray[index + 1]的位置。

 数组扩容时，大于8个直接扩大到1.5倍，大于4个的时候，扩大到8，小于4个的时候，扩大到4个。

 此外ArrayMap中还有两个缓存，是两个静态数组，mBaseCache和mBaseTwiceCache，扩容的时候，会把原来旧的数组赋值给这两个cache，扩容重新分配内存空间的时候，会优先取两个cache。也就是说，另外在新建另外一个ArrayMap时，可以直接取缓存，不用去新申请空间，这样也就节省了空间。

 删除时，根据key的hash值找到index，如果只有一个元素，直接把两个数组赋值成空数组，如果hash数组的长度大于8且map的大小小于hash数组长度的1/3，则重新分配数组空间，否则，把相应位置的元素删了，后面的元素往前移动。
