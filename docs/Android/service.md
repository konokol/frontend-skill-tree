# Android四大组件之Service

## 概念

Service是一种可以在后台长时间运行而不提供用户界面的组件，它可以通过其他的组件启动，当切换到其他应用之后，Service还可以在后台运行。

## 使用

- 直接继承Service或者IntentService；
- 在AndroidManifest.xml文件中声明自定义的Service；
- 组件通过context.startService()、context.startForegroundService()或者context.bindService()启动Service，区别在于startService()启动的Service生命周期与启动的组件无关，bindService()启动的Service生命周期与启动其的组件一致；
- 若通过startService()启动，会调用onStartCommand()，若通过bindService()启动，则会调用onBind()，在对应的方法中处理；
- 主动调用stopSelf()停止Service，绑定服务需要先调用context.unbindService()解绑。

***使用Tips:***

1. 调用startService()启动，如果发现service已经存在了，会直接走到onStatCommand()方法中，可以根据不同的startId来做不同的操作；
2. Android 5.0(API 21)之后，通过隐式Intent启动Service会直接抛异常；
3. 所有正在运行的Service都可以在系统设置中被看到，用户可以强杀，因此有必要在AndroidManifest.xml中声明Service时指定description，告诉用户此Service的作用；
4. 除了调用context.stopService()外，用context.startService()指定特定的startId，在Service中调用stopSelf()也可以结束Service();
5. 默认情况下Service运行在主进程，可以进行UI操作，比如可以弹Toast，更新通知栏。

## Service与线程的区别

1. Service是Android的四大组件之一，除了可以处理一般的没有界面的任务，还可以用来做跨进程通信(AIDL)，因此Service既可以运行在当前进程中，也有可能被其他的进程启动；
2. 启动Service之后，实际上是运行在主线程上的（IntentService是特殊处理，自己切换到子线程的），因此需要注意避免ANR，Service中20s还没有响应就会出现ANR；
3. Service有自己的特有生命周期，线程没有；
4. 如果run方法没执行完，线程可以在其所在的组件生命周期结束后继续存在，使用不慎会造成内存泄漏。

## 启动Service的两种方式

### startService

使用context.startService()或者context.startFrogoundService()可以启动一个Service，启动之后，Service的生命周期就和启动它的组件无关了，即使启动它的组件生命周期结束了，Service也还是存在。IntentService是自己调用stopSelf()来结束的。

Service启动之后，默认运行在主线程中，在onStartCommand()中可以根据不同的startId进行不同的操作。如果启动的是IntentService，在onHandleIntent()中进行操作。

onStartCommand()的返回值不同可以决定如何在系统结束Service之后，继续运行Service：

- START_NOT_STICKY  结束Service之后不会重建；
- START_STICKY  结束Service之后，会重建并调用onStartCommand，如果有挂起Intent，onStartCommand中会传递该Intent，否则重启时onStartCommand中的intent是空值。适用于不执行命令，等待命令来时才执行的操作，比如播放器。
- START_REDELIVER_INTENT  结束Service之后会重启，并调用onStartCommand()，传递的intent是最后一次启动Service的Intent。适用于执行任务时需要立即恢复的操作，比如文件下载，断点续传。

Service的任务处理完之后，可以通过stopSelf来结束，也可以通过context.stopService()来结束。

### bindService

context.startService()可以启动Service，启动之后，Service的生命周期和启动它的组件绑定，启动Service的组件结束后，Service也会结束。

多个组件可以绑定同一个Service，当这些组件的生命周期都结束后，被启动的Service的生命周期才会结束。

通过bindService()启动的Service，同时也可以实现onStartCommand()方法，根据返回值，在所有组件解绑之后，Service会重启。

使用bindService启动service之后，不允许再通过startService启动（todo）。

这种方式启动的Service多用于跨进程通信，或者是从Activity中启动和UI有交互。生命周期中的onBind()会返回一个IBinder，在bindService()的参数中有一个ServiceConnection接口，可以获取到这个IBinder接口，从而进行进程间的通信。

## 生命周期

![Service生命周期](../img/service_lifecycle.png)

## 几种不同的Service

### 前台Service

前台Service可以通过startService(int, Notification)启动，Service运行时，必须在状态栏显示通知，停止使用stopForground()。

如果targetSdkVersion是Android 9 (API level 28) ，启动前台Service必须在AndroidManifest文件中声明FOREGROUND_SERVICE权限，否起会抛SecurityException。

如果targetSdkVersion是Android 10(API level 29)，在前台Service中访问定位需要在AndroidManifet.xml文件的<service>标签中加上`android:foregroundServiceType="location"`，指定前台Service类型。

如果targetSdkVersion是Android 11(API level 30)，在前台Service中访问相机和麦克风，foregroundServiceType也要声明`camera`和`microphone`。

在Android 11上，前台Service有一些限制，对于从后台启动的前台Service：

- 仅当用户赋予了`ACCESS_BACKGROUND_LOCATION`权限时，Service中才能获取到定位信息；
- 访问不了相机和麦克风；

对于从前台启动的前台Service：

- 仅当用户赋予了`ACCESS_BACKGROUND_LOCATION`权限时，Service中才可以一直获取到定位信息，否则只有当APP在前台时才能获取到定位信息；
- 用户赋予了`CAMERA`权限，才可以访问相机；
- 用户赋予了`RECORD_AUDIO`权限，才可以访问麦克风；

### 后台Service

Android官网上并没定义后台Service的概念，这里的后台Service是相对前台Service的，其特点体现在：

- startService()之后，默认运行在主线程上；
- 没有用户界面，除非到设置里去看，否则用户感知不到Service的存在；

具体参考[startService](#starService)

### 绑定Service

通过bindService()启动的Service，客户端可以通过三种方式来与其通信：

1. **Binder**  

    onBind方法会返回一个Binder对象，可以扩展Bind类提供一些方法，客户端绑定之后在ServiceConnection的回掉中可以拿到Binder对象，与Service通信，也可以在ServiceConnection的回掉中通过Service对象来调用Service的public方法。多个客户端绑定同一个Service时，拿到的Binder对象和Service对象都是同一份。

2. **Messenger**  

    创建一个Handler，接受消息；

    使用Handler创建一个Messagener对象；

    在Service的onBind()方法中返回通过messagener.getBinder()返回一个Binder；

    在客户端的ServiceConnection回调中，通过service创建一个Messenger对象；

    客户端中通过Messager对象的sendMessage(msg)方法向Service发消息；

3. AIDL

    AIDL文件中定义接口，客户端访问Service时，拷贝.aidl文件，获取到Stub接口之后，可以调用到Service的方法。一般来说同一个应用中不建议使用AIDL，只有不同APP之间跨进程通信时才需要用到。

   


![已启动且允许绑定的服务的生命周期](../img/service_binding_tree_lifecycle.png)

### IntentService

&#8195;&#8195;Service在onStartCommand中，仍然是在主线程中，IntentService在onCreate方法中实例化了一个HandlerThread，在onStartCommand中通过Handler把消息post到子线程上，提供一个onHandleIntent()的抽象方法，在onHandleIntent中，实际是在子线程中处理，可以进行耗时操作，之后onHandleIntent执行完调用stopSelf()结束自己。

