<!-- Activity -->

# Android四大组件之Activity

## 生命周期

### Activity正常生命周期

![Activity生命周期](../../../img/activity_lifecycle.png)

值得注意的是，Android 7.0之后，在多窗口模式下，只有获取到焦点的Activity才是onResume的状态，所以即使当前的Activity是完全可见的，没有焦点时也处于onPause状态。

### Activity异常情况下的生命周期

onStop()之前调用onSaveInstante()保存数据，在onCreate之后调用onRestoreInstanceState(Bundle)恢复数据，委托Window以及上层的View保存数据

#### 内存不足Activity被杀死

#### 配置变化导致Activity重建
配置```android:configChanges=""```可以让配置改变的时候不重启Activity

## 启动Activity的方式

### 隐式Intent匹配

- **category:**   可以没有，一旦指定，必须完全匹配
- **data:**   和action的匹配规则一样

### Activity的启动模式

- **stardard** 标准模式，每次启动均创建一个新的Activity实例;

- **singleTop** 栈顶复用，要启动的Activity在栈顶时复用Activity实例，否则和标准模式一样；

- **singleTask** 栈内复用，在要启动的任务栈中有Activity的实例就复用；

- **singleInstance** 单例模式，独享任务栈

  

  指定要启动的Activity的任务栈，taskAffinity，默认和包名一样;

指定启动模式的方式，manifest文件或者Intent中设置flag，不完全一直，可以指定NEW_TASK，SINGLE_TOP，CLEAR_TOP，EXECULE_FROM_RECENT

 [Activity与启动方式详解](http://blog.csdn.net/singwhatiwanna/article/details/9294285)
