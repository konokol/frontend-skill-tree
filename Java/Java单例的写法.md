# Java单例的写法

## 双重校验

最常见的写法；

```Java
class Singleton {
  private static volatile Singleton instance;

  private Singleton(){}

  public static Singleton getInstance() {
    if (instance == null) {
      synchronized(Singleton.class) {
        instance = new Singleton();
      }
    }
  }
}
```

## 饿汉机制

比较少用，在类加载的时候，就已经实例化了；

```Java
class Singleton {
  private static final Singleton instance = new Singleton();

  private Singleton(){}

  public static Instance getInstance() {
    return instance;
  }
}
```

## 懒汉模式
只要InstanceHolder没有被主动使用过，就不会被加载，实际上也是相当于懒加载的。

```Java
class Singleton {
  private static Singleton instance;

  public static Singleton getInstance() {
    return InstanceHolder.INSTANCE;
  }

  private static class InstanceHolder {
    private static final Singleton INSTANCE = new Singleton();
  }
}
```
## 使用枚举

枚举本身就是单例的。枚举类是在第一次访问时才被实例化，是懒加载的

```Java
class enum Singleton {
  INSTANCE;
}
```
