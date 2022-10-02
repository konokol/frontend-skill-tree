# 字符串

## String、StringBuilder、StringBuffer 的区别

1. **String**

  String是不可变的对象，底层使用final类型的数组，每次String类型对象改变时，实际都是重新生成一个对象。

2. **StringBuffer**

  StringBuffer是线程安全的可变的对象，是可修改的，而且修改的都是对象本身，由于StringBuilder的绝大多数方法都是synchronized的，所以是线程安全的，但是当多线程操作同一个对象时，会比较慢。

3. **StringBuilder**

  StringBuilder也是可变的字符串对象，和StringBuffer类似，也是可以修改的，但是StringBuilder是非线程安全的。
