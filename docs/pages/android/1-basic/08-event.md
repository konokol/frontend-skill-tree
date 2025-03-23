# 事件

## 事件分发机制

### MotionEvent

MotionEvent有4种状态:
- MotionEvent.ACTION_DOWN，手指按下的瞬间；
- MotionEvent.ACTION_MOVE，手指在屏幕上移动；
- MotionEvent.ACTION_UP，手指抬起的瞬间；
- MotionEvent.ACTION_CANCEL，取消手势，一般不由用户手动产生.

事件分发的过程中，由上层向下层传递，直到事件被处理，如果传到最底层也没有处理，则继续向外层分发。

### 3个重要方法

- dispatchTouchEvent()，决定事件是否往下分发，返回true表示事件已经被消费，false表示在本层事件不在往下分发由上层的onEvent处理事件，super表示事件由本层的onInterceptTouchEvent决定是否继续向下分发。
- onInterceptTouchEvent()，是否对事件拦截，返回false的时候，表示不拦截，交由下层的dispatchTouchEvent继续处理，否则拦截事件，由本层的onTouchEvent处理；
- onTouchEvent()，事件处理，返回true的，表示事件被消费，不再传递，返回false或者super，事件都继续向上层继续传递。


### Android触摸事件流程总结

1. 一个事件序列是指从手指触摸屏幕开始，到手指离开屏幕结束，这个过程中产生的一系列事件。同一个事件序列是以ACTION_DOWN事件开始，中间含有数量不定的MOVE事件，最终以ACTION_UP事件结束。

2. 事件传递的顺序是：Activity->Window->View，即事件总是先传递给Activity，然后在传递给Window，最后在传递给View，顶级View接收到事件后，就会按照事件分发机制去分发事件。

3. 事件的传递过程是由外向内的，即事件总是由父元素分发给子元素。

4. 正常情况下，一个事件序列只能被一个View拦截且消耗。一旦一个元素拦截了某次事件，那么同一个事件序列内的所有事件都会直接交给它处理，因此同一个事件序列中的事件不能分别由两个View同时处理，但是通过特殊手段可以做到，比如一个View将本该自己处理的事件通过onTouchEvent强行传递给其他View处理。

5. 某个View一旦开始处理事件，如果它不消耗ACTION_DOWN事件，那么同一事件序列的其他事情都不会再交给它来处理，并且事件将重新交给它的父容器去处理（调用父容器的onTouchEvent方法）；如果它消耗ACTION_DOWN事件，但是不消耗其他类型事件，那么这个点击事件会消失，父容器的onTouchEvent方法不会被调用，当前view依然可以收到后续的事件，但是这些事件最后都会传递给Activity处理。

6. Android点击事件分发是到达顶级View后（一般是ViewGroup），会调用ViewGroup的dispatchTouchEvent方法，其中它的onInterceptTouchEvent方法如果返回true，则会对事件传递进行拦截，事件由ViewGroup处理；如果onInterceptTouchEvent方法返回false，则代表不对事件进行拦截，默认返回false。则此时子View中的dispatchTouchEvent方法将被调用，到此，事件已经由顶级View传递给了下一层的View，接下来的过程是一个递归循环的过程，和顶级View事件分发过程是一致的，直到完成整个事件分发。

*参考*  

[Android事件分发机制详解：史上最全面、最易懂](http://blog.csdn.net/carson_ho/article/details/54136311)</br>
[Android事件分发机制完全解析，带你从源码的角度彻底理解(上)](http://blog.csdn.net/guolin_blog/article/details/9097463)</br>
[Android事件分发机制完全解析，带你从源码的角度彻底理解(下)](http://blog.csdn.net/guolin_blog/article/details/9153747)</br>
