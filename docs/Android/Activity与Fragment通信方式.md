# Fragment相关

## Fragment的生命周期

![Fragment生命周期](../img/fragment_lifecycle.png)

## Activoty与Fragment的通信方式

1. **单向通信**

  Activity通过设置setArgument()方法向Fragment方法传值，Fragment通过getActivity()的方式调用Activity的方法。

2. **使用接口**
  Activity和Fragment分别实现接口，在Activity中获取Fragment的实例，调用接口方法，Fragment中同理；

3. **广播的方式**

  略

4. EventBus

  略

## Fragment中的坑

[Fragment全解析系列（一）：那些年踩过的坑](http://www.jianshu.com/p/d9143a92ad94)
