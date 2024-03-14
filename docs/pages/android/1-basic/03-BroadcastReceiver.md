# 广播

BroadCastReceiver是Android四大组件之一，主要用于接收系统或者app发送的广播事件。广播采用了观察者模式，通过发布订阅的模式实现通信，广播的通信机制也是用Android的Binder。

## 接收广播

接受广播的方式有两种

- **清单文件注册**    

在Manifest文件中声明广播，注册intent-filter.
```xml
<receiver android:name=".MyBroadcastReceiver" android:exported="false">
    <intent-filter>
        <action android:name="APP_SPECIFIC_BROADCAST" />
    </intent-filter>
</receiver>
```

实现BroadcastReceiver，在onReceive中处理收到的广播。
```java
public class MyBroadcastReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        // ...
    }
}
```

- **通过context注册**

```Java
// 创建广播实例
BroadcastReceiver br = new MyBroadcastReceiver();
// 创建InterntFilter
IntentFilter filter = new IntentFilter(APP_SPECIFIC_BROADCAST);

// 是否导出
boolean listenToBroadcastsFromOtherApps = false;
if (listenToBroadcastsFromOtherApps) {
    receiverFlags = ContextCompat.RECEIVER_EXPORTED;
} else {
    receiverFlags = ContextCompat.RECEIVER_NOT_EXPORTED;
}
// 注册广播
ContextCompat.registerReceiver(context, br, filter, receiverFlags);

// 解注册
ContextCompat.unregisterReceiver(context);
```

## 发送广播

- **常规广播**   
context.sendBroadCastReceiver(Intent)，会向所有的接收器发送广播，顺序不固定。如果接收器跨进程了，也能收到广播。优点是效率高，缺点是接收器只能被动接受广播，无法阻止发送者发送。

- **有序广播**      
context.sendOrderedBroadcast(Intent, String)，按顺序向接收者发送广播，顺序按接收者注册的的intent-filter的`android:priority`确定。接收器可以在收到广播后继续处理将广播往下发，也可以中断广播。

- **黏性广播**    
context.sendStickyBroadcast(Intent)，黏性广播是指在发送之后，即使接收器后没有注册，也能在注册之后收到广播。接受黏性关闭需要权限`android.permission.BROADCAST_STICKY`。由于存在安全问题，黏性广播已经被废弃了。

- **本地广播**    
LocalBroadcastManager.getInstance(Context).sendBroadCastReceiver(Intent)，本地广播只能在当前进程内接受，安全性更高。

## 系统API发生的行为变更

- Android 14，APP处于后台时，会延迟收到一些不重要的广播，当恢复到前台时，会立刻收到这些延迟的广播。
- Android 9，NETWORK_STATE_CHANGED_ACTION 不再接收位置信息和个人身份数据相关的信息。
- Android 8.0，对隐式注册的广播限制，通过清单文件注册的广播接收器，大部分系统广播都无法收到。通过context注册的广播不受限制。
- Android 7，targetApi >= 24，系统不发送ACTION_NEW_PICTURE，ACTION_NEW_VIDEO广播。清单文件中注册的接收器，不能接收CONNECTIVITY_ACTION广播。

## 最佳实践

- 广播接收器的onReiceive运行在主线程上，不可以做耗时的操作，运行时间超过15s，会产生ANR。
- 广播接收器的生命周期在onReceive执行结束之后就结束了，因此不要在onReceive中执行长期存在的任务，比如开一个耗时的线程，类似的做法建议用Service。
- 收到广播后，尽量不要启动新的Activity，体验非常糟糕，可以在接收到通知后，发送通知栏通知。
- 广播操作的命名空间是全局性的，需要指定好命名空间，防止因为重名，导致其他应用接受到广播。
- 广播中不要发送隐私信息，容易被其他应用接受到，可以在发送广播时指定权限。

*参考*

[Android Developer 广播概览 ](https://developer.android.com/develop/background-work/background-tasks/broadcasts?hl=zh-cn#changes-system-broadcasts)
[理解四大组件Broadcast 发送与接收流程(基于Android10)](https://juejin.cn/post/7123570621346217992)