# 启动优化

## 定指标

固定的几个点，application.onAttachBaseContext、application.onCreate、activity.onCreate，首屏渲染完成。

划分了几个主要阶段。

## 优化策略

### 常规优化

1、闪屏优化。增加windowBackgroud，或者用SplashScreen（Android 12以上）。替换闪屏的Activity。
2、低版本Dex加载优化。

[抖音BoostMultiDex优化实践：Android低版本上APP首次启动时间减少80%（一）](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247485522&idx=1&sn=cddfb1c64642b53ee51ca00ce3c696ca&chksm=e9d0c3b0dea74aa60f7c4266b3ff6264702b1042170f7697f1de67f26654e78abb515478a838&token=1566092111&lang=zh_CN#rd)  
[抖音BoostMultiDex优化实践：Android低版本上APP首次启动时间减少80%（二）](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247485530&idx=1&sn=c6f92a614829215d13aec273cbd1022a&chksm=e9d0c3b8dea74aaed9a458e9711d989c780a87d635e377583cc377cd3553d0a8ccbe4aeaa857&token=1566092111&lang=zh_CN#rd)

独立进程单独加载dex文件，当执行代码依赖的类不存在时，通过loading等待。

首次启动时，正常启动普通的odex，再在后台启动一个进程，单独做odex操作。通过JNI的调用查到系统加载的Dex文件，把从apk中直接解压的文件放到PathClassLoader中。

3、启动阶段耗时操作的优化
 - onCreate中布局的优化。
 - IPC的治理，非必要的结果缓存
 - IO层面，减少非必要的IO
 - CPU方面，线程管控，使用线程池

4、启动任务

核心思路
1、解决依赖关系
2、提高并行度
3、优化主线程耗时
4、动态调整任务执行顺序

- 分阶段启动
- 有向无环图

### 黑科技

### 启动任务优化

## 工具

## 治理

*参考*
https://blog.csdn.net/IT_Android/article/details/142357904?spm=1001.2014.3001.5502  
https://juejin.cn/post/6844903710020091917  
https://juejin.cn/post/6844903705028853767
https://uaxe.github.io/geektime-docs/%E5%89%8D%E7%AB%AF-%E7%A7%BB%E5%8A%A8/Android%E5%BC%80%E5%8F%91%E9%AB%98%E6%89%8B%E8%AF%BE/07%20-%20%E5%90%AF%E5%8A%A8%E4%BC%98%E5%8C%96%EF%BC%88%E4%B8%8A%EF%BC%89%EF%BC%9A%E4%BB%8E%E5%90%AF%E5%8A%A8%E8%BF%87%E7%A8%8B%E7%9C%8B%E5%90%AF%E5%8A%A8%E9%80%9F%E5%BA%A6%E4%BC%98%E5%8C%96/#_2