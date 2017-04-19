&#8195;&#8195;从两方面考虑，提高进程的优先级，或者在进程被杀死之后的唤醒

**进程优先级**</br>
&#8195;&#8195;前台进程 > 可见进程 > 服务进程 > 后台进程 > 空进程
![](http://ww1.sinaimg.cn/large/afdaace3ly1feseik6r4vj20go08n0ul.jpg)

**提高进程优先级的方式**</br>

1. 利用Activity，锁屏时启动一个1像素的Activity，解锁之后，结束掉；
2. Service的setForeground()，2.3之后设置的同时需要发一条通知，可以启动一个内部Service，发完通知之后，马上结束调内部Service.

**进程唤醒**

1. 监听系统的广播，开机，屏幕解锁，应用安装等；
2. 利用第三方应用的广播；
3. 利用Service激活，startComand()中返回START_STICKY，第一次5s重启，之后10s，20s，短时间被杀死5次不重启，被有Root权限的应用froceStop之后不重启；
4. 守护进程，被杀死之后互相唤醒；
5. native方法；
6. JobSchedule，仅在5.0之后有效；

**其他方式**

通过推送，Google的GCM，小米推送，华为推送，百度推送等。

[Android进程保活招式大全--腾讯Bugly](http://dev.qq.com/topic/57ac4a0ea374c75371c08ce8)
