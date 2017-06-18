# 高效加载图片

**加载缩略图**

BitmapFactory.Options解码图片，inJustDecodeBound选项，置为true的时候，解码出来的图片，只返回图片的宽高，并不把图片加载到内存中，然后调整合适的inSampleSize，缩放图片；

**缓存**

使用LruCache，根据设备可用内存，缩放后图片的大小，图片使用频率等情况设计缓存。还可以实现大图后台线程加载。

[Android高效加载大图、多图解决方案，有效避免程序OOM](http://blog.csdn.net/guolin_blog/article/details/9316683)
