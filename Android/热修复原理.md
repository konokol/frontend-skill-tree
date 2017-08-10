# Android 热修复原理

## 1. QQ空间的方案

利用dex文件加载的先后顺序，将补丁的dex放在dexElements数组的最前面，加载dex的时候，就会先加载补丁的dex。

存在问题，当补丁中的某个类调用引用了非补丁dex中的类时，会出现问题，原因是APK安装过程中dex会被优化成odex，调用关系在同一个dex的类会被打上标记CLASS_ISVERIFIED，补丁dex中的类就会找不到要引用的类。解决方法是，定义一个AntiLazyLoad类在一个单独的dex中，在编译期，给每个类的构造方法中插入代码段（构造方法中插入是为了不加入多余的方法），引用AntiLazyLoad类，这样，每个类都不会被加上CLASS_ISVERIFIED标记。

**优点：**
- 一般补丁包较小，无须合成完整的dex文件；
- 可以实现类替换；

**缺点：**
- 重启之后才生效；
- 修复的类过多之后，造成补丁包过大；
- ART环境下，类结构的变化会造成内存错乱，必须把相关调用类以及父类子类全部加载到补丁包中，也会使补丁包过大。

## 2. Tinker的方案

打补丁包时，利用BSDiff算法（Tinker针对dex文件的结构做了调整，写了DexDiff算法）将新的dex文件与旧的作差分，得到补丁包。加载时，将补丁包与旧的dex文件合成新的dex，替换旧的dex。

**优点：**
- 不用像QQ空间一样增加dex，在类的构造方法中插入代码；
- 兼容性和稳定性比QQ空间的方案强；
- 对打包过程没有侵入；
- 补丁包小；

**缺点：**
- 需要重启之后生效；
- 合成dex文件时消耗的内存和磁盘空间都比较多，必须放在单独进程中；

## 3. 阿里的AndFix方案

通过对native层操作，替换有问题的方法。

![AndFix修复原理](http://cdn3.infoqstatic.com/statics_s2_20170810-0346/resource/articles/Android-hot-fix/zh/resources/18.jpg)

**优点：**
- 即时生效，不需要重启APP；
- 对应用无侵入；

**缺点：**
- 不能增加方法；
- 由于对native操作，需要兼容不同的cpu架构，部分机型不支持。
- 不支持对类的新增和替换。

[Android热修复技术选型——三大流派解析](http://www.infoq.com/cn/articles/Android-hot-fix)
