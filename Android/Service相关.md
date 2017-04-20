#### IntentService与普通Service的区别
&#8195;&#8195;Service在onStartCommand中，仍然是在主线程中，IntentService在onCreate方法中实例化了一个HandlerThread，在onHandleIntent中，实际是在子线程中处理，可以进行耗时操作
