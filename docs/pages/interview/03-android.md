# Android相关问题

## Activity相关
1. Activity启动流程  
2. onSaveInstanceState(), onRestoreInstanceState调用时机  
3. Activity的启动模式（Launch Mode）和使用场景  
4. Activity A跳转Activity B，再按返回键，生命周期执行顺序  
5. 横竖屏切换、HOME键、返回键、锁屏与解锁，跳转透明Activity，启动一个Theme为Dialog的Activity，弹出Dialog的Activity生命周期  
6. onStart和onResume, onPause和onStop的区别  
7. Activity之间传递数据的方式Intent是否有大小限制，如果传递数量偏大，有哪些方案  
8. Activity的onNewIntent方法什么时候执行  
9. 显式启动和隐式启动  
10. scheme使用场景、协议格式、如何使用  
11. ANR的四种场景  
12. onCreate和onRestoreInstance恢复数据的区别  
13. Activity间传递数据的方式  
14. 跨App启动Activity方式  
15. Activity的任务栈是什么  
16. 有哪些Activity常用的标记位Flags  
17. Activity被回收之后，onSaveInstanceState与onRestoreInstance调用流程是怎样的？  

## Service相关问题

1. Service的生命周期、两种启动方式的区别  
2. Service启动流程  
3. Service与Activity如何通信  
4. IntentService是什么，IntentService原理，应用场景及其与Service的区别  
5. Service的onStartCommand方法有几种返回值？各代表什么意思？  
6. bindService与startService混合使用的生命周期以及如何关闭？  

## BroadcastReceiver相关问题

1. 广播的分类和使用场景  
2. 广播的两种注册方式的区别  
3. 广播发送和接收的原理  
4. 本地广播和全局广播的区别  

## ContentProvider相关问题
1. 什么是ContentProvider，及其使用场景  
2. ContentProvider、ContentResolver、ContentObserver之间的关系  
3. ContentProvider的实现原理  
4. ContentProvider的优点  
5. URI是什么  

## Handler相关问题

1. Handler的实现原理  
2. 子线程中能不能直接new一个Handler，为什么主线程可以?  
3. Handler导致的内存泄漏原因以及解决方案?  
4. 一个线程可以有几个Handler，几个Looper，几个MessageQueue对象?  
5. Message对象创建方式有哪些，分别有哪些区别?   
6. Handler有哪些发送消息的方法?    
7. Handler的post与sendMessage区别和应用场景?   
8. Handler postDelay后消息队列有什么变化，假设先postDelay 10s，再postDelay 1s，怎么处理这2条消息  
9. MessageQueue是什么数据结构  
10. Handler怎么做到一个线程对应一个Looper，如何保证自由一个MessageQueue ThreadLocal在Handler机制中的作用是什么  
11. HandlerThread是什么？原理？使用场景有哪些？
12. IdleHandler使用场景  
13. 消息屏障，同步屏障机制是什么  
14. 子线程能不能更新UI  
15. 为什么Android系统不建议子线程访问UI
16. Android中为什么主线程不会因为Looper.loop死循环卡死  
17. Handler消息机制中，一个Looper是如何区分多个Handler的？当Activity有多个Handler的时候，怎么区分当前消息由哪个Handler处理？处理Message的时候如何区分哪个callback？  
18. Looper.quit/quitSafely的区别  
19. 通过Handler如何实现线程切换  
20. Handler如何与Looper关联  
21. Looper如何与Thread关联  
22. Looper.loop源码  
23. MessageQueue的enqueueMessage方法如何进行线程同步  
24. MessageQueue的next方法内部原理  
25. 子线程中是否可以用MainLooper去创建Handler，Looper和Handler是否一定处于一个线程？  
26. ANR与Handler的联系  

## View绘制相关问题

1. View绘制流程  
2. MeasureSpec是什么  
3. 子View创建MeasureSpec创建规则是什么  
4. 自定义View,wrap_content不起作用的原因  
5. 在Activity中获取某个View的宽高有几种方法  
6. 为什么onCreate获取不到View的宽高  
7. View.post和Handler.post的区别  
8. Android绘制和屏幕刷新机制的原理  
9. Choreography原理  
10. 什么是双缓冲  
11. 什么是SurfaceView，为什么使用SurfaceView  
12. View和SurfaceView的区别  
13. SufraceView为什么可以直接子线程绘制  
14. SurfaceView、TextureView、SurfaceTexture、GLSurfaceView区别  
15. getWidth和getMeasureWidth的区别  
16. invalidate和postInvalidate的区别  
17. Requestlayout、onLayout、onDraw、DrawChild的区别和联系  
18. LinearLayout、FrameLayout、RelativeLayout哪个效率高  
19. LinearLayout的绘制流程  
20. 自定义View的流程和注意事项  
21. 自定义View如何考虑机型适配  
22. 自定义控件优化方案  
23. invalidate如何局部刷新  
24. View加载流程  

## View事件分发相关问题

