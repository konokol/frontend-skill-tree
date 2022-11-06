# 数字和字符串

## 数字

数字类的继承关系

![数字的继承关系](../../img/numbers.png)

大体上分为3类

**包装类型**

Byte、Short、Integer、Long、FLoat、Double这6个类对应相应的基本类型，和基本类型可以互相拆箱和装箱

**大数**

BigInteger和BigDecimal是java.math包中的类，其作用是为了精确表示浮点数，以及整数的大数计算

**原子操作类**

AutomaticInteger、AutomaticLong、Scripted64这几个类是java.util.concurrent.atomic包中的类，用来处理原子性操作的。

基本类型的自增和自减操作，实际上是可以拆解成n=n+1(或n=n-1)，不具备原子性，因此增加了原子类来做原子性的计算。

除了图中列出的几个，还有AutomaticBoolean等原子类，只是不继承Number

## 字符串

**String**

**StringBuilder**

**StringBuffer**


*参考*

1、[Oracle-数字与字符串](https://docs.oracle.com/javase/tutorial/java/data/index.html)

