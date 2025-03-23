# Fresco相关

## Fresco的优势

- 在 Android5.0 以下系统，图片不存储在 Java heap 中，而是存储在 ashmemheap 中，在图片不显示的时候，占用的内存会自动释放，降低了 OOM 的风险
- 可以实现渐进式的 JPEG 图片呈现
- 支持 gif 和 WebP 格式图片加载
- image pipeline 设计允许多方面控制图片的加载
- Drawees 设计允许多种方式处理图片的呈现

## ImagePipeline
### 加载图像流程

1. 检查内存缓存，如有，返回
2. 后台线程开始后续工作
3. 检查是否在未解码内存缓存中。如有，解码，变换，返回，然后缓存到内存缓存中。
4. 检查是否在磁盘缓存中，如果有，变换，返回。缓存到未解码缓存和内存缓存中。
5. 从网络或者本地加载。加载完成后，解码，变换，返回。存到各个缓存中。

### 缓存

#### 1. Bitmap缓存
Bitmap缓存存储Bitmap对象，这些Bitmap对象可以立刻用来显示或者用于后处理
在5.0以下系统，Bitmap缓存位于ashmem，这样Bitmap对象的创建和释放将不会引发GC，更少的GC会使你的APP运行得更加流畅。
5.0及其以上系统，相比之下，内存管理有了很大改进，所以Bitmap缓存直接位于Java的heap上。
当应用在后台运行时，该内存会被清空。
#### 2. 未解码图片的内存缓存
这个缓存存储的是原始压缩格式的图片。从该缓存取到的图片在使用之前，需要先进行解码。
如果有调整大小，旋转，或者WebP编码转换工作需要完成，这些工作会在解码之前进行。
#### 3. 磁盘缓存
和未解码的内存缓存相似，磁盘缓存存储的是未解码的原始压缩格式的图片，在使用之前同样需要经过解码等处理。
和磁盘缓存不一样，APP在后台时，内容是不会被清空的。即使关机也不会。用户可以随时用系统的设置菜单中进行清空缓存操作。

### setUri()过程源码解析

- setUri最终都是ImageRequest，DraweeController设置Bitmap；
- 设置Controller的时候，将Controller设置给DraweeHolder，从DraweeHolder中取Drawable设置给ImageView，同时开始Controller的onAttach()方法，开始异步加载图片；
- DraweeHolder中持有Hierarchy和Controller的实例，Controller的onAttach方法中submitRequest()，开始获取图片；
- 获取到图片之后，通过Hierarchy，用回调的方式调用invalidateDrawable的方式绘制ImageView.

### Glide，Picasso和Fresco比较

#### Glide与Picasso的区别
 Glide.with(context).load(url).into(imageview);
1. 优于Fresco，默认使用RGB_565，比ARGB_8888更省内存；
2. Glide缓存ImageView大小的图，Picasso缓存全尺寸的；
3. Glide支持Gif图加载
4. 自带二级缓存；

*参考*</br>
[Fresco](https://www.fresco-cn.org/docs/intro-image-pipeline.html)</br>
[Android图片加载框架比较----Glide,Picasso,Fresco](http://blog.csdn.net/hong_geek/article/details/49849339)
