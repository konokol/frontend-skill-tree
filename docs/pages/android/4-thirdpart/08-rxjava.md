# RxJava

## 核心概念与原理

RxJava是基于响应式编程的库，通过Observable发射数据，通过Observer观察数据，使用各种操作符进行转换、组合灯操作。核心思想的是观察这模式和数据流驱动。

**Observable和Observaber的区别**

- Observable是数据源，负责发送数据和事件
- Observer是观察者，订阅数据源，通过onNext，onError和onComplete处理数据。

**RxJava中使用的设计模式**

- 观察者模式，Observable和Observer解耦
- 装饰这模式，链式操作
- 迭代器模式，数据流的遍历

## 操作符

**常用的操作符**

- 转换类：map(一对一转换)、flatMap(一对多转换)、concatMap(顺序合并)、switchMap()
- 处理类：fliter(过滤)、take(取前N项)、debounce(防抖)、reduce(压缩)
- 组合类：zip(合并多个流)、merge(无序合并)、concat(顺序合并)

**map和flatMap的区别**

map是将一个元素转成成另一个元素，flatMap是将一个元素转换成新的observeble，最终合并的结果是无序的。

**switchMap与concatMap的区别**

switchMap：新事件会取消未完成的旧事件流，仅保留最新结果。concatMap：严格按顺序处理事件流，保证顺序性。

## 线程管理与调度

**subscribeOn和observeOn的区别**

subscribeOn是指定数据流(生产者)的线程，仅调用的首次生效，onserveOn是指定观察者的线程，可以多次调用。

**常见的Scheduler类型**

- Scheduler.io()，io密集型任务
- Scheduler.computation()，CPU密集型任务
- AndroidSchedulers.mainThread()，Android的主线程

## 背压

背压是指上游数据源发射的速度超过了下游观察者消费的速度，导致数据积压，严重会造成内存溢出。

RxJava 2.0中引入了Flowable来解决背压问题，常见策略包括：

- Buffer，缓存所有的数据，直到OOM
- Drop，下游处理速度跟不上时，丢弃onNext
- Lastest，只保留最新的数据

## 内存泄漏与资源管理

当页面退出时，如果异步任务没执行完，可能造成内存泄漏。

**手动处理**：使用Disposable或CompositeDisposable，退出时手动释放  
**自动处理**：利用RxLifeCycle、AutoDispose

## RxJava 1.0和2.0的区别

*参考*

1. [RxJava官方文档](https://github.com/ReactiveX/RxJava)
2. http://zhanzhang.xihaba.cn/?jaynm/article/details/109813016
3. https://juejin.cn/post/7311630480335061042