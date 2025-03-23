# 理解Activity，View，Window三者关系

这个问题真的很不好回答。所以这里先来个算是比较恰当的比喻来形容下它们的关系吧。Activity像一个工匠（控制单元），Window像窗户（承载模型），View像窗花（显示视图）LayoutInflater像剪刀，Xml配置像窗花图纸。

1、Activity构造的时候会初始化一个Window，准确的说是PhoneWindow。

2、这个PhoneWindow有一个“ViewRoot”，这个“ViewRoot”是一个View或者说ViewGroup，是最初始的根视图。

3、“ViewRoot”通过addView方法来一个个的添加View。比如TextView，Button等

4、这些View的事件监听，是由WindowManagerService来接受消息，并且回调Activity函数。比如onClickListener，onKeyDown等。

[Activity Window View之间的三角关系](http://www.jianshu.com/p/a533467f5af5)

[理清Activity、View及Window之间关系](http://blog.csdn.net/huachao1001/article/details/51866287)
