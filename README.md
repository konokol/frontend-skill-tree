# Android学习笔记

Android常用知识点汇总，不提供详细原理，只提供大致的思路，更详细的内容可以参考每一个知识点后链接的文章，所有文章的版权属于原作者所有，此处只提炼要点。

## Android基础

### 四大组件

- [Service相关](./Android/Service%E7%9B%B8%E5%85%B3.md)
- [Activity相关](./Android/Activity%E7%9B%B8%E5%85%B3.md)
- [Activity与Fragment通信方式](./Android/Activity%E4%B8%8EFragment%E9%80%9A%E4%BF%A1%E6%96%B9%E5%BC%8F.md)
 
### Fragment

- [Activity与Fragment通信方式](./Android/Activity%E4%B8%8EFragment%E9%80%9A%E4%BF%A1%E6%96%B9%E5%BC%8F.md)
- [Fragment全解析系列（一）：那些年踩过的坑](http://www.jianshu.com/p/d9143a92ad94)

### View原理

- [事件分发机制](./Android/%E4%BA%8B%E4%BB%B6%E5%88%86%E5%8F%91%E6%9C%BA%E5%88%B6.md)
- [Window的理解](./Android/Window%E7%9A%84%E7%90%86%E8%A7%A3.md)
- [View的绘制流程](./Android/View%E7%9A%84%E7%BB%98%E5%88%B6%E6%B5%81%E7%A8%8B.md)

### 动画

- [动画简介](./Android/%E5%8A%A8%E7%94%BB%E7%AE%80%E4%BB%8B.md)

### Android中的多线程

- [HandlerThread与IntentService](./Android/HandlerThread%E4%B8%8EIntentService.md)

### 虚拟机相关

- [64K方法限制](./Android/64K%E6%96%B9%E6%B3%95%E9%99%90%E5%88%B6.md)
- [Android GC原理](./Android/Android%20GC%E5%8E%9F%E7%90%86.md)

### 版本新特性

- [Android 5.0到7.0的行为变更](./Android/Android%205.0%E5%88%B07.0%E7%9A%84%E8%A1%8C%E4%B8%BA%E5%8F%98%E6%9B%B4.md)

### 热修复

- [热修复原理](./Android/%E7%83%AD%E4%BF%AE%E5%A4%8D%E5%8E%9F%E7%90%86.md)

### 多线程

- [AsyncTask原理解析](./Android/AsyncTask%E5%8E%9F%E7%90%86%E8%A7%A3%E6%9E%90.md)

### 开源框架源码

- [ButterKnife源码解析](./Android/ButterKnife%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90.md)
- [Fresco相关](./Android/Fresco%E7%9B%B8%E5%85%B3.md)
- [EventBus原理解析](./Android/EventBus%E5%8E%9F%E7%90%86%E8%A7%A3%E6%9E%90.md)

### 系统与源码

- [Android源码阅读计划](./Android/Framework/Android%E6%BA%90%E7%A0%81%E9%98%85%E8%AF%BB%E8%AE%A1%E5%88%92.md)
- [AsyncTask原理解析](./Android/AsyncTask%E5%8E%9F%E7%90%86%E8%A7%A3%E6%9E%90.md)
- [Handler消息机制](./Android/Handler%E6%B6%88%E6%81%AF%E6%9C%BA%E5%88%B6.md)
- [Android中对集合的优化](./Android/Android%E4%B8%AD%E5%AF%B9%E9%9B%86%E5%90%88%E7%9A%84%E4%BC%98%E5%8C%96.md)

### IO

- [序列化](./Android/%E5%BA%8F%E5%88%97%E5%8C%96.md)

### 性能优化

- [Android内存泄漏](./Android/Android%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F.md)
- [数据库优化](./Android/%E6%95%B0%E6%8D%AE%E5%BA%93%E4%BC%98%E5%8C%96.md)
- [图片加载相关](./Android/%E5%9B%BE%E7%89%87%E5%8A%A0%E8%BD%BD%E7%9B%B8%E5%85%B3.md)

## 其他
- [如何保证进程不被杀死](./Android/%E5%A6%82%E4%BD%95%E4%BF%9D%E8%AF%81%E8%BF%9B%E7%A8%8B%E4%B8%8D%E8%A2%AB%E6%9D%80%E6%AD%BB.md)
- [Android知识点汇总](./Android/Android%E7%9F%A5%E8%AF%86%E7%82%B9%E6%B1%87%E6%80%BB.md)

## Java基础

### 基础

- [异常](./Java/%E5%BC%82%E5%B8%B8.md)
- [注解](./Java/%E6%B3%A8%E8%A7%A3.md)
- [Java单例的写法](./Java/Java%E5%8D%95%E4%BE%8B%E7%9A%84%E5%86%99%E6%B3%95.md)
- [Java知识点汇总](./Java/Java%E7%9F%A5%E8%AF%86%E7%82%B9%E6%B1%87%E6%80%BB.md)
- [String、StringBuilder、StringBuffer的区别](./Java/String%E3%80%81StringBuilder%E3%80%81StringBuffer%E7%9A%84%E5%8C%BA%E5%88%AB.md)

### 新版本特性

- [Java 8函数式数据处理](./Java/Java%208%E5%87%BD%E6%95%B0%E5%BC%8F%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86.md)
- [Java 8 ----Lambda表达式](./Java/Java%208%20----Lambda%E8%A1%A8%E8%BE%BE%E5%BC%8F.md)

### 多线程

- [ThreadLocal原理](./Java/ThreadLocal%E5%8E%9F%E7%90%86.md)

### 集合

- [集合框架](./Java/%E9%9B%86%E5%90%88%E6%A1%86%E6%9E%B6.md)

### Java虚拟机

- [JVM运行时内存模型](./Java/JVM%E8%BF%90%E8%A1%8C%E6%97%B6%E5%86%85%E5%AD%98%E6%A8%A1%E5%9E%8B.md)

### 其他

- [面向对象](./Java/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1.md)
- [Java中的四种引用](./Java/Java%E4%B8%AD%E7%9A%84%E5%9B%9B%E7%A7%8D%E5%BC%95%E7%94%A8.md)