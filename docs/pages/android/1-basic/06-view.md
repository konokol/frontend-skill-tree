# View

## View的绘制流程

**测量(Measure)**

onMeasure(int widthSpec, int heightSpec)</br>
宽高的MeasureSpec，int值32位，高两位表示Mode， 低30位表示size，测量时，measureSpec由父View向子View传递。

MeasureSpec的Mode有3种值：
> UNSPECIFIED 父容器对子容器没有任何限制，子容器想要多大都可以
> EXACTLY 父容器已经为子容器设置了尺寸,子容器应当服从这些边界,不论子容器想要多大的空间。
> AT_MOST 子容器大小可以是指定大小内的任意值

1. 父View的MeasureSpec是EXACTLY
  - 子View的layout_width或layout_height是match_parent，则子View的MeasureSpec也是EXACTLY;
  - 子View的layout_xxx是wrap_content，MeasureSpec是AT_MOST;
  - 子View的layout_xxx是具体的值，MeasureSpec是EXACTLY.
2. 父View的MeasureSpec是UNSPECIFIED
  - 子View的layout_xxx是match_parent，MeasureSpec是UNSPECIFIED;
  - 子View的layout_xxx是wrap_content，MeasureSpec是UNSPECIFIED;
  - 子View的layout_xxx是具体值，MeasureSpec是EXACTLY.
3. 父View的MeasureSpec是AT_MOST
  - 子View的layout_xxx是match_parent，MeasureSpec是 AT_MOST;
  - 子View的layout_xxx是wrap_content，MeasureSpec是AT_MOST;
  - 子View的layout_xxx是具体值，MeasureSpec是EXACTLY.

setMeasuredDimension(w, h)，设置完之后，测量结束。</br>

getDefault(getSuggestedMinimum(), measureSpec)，建议最小一般是背景图的大小，或者是minXXX的大小，只要measureSpec不是UNSPECIFIED的，都是用的测量值。

**布局(layout)**

经过测量之后，mMeasuredWidth和mMeasuredHeight获取到测量的大小，根据gravity等属性，确定每个View的位置，调用每个View的layout(l,t,r,b)方法，设置其位置。

**绘制(draw)**

1. 绘制背景；
2. 如果有必要，保存画布的layer准备fading;
3. 绘制View内容;
4. 绘制子View;
5. 如果需要，绘制fading edges，恢复layer;
6. 绘制滚动条

requestLayout()会重新布局，invalidate()和postInvalidate()重新绘制，invalidate是在主线程中，postInvalidate是异步刷新

## 自定义View


**参考**  

[View的绘制流程](http://www.jianshu.com/p/5a71014e7b1b)
