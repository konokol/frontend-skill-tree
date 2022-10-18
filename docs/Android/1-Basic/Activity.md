<!-- Activity -->

# Android四大组件--Activity

## 基本概念

Activity是Android的四大组件之一，也是唯一可以和用户直接交互的组件，它承载着和用户交互的界面，每个Activity都附着在一个全屏或者非全屏的窗口上。Activity充当了应用于用户的入口点，用户与应用交互时，都是直接和Activity打交道。

传统桌面的应用与用户互动往往是通过唯一的入口，移动端交互则不同，从一个应用中，可以很容易进到另一个应用的任何一个页面而无需启动整个应用，这个打开的页面就是一个单独的Activity。

一个应用中可以有多个Activity，这些Activity都需要在AndroidManifest文件中注册，多个Activity协同工作共同完成和用户的交互，但是不同的Activity之间也具有极弱的关联关系。不同的Activity通过Intent交互，从一个Activity启动另一个Activity，只需要通过Intent传入类名即可，甚至隐式启动Activity时，类名也不需要。

## 生命周期

### 正常生命周期

![Activity生命周期](../../img/activity_lifecycle.png)

- **onCreate**

  : onCreate是生命周期的第一个方法，每个Activity对象只会调用一次onCreate，一般会在onCreate中做一些初始化相关的工作。

  : onCreate参数中有一个Bundle参数，如果Activity是被销毁重建的，则Bundle中会存有一些上次被销毁时的数据，重建时可以利用这些数据做一些恢复工作。

- **onStart**

  : onStart是用户即将进入前台时调用的方法，此时Activity已经对用户可见了，但是还不能交互。onStart会快速的走完，接着马上走onResume，Activity不会一直停在onStart不动，因此不可以在onStart中做特别耗时的操作。

- **onResume**

  : 走到onResume时，Activity才真正的完全处于前台，此时用户就可以和应用交互了，如果用户一直不交互，Activity会一直停留在onResume的状态。
  
  : 值得注意的是，Android 7.0之后，在多窗口模式下，只有获取到焦点的Activity才是onResume的状态，所以即使当前的Activity是完全可见的，没有焦点时也处于onPause状态。但是在一些折叠屏手机上，会有多个Activity都处于onResume的状态，只是其中只有一个Activity有焦点。

- **onPause**

  : onPause标志着Activity进入了后台，和onStart一样，此时也不能和用户交互。在onPause中一般用来做一些轻量级资源回收工作，比如释放系统资源，释放传感器资源等。

  : 如果启动另一个Activity，onPause执行完了之后才会执行下个Activity的onResume，所以一般也不应该在onPause中执行特别耗时的操作。

  : 和onStart稍有区别的是，在多窗口模式下，或者Activity上盖了一个透明主题的Activity、或者覆盖了一个Dialog，Activity在走完onPause之后，是不会走onStop的。

- **onStop**

  : onStop时，Activity对用户就已经不可见了，已经完全进入后台了。在onStop时，应当释放一些对用户不可见时无用的资源，比如停止动画，将精确定位切换成粗略定位。在onStop中，还可以执行一些CPU密集型的关闭操作，如读写数据库。


- **onDestroy**

  : onDestroy是Activity被销毁时执行的生命周期方法，不论是主动结束Activity还是异常情况下Activity被销毁，都会走到这个方法。

- **onRestart**

  : 当从Activity离开，走完onStop后，如果再次返回到当前Activity，则会走到onRestart。


### 异常生命周期

🌰🌰🌰：onPause和onStop不执行

如果在onStart中直接调用finish()方法，由于Activity还没到前台，onPause和onStop也就不会执行。

🌰🌰🌰：onDestroy方法不执行

一般情况下，onDestroy方法都是会执行的，但是当任务栈中存在多个未销毁的Activity时，通过最近任务杀死进程，只有处于栈顶的Activity才会走onDestroy方法。

🌰🌰🌰： 主动finishActivity，10s之后才执行onDestroy

调用finish()方法会导致系统触发Activity的onDestry()，但是调用finish()之后，只是先主线程的消息队列发送一条销毁Activity的消息，因此不会马上触发onDestroy()。比如有场景，从ActivityA启动ActivityB，并同时finish()掉ActivityA，同时ActivityB中通过Handler post消息持续播放动画，此时由于消息队列一直在处理前台的ActivityB的消息，会导致处于后台的ActivityA的销毁的消息一直等不到执行的机会，但是系统并不会让后台的Activity一直不销毁，占用系统资源，因此有一个兜底的10s时间，超时后即会销毁。同样的，如果Activity的转场动画时间很长，也同样有机会触发超时。

## 状态保存与恢复

