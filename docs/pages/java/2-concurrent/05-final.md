# final

## 基础使用

- 修饰类  
  final修饰的类不可以被继承。final类中所有的方法都是隐式final的，因为不能被继承，因此final类中方法肯定不能被复写。  
  对final类扩展可以使用组合的方式，如对String类扩展，增加一个copy方法：  
  ```Java
  public class StringWrapper {
    final String realString;
    // ...

    // 代理public方法
    public int length() {
      return realString.length();
    }

    // ...

    /**
     * 扩展的方法
     **/
    public String copy() {
      return new String(realString);
    }

  }
  ```  
  JDK中常见的final类有：   
    - java.lang包，包括基本类型的包装类型(Integer、Double等)、String系列(String、StringBuffer等)、系统类(System、Class等)、数学类(Math、StrictMath)
    - java.util包，包括UUID、Optional、Scanner等
    - java.lang.reflect包，如Array、Constructor、Field等
    - java.time包，Duration、LocalTime等
  
- 修饰方法  
  final修饰的方法不能被复写，但是可以被重载。所有private方法都是隐式final的，因为private方法不可以被重写。
- 修饰变量  
  final修饰的变量为不可变变量，一旦赋值之后，不可以被重新赋值。引用类型final变量，虽然不能对变量本身重新赋值，但是可以修改引用类型的成员变量。  
  final类型成员变量，必须在声明变量时赋值，或者在构造方法、构造代码块、静态代码块中赋值。  
  final类型局部变量，必须在声明时赋值。 
  static final类型的变量可以称为Java中的常量，需要在声明变量或静态代码块中对变量赋初始值。
- 修饰参数  
  final修饰的参数表明参数不可以被重新赋值。

## final与匿名内部类

当匿名内部类访问外部局部变量时，局部变量必须被声明为final。Java 8之后虽然不用显示声明为final，但实际被匿名内部类访问的局部变量仍然是final的。
```Java
class OuterClass {

  public void foo() {
    final int a = 1; // 必须声明为final，否则会编译报错 
    Runnable r = () -> {
      System.out.println("a=" + a);
    }
    r.run();
  }

}
```
这么做的原因是，匿名内部类的生命周期可能比外部类长，当外部类的方法调用结束后，调用栈被清空，局部变量值被回收，如果匿名内部类直接引用外部类的局部变量，这种场景下，有可能会访问到一个被回收的变量。  
因此JVM的实现中，对于被引用的局部变量，给匿名内部类增加了一个成员变量，将局部变量的值赋值给匿名内部类的成员变量，但是存在成员变量被重新赋值的可能，为了保证安全，强制约定被匿名内部类引用的成员变量必须声明为final类型。  
上面的代码等同于下面的代码：
```Java
class OuterClass {
  public void foo() {
    final int a = 1;
    Runnable r = new OuterClass$1(a);
    r.run();
  }
}

class OuterClass$1 implements Runnable {
  int a;

  OuterClass(int a) {
    this.a = a;
  }

  public void run() {
    System.out.println("a=" + a);
  }
}
```

## final重排序规则

- 基本数据类型    
    - 写：禁止final的写重排序到构造方法外面，即保证当对象对其他线程可见时，final变量一定是被初始化过的。
    - 读：禁止初次读对象的引用与读该对象的final域变量重排序，即保证读到final变量的引用时，一定会先读包含final变量的引用，从而避免了读到未初始化变量的情况。
- 引用类型  
    - 增加额外的约束：禁止对“构造方法对final变量的写入”和“将对象引用赋值给引用变量”重排序，避免重新赋值后，取到未赋值的final变量。

## final的实现原理

## 参考

[关键字: final详解](https://www.pdai.tech/md/java/thread/java-thread-x-key-final.html)