1. View事件分发机制
2. View的onTouchEvent、onClickListener和OnTouchListener的onTouch方法，三者的优先级  
3. onTouch和onTouchEvent的区别  
4. ACTION_CANCEL什么时候触发  
5. 事件是先到DecorView还是先到Window  
6. 点击事件被拦截，但是想传到下面的View，如何操作  
7. 如何解决View的事件冲突  
8. 在ViewGroup中的onTouchEvent中消费ACTION_DOWN事件，ACTION_UP事件是怎么传递的
9. Activity ViewGroup和View都不消费ACTION_DOWN，那么ACTION_UP事件是怎么传递的  
10. 同时对父View和子View设置点击方法，优先响应哪个  
11. requestDisallowInterceptTouchEvent的调用时机  

## Binder机制相关问题  
1. Android中进程和线程的关系和区别  
2. 为何需要进行IPC，多进程通信可能会出现什么问题  
3. Android中IPC方式有几种，各种方式优缺点  
4. 为何新增Binder来作为主要的IPC方式  
5. 什么是Binder  
6. Binder原理  
7. 使用Binder进行数据传输的具体过程  
8. Binder框架中ServiceManager的作用  
9. 什么是AIDL  
10. AIDL使用步骤  
11. AIDL支持哪些数据类型  
12. AIDL的关键类、方法和工作流程  
13. 如何优化多模块都使用AIDL的情况  
14. 使用Binder传输数据的最大限制是多少，被占满会导致什么问题  
15. Binder驱动加载过程中有哪些重要的步骤  
16. 系统服务与bindService启动的服务的区别  
17. Activity的bindService流程  
18. 不通过AIDL，手动编码来实现Binder通信  

## Window&WindowManager相关问题  

1. 什么是Window  
2. 什么是WindowManager  
3. 什么是DecorView  
4. Activity、View、Window三者之间的关系  
5. DecorView什么时候被WindowManager添加到Window中  

## AMS  
1. ActivityManagerService是什么？什么时候开始初始化？有什么作用？
2. ActivityThread是什么？ApplicationThread是什么？他们的区别是什么？
3. Instrumentation是什么？和ActivityThread是什么关系？    
4. ActivityRecord、TaskRecord、ActivityStack、ActivityStackSupervisor、ProcessRecord之间的关系  
5. ActivityManager、ActivityManagerService、ActivityManagerNative、ActivityManagerProxy的关系  

## Fragment相关问题
1. Fragment的生命周期  
2. Activity与Fragment的通信方式，Fragment之间如何进行通信  
3. 为什么使用Fragment.setArguments(Bundle)传递参数  
4. FragmentPageAdapter和FragmentStatePageAdapter区别以及使用场景  
5. Fragment懒加载  
6. ViewPage与ViewPage2区别  
7. Fragment嵌套问题

## WebView相关问题
1. 如何提高WebView的加载速度  
2. WebView与JS交互手段  
3. WebView漏洞  

## RecyclerView相关问题  

1. RecyclerView的多级缓存机制，每一级缓存具体作用是什么，分别在什么场景下会用到缓存  
2. RecyclerView的滑动回收复用机制  
3. RecyclerView的刷新回收复用机制  
4. RecyclerView为什么要预布局  
5. ListView与RecyclerView区别  
6. RecyclerView性能优化  

## 模块化&组件化  
1. 什么是模块化  
2. 什么是组件化  
3. 组件化的优点和方案  
4. 组件独立调试  
5. 组件间通信  
6. Application动态加载  

## 动画相关问题
1. 动画类型  
2. 补间动画和属性动画的区别  
3. ObjectAnimator和ValueAnimator的区别  
4. TimeInterpolator插值器和自定义插值器  
5. TypeEvaluator估值器  

## Bitmap相关问题  

1. Bitmap内存占用计算  
2. getByteCount和getAllocationByteCount的区别  
3. Bitmap的压缩方式  
4. LruCache和DiskLruCache原理  
5. 如何设计一个图片加载库  
6. 如果有一张很大的图片，如何去加载  
7. 如果把drawable-xxhdpi下的图片移动到drawable-xhdpi下，图片内存如何变化  
8. 如果hdpi、xxhdpi下都放置了图片，加载的优先级是怎样的，如果是400x800和1080x1920，加载的优先级  
9. 屏幕分辨率适配方案  

## 性能优化相关问题  
1. 内存优化  
2. 启动优化  
3. 布局优化  
4. 卡顿优化  

## 系统启动相关问题 
1. Android系统启动流程  
2. SystemServer、ServiceManager、SystemServiceManager的关系  
3. Zygote进程为什么要交给SystemServer，而是专门设计一个Zygote  
4. Zygote的IPC通信机制为什么使用socket，而不是Binder  

## App启动&App打包安装流程  

1. 应用启动流程  
2. Apk组成和Android打包流程  
3. Android的签名机制，签名如何实现，V2相比V1签名机制的改变  
4. APK安装流程  
