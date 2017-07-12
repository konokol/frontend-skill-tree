# ButterKnife原理解析

基于ButterKnife 8.5.1

## 1. ButterKnife用法
[Field and method binding for Android views](http://jakewharton.github.io/butterknife/)

ButterKnife可用的地方很多，Activity，Fragment，Dialog甚至是任意的Object，不过用法都大同小异。基本用法都是对View加上@BindView注解，然后在适当的地方调用ButterKnife.bind(target, source)方法。

## 2. 原理解析

这里以Fragment中的用法为例，下面的是ButterKnife官网上的例子。

```Java
public class FancyFragment extends Fragment {
  @BindView(R.id.button1) Button button1;
  @BindView(R.id.button2) Button button2;

  @Override public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    View view = inflater.inflate(R.layout.fancy_fragment, container, false);
    ButterKnife.bind(this, view);
    // TODO Use fields...
    return view;
  }
}
```
一步一步来分析源码。
1. 首先从ButterKnife.bind(this, view)看，戳进源码：
```Java
@NonNull @UiThread
  public static Unbinder bind(@NonNull Object target, @NonNull View source) {
    return createBinding(target, source);
  }
```
这里调用了createBinding方法, 返回一个Unbinder对象。

2. 继续往下看，createBinding方法是怎么创建Unbinder对象的：
```Java
private static Unbinder createBinding(@NonNull Object target, @NonNull View source) {
    Class<?> targetClass = target.getClass();
    if (debug) Log.d(TAG, "Looking up binding for " + targetClass.getName());
    Constructor<? extends Unbinder> constructor = findBindingConstructorForClass(targetClass);

    if (constructor == null) {
      return Unbinder.EMPTY;
    }
    //...
    try {
      return constructor.newInstance(target, source);
    } //省略异常处理的代码
}
```
可以看到，这里是找到通过targetClass找到一个Unbinder类的构造方法，并通过构造方法产生一个Unbinder对象，具体到上面的例子中，targetClass就是我们的FancyFragment。

3. 再继续看怎么找构造方法的，点开findBindingConstructorForClass方法：
```Java
@Nullable @CheckResult @UiThread
 private static Constructor<? extends Unbinder> findBindingConstructorForClass(Class<?> cls) {
   //BINDINGS是一个HashMap<class, Constructor>
   Constructor<? extends Unbinder> bindingCtor = BINDINGS.get(cls);
   if (bindingCtor != null) {
     if (debug) Log.d(TAG, "HIT: Cached in binding map.");
     return bindingCtor;
   }
   String clsName = cls.getName();
   //忽略调android和java包下的类
   if (clsName.startsWith("android.") || clsName.startsWith("java.")) {
     if (debug) Log.d(TAG, "MISS: Reached framework class. Abandoning search.");
     return null;
   }
   try {
     //新建一个ViewBinding类
     Class<?> bindingClass = Class.forName(clsName + "_ViewBinding");
     //noinspection unchecked
     bindingCtor = (Constructor<? extends Unbinder>) bindingClass.getConstructor(cls, View.class);
     if (debug) Log.d(TAG, "HIT: Loaded binding class and constructor.");
   } catch (ClassNotFoundException e) {
     if (debug) Log.d(TAG, "Not found. Trying superclass " + cls.getSuperclass().getName());
     bindingCtor = findBindingConstructorForClass(cls.getSuperclass());
   } catch (NoSuchMethodException e) {
     throw new RuntimeException("Unable to find binding constructor for " + clsName, e);
   }
   BINDINGS.put(cls, bindingCtor);
   return bindingCtor;
 }
```
这里代码也很简单，先从一个HashMap也就是BINDINGS中找，如果没有的话，就通过反射的方法新建实例化一个类然后取其构造方法，这个类的类名是clsName_ViewBinding，具体到上面的例子，就是创建了一个FancyFragment_ViewBinding的对象。之后，将这个对象的构造方法存入HashMap中。

 那么这个BINDINGS是什么呢？翻源码也可以看到，它是一个静态的HashMap，以class为key，value是构造方法，在这里，其实它就相当于一个缓存，只要ButterKnife.bind(...)方法调用过一次，下次就可以直接找到相关的_ViewBinding的构造方法。

4. 具体到我们最开始Fragment中ButterKnife使用的例子，到这里可以整理一下思路。在FancyFragment的onCreateView(...)方法中，我们调用了ButterKnife.bind(this, view)方法，调用这个方法之后，最终是通过构造方法实例化了一个类，即FancyFragment_ViewBinding。这个类是什么呢？肯定不能实例化一个不存在的类，编译完成之后，在项目中搜索一下这个类，会发现这个类在build文件夹下，是在编译期自动生成的，看一下这个类实现：
```Java
public class FancyFragment_ViewBinding implements Unbinder {
  private FancyFragment target;

  @UiThread
  public FancyFragment_ViewBinding(FancyFragment target, View source) {
    this.target = target;

    target.button1 = Utils.findRequiredViewAsType(source, R.id.button1, "field 'button1'", Button.class);
    target.button2 = Utils.findRequiredViewAsType(source, R.id.button2, "field 'button2'", Button.class);
  }

  @Override
  @CallSuper
  public void unbind() {
    ChannelAudioFragment target = this.target;
    if (target == null) throw new IllegalStateException("Bindings already cleared.");
    this.target = null;

    target.button1 = null;
    target.button2 = null;
  }
}
```
这里代码也很明确，Utils.findRequiredViewAsType(...)就是调用view.findViewById(id)方法，然后通过反射进行一下强制类型转换，这样就找到了id对应的view，然后复制给targetClass中注解的属性。整个流程也就省去了我们手写findViewById(id)方法的过程。
