## 获取源码
可以直接从SDK里提供的android.jar中读，在Android Studio中看，但是其中隐藏的方法和类是无法跳转和查看的，看起来不是很方便，粗看可以，如果想要细看，还是需要把源码下载下来，https://source.android.com/source/index.html，主要看 https://android.googlesource.com/platform/frameworks/base部分

Google提供的源码比较大，下载起来会比较慢，也可以使用清华的镜像，https://mirror.tuna.tsinghua.edu.cn/help/AOSP/


## 阅读的深度
从平时应用开发的经验来看，读到Framework层就够了，从HAL层再往下就很少用到了。

## 阅读的建议
- 写笔记，加深印象
- 多总结，多画图
- 阅读笔记避免大片的粘贴代码，避免大片文字解释
- 避免过度关注细节
- 对整体流程要有大致概念
- 带着问题和目的读

## 阅读顺序
1、应用启动流程

2、Activity的启动流程与生命周期管理

3、Window的机制

4、View的工作流程与事件体系

5、UI刷新机制

6、Fragment

7、Context

8、IPC与消息机制

9、PMS工作流程

10、IMS机制

12、Activity源码

13、Service启动与绑定

14、BroadcastReceiver发送与接收

15、ContentProvider启动流程

16、ListView与RecyclerView

17、Android虚拟机

