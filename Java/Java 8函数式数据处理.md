# Java 8函数式数据处理

# 1 流

## 1.1 流是什么

**流**是Java 8中新引入的概念，它允许你以声明式方式处理数据集合（通过查询语句来表达，而不是临时便携一个实现）。

举个例子，筛选出价格大于¥50的菜品，并对这些菜品进行排序，最后返回菜品名称的集合，在Java 8之前：

```Java
//第一步，筛选
List<Dish> tempList = new ArrayList<>(dishes.size());
for (Dish dish : dishes) {
	if (dish.getPriceCent() > 5000) {
		tempList.add(dish);
	}
}
//第二步，排序
Collections.sort(tempList, new Comparator<Dish>() {
	public int compare(Dish d1, Dish d2) {
		return d1.getPriceCent() - d2.getPriceCent();
	}
});
//第三步，返回名称集合
List<String> result = new ArrayList<>(tempList.size())
for (Dish dish : tempList) {
	result.add(dish.getName());
}
```
在Java 8中，引入了流的概念之后，结合Lambda表达式：

```Java
List<String> result = dishes.stream()
							.filter(dish -> dish.getPriceCent() > 5000)
							.sorted(comparing(Dish::getPriceCent))
							.map(Dish::getName)
							.collect(toList());
```

流式方法的好处：

- 代码是以声明性方式写的，说明想要完成什么，而不是如何实现一个操作；
- 把几个基本操作链接起来，用以表达复杂的数据操作流水线，使代码清晰可读。

使用Java 8的Stream API可以写出这样的代码：

- 声明性——更简洁 ，更易读
- 可复合——更灵活
- 可并行——性能更好

## 1.2 流简介

Java 8中的集合支持一个新的stream方法，它会返回一个流，当然也有很多其他方法，比如利用数值范围或者I/O资源也可以生成流元素。

定义：**从支持数据处理操作的源生成得元素序列。**

关键概念：

|术语 			|说明	|
|----			|----		|
|元素序列		|类似集合，流提供一个接口，可以访问特定元素类型的一组有序值。集合讲的是数据，流讲的是计算。|
|源				|流会使用一个提供数据的源，比如集合、数组或者是I/O. 从有序集合生成流时会保留原有的序列。|
|数据处理操作	|流的数据处理功能类似于数据库的操作，以及函数式编程语言中的常用操作，如filter、map、reduce、find、match、sort等。流操作可以顺序执行，也可以并行执行。|
|流水线			|很多的流操作本身会返回一个流，这样多个操作就可以链接起来，形成一个流水线。|
|内部迭代		|和使用迭代器进行显示迭代的集合不同，流的迭代操作是在背后进行的。|


























