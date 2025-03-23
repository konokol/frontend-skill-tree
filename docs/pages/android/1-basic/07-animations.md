# Android动画

## ViewAnimation
ViewAnimation是比较简单的动画，一共有4种alpha, rotate, translate, scale. 需要注意的是，ViewAnimation并不会改变View本身的属性。

**使用方法**

- 使用xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android">

    <alpha
        android:duration="300"
        android:fromAlpha="1.0"
        android:toAlpha="0.0" />
</set>
```
```Java
view.startAnimation(AnimationUtils.loadAnimation(context, R.anim.alpha));
```
- 代码实现
```Java
TranslateAnimation translateAnimation =
              new TranslateAnimation(
                  Animation.RELATIVE_TO_SELF,0f,
                  Animation.RELATIVE_TO_SELF,100f,
                  Animation.RELATIVE_TO_SELF,0f,
                  Animation.RELATIVE_TO_SELF,100f);
           translateAnimation.setDuration(1000);
           view.startAnimation(translateAnimation);
```

## DrawableAnimation
DrawableAnimation是通过设置一组图片，然后顺序播放来实现动画，比如ImageView的背景。

**使用方法**

和ViewAnimation类似，可以通过xml和代码来实现。
- xml方式</br>
在drawable文件夹下新建
```xml
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="false">

    <item
        android:drawable="@drawable/ic_battery_charging_20"
        android:duration="300" />

    <item
        android:drawable="@drawable/ic_battery_charging_30"
        android:duration="300" />
</animation-list>
```
在代码中
```Java
view.setBackgroundResource(R.drawable.charging);
((AnimationDrawable) view.getBackground()).start()
```

- 纯代码</br>
```Java
animationDrawable = new AnimationDrawable();
Drawable drawable = getResources().getDrawable(R.drawable.image);
animationDrawable.addFrame(mDrawable, 500);
animationDrawable.setOneShot(false);
view.setBackgroundDrawable(animationDrawable);
animationDrawable.start();
```

## PropertyAnimation

PropertyAnimation是Android 3.0（API 11）之后引入的动画，它是通过真实的改变View的值来实现的动画，是最强大的动画。只要是View的set方法可以设置的属性，都可以进行动画，比如scale，backgroudColor，alpha等等。

**用法**

和其他两种动画一样，也可以通过xml和代码的形式来实现。
- 通过xml的时候，需要先定义animator-list，在其中写属性动画，可以顺序播放，也可以同时播放，通过AnimatorInflater.loadAnimato(context, animator)；
- 通过代码，ObjectAnimator.of(view, propertyName, args)来实现。

**自定义属性动画**

```Java
ValueAnimator animator = ValueAnimator.ofObject(new TypeEvaluator() {
            @Override
            public Object evaluate(float fraction, Object startValue, Object endValue) {
                return null;
            }
        } , 0 , 100);
animator.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
        @Override
        public void onAnimationUpdate(ValueAnimator animation) {
          //设置View的属性
        }
});
animator.setDuration(2000);
animator.start();
```

## Animation与Animator的区别

Animation是改变View的外观，实际不会改变View的位置；
Animator是改变View的属性，真正改变了View的属性。

[Android 动画,看完这些还不够](http://blog.csdn.net/u012984054/article/details/50841476)
