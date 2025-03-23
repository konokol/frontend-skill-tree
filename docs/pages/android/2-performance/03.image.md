# 图片加载

## Glide

### 图片加载流程

### 对图片的优化

## 内存泄漏的处理

- 多级缓存机制
- 

### 缓存机制

读

软引用 --> LRUCache --> DiskLRUCache --> 网络

写

DiskLruCache --> 弱引用，当引用计数器为0时


## 图片加载优化

### 图片占用的大小

size = 原图高度 * (设备的 dpi / 目录对应的 dpi ) 新图的宽度 = 原图宽度 * (设备的 dpi / 目录对应的 dpi ) * 4

### 单张图youhua

- 放在合适drawable目录下
- 图片加载框架加载
- 减少图片格式，RGB565比RGB8888占用内存更少
- 降低图片分辨率，BitmapFactory.Options.inSampleSize

#### 指标监控

- 大图监控
- 缓存命中率
- 内存占用大小
- 图片加载成功率
- 图片加载速度


## 高效加载图片

**加载缩略图**

BitmapFactory.Options解码图片，inJustDecodeBound选项，置为true的时候，解码出来的图片，只返回图片的宽高，并不把图片加载到内存中，然后调整合适的inSampleSize，缩放图片；

**缓存**

使用LruCache，根据设备可用内存，缩放后图片的大小，图片使用频率等情况设计缓存。还可以实现大图后台线程加载。



*参考*
[Android高效加载大图、多图解决方案，有效避免程序OOM](http://blog.csdn.net/guolin_blog/article/details/9316683)
https://juejin.cn/post/6987360280686624804
https://juejin.cn/post/7095565564029960206/#heading-3