一般Activity在2大类场景下需要进行状态的保存与恢复，内存不足导致Activity被杀死和配置变化导致的Activity重建。

**状态保存**

Activity中提供了onSaveInstanceState()方法来保存状态，该方法在onStop之前调用，将需要保存的数据写入bundle中，既可完成数据的保存。

在API 21之后，Activity的onSaveInstanceState()增加了一个重载的方法：

```java
public void onSaveInstanceState(@NonNull Bundle outState,
            @NonNull PersistableBundle outPersistentState) {
  onSaveInstanceState(outState);
}
```
在清单文件中对Activity增加属性```android:persistableMode="persistAcrossReboots"```之后，Activity具有了持久化保存数据的能力，设备重启之后首次再打开Activity，被持久化的参数就传到onCreate方法的Bundle参数中。

Activity的onSaveInstanceState方法中，使用委托的方式，通过调用Window的```saveHierarchyState```方法保存视图结构，这里的Window通常是PhoneWindow，PhoneWindow又继续调用其ContentView的```saveHierarchyState```方法来委托其子View保存其状态。子View如需保存其状态，必须要有id，且必须设置属性```android:=android:saveEnabled="true"```。

**状态恢复**

状态恢复的方法有2个，一个是onCreate方法，一个是onRestoreInstanceState。

onCreate方法的参数中有一个Bundle方法，Bundle非空时，可以利用Bundle中的数据恢复状态。

onSaveInstanceState方法在onCreate方法之后调用，参数也是一个Bundle参数，可以通过其恢复状态。

### 内存不足Activity被杀死

当系统内存不足时，会杀死一些进程来释放资源，进程被杀死的优先级跟当前进程的前后台状态有关。

|  系统杀进程可能性| 进程状态                   | Activity状态                 |
|:------------- |:------------------------- |:--------------------------- |
|  小           |  前台（有焦点或即将获取焦点）  | onCreate、onStart、onResume  |
|  大           |  后台（即将失去焦点）         | onPause                     |
|  最大         |  后台（失去焦点）            |  onStop                      |
|  最大         |  空                        |  onDestroy                   | 

### 配置变化导致Activity重建

当配置发生变更时，Activity会被销毁之后重新创建。常见的会触发配置变更的行为包括：横竖屏切换、语言或输入设备发生变化。配置变更时会回调onConfigurationChanged方法，也会调用onSaveInstanceState方法，可以在对应的方法中保存状态。

配置```android:configChanges=""```可以让配置改变的时候不重启Activity

## 任务栈

### 启动模式

设置Activity的启动模式有种方式，通过清单文件设置或者在Intent中设置FLAG标记。

**使用清单文件**

- **stardard** 标准模式，每次启动均创建一个新的Activity实例;

- **singleTop** 栈顶复用，要启动的Activity在栈顶时复用Activity实例，同时调用onNewIntent()方法，否则和标准模式一样；

- **singleTask** 栈内复用，在要启动的任务栈中有Activity的实例就复用，同时调用onNewIntent()方法，如果启动的任务栈中不存在Activity实例，就会创建一个新的任务栈，并创建Activity的实例。这种模式启动Activity自带CLEAR_TOP的特性，会将这个Activity之上的Activity都出栈；

- **singleInstance** 单例模式，独享一个任务栈

**使用Intent标记**

- FLAG_ACTIVITY_NEW_TASK
  虽然名字叫NEW_TASK，但是和清单文件中配置singleTask效果是一样的。

- FLAG_ACTIVITY_SINGLE_TOP
  效果和清单文件中配置singleTop效果一样。

- FLAG_ACTIVITY_CLEAR_TOP
  清单文件中lanchMode没有与之匹配的模式。如果启动的Activity在栈内但不在栈顶，会清空其上方的Activity，不会创建新实例，但会调用onNewIntent()方法。

### 任务栈的设置

清单文件中设置taskAffinity，可以指定要启动的Activity的任务栈，默认和包名一样;

清单文件中还有一个属性allTaskReparenting，当设置该属性时，Activity可以从一个任务栈中移到另一个任务栈中。

通过adb命令可以获取当前的任务栈：
```
adb shell dumpsys activity activities
```

在代码中，可以调用```activityManager.getRunningTasks```可以获取任务栈。

## 页面导航

### 隐式Intent匹配

- **category:**   可以没有，一旦指定，必须完全匹配
- **data:**   和action的匹配规则一样


## Activity的启动流程

*参考:*

 1. [Android developers -- Activity](https://developer.android.google.cn/guide/components/activities/intro-activities)
 2. [Activity与启动方式详解](http://blog.csdn.net/singwhatiwanna/article/details/9294285)
