
# 线程

## 实现多线程线程的方法

1. 直接new Thread()，重写run方法，调用start()执行;
2. 实现Runnable接口，传入到Thread的构造方法中；
3. 实现Callable接口，包装成FutureTask，传入到Thread的构造方法中。

3种方式本质上都是通过Thread类的start方法实现的多线程。