# 集合

## 集合与数组

数组是定长的，初始化的时候必须指定长度。基本类型都有对应类型的数组，比如 IntArray、CharArray。

集合分为可变集合和只读集合，非可变集合是可以动态扩容的。非可变集合，其元素不能修改。无论只读集合还是非只读集合，编译成的字节码都对应 Java 中的集合，所谓“不可变”实际是在编译期确定的。即使是只读的，但是还是有可能被Java层修改。

```kotlin
val array = intArrayOf(1, 2, 3)
val list = listOf(1, 2, 3)
array[0] = 10  // 可变
// list[0] = 10 // 编译错误
```

## 集合的层次结构

```text
Iterable
├── Collection
│   ├── List
│   │   └── MutableList
│   └── Set
│       └── MutableSet
└── Map（独立，不继承 Collection）
    └── MutableMap
```

常见的三种集合是List、Set、Map，和 Java 中集合的继承结构类似，Map 是单独的，List和Set继承自Collection. List、Set、Map 接口都是只读的，可变集合继承自他们，对应的类型是 MutableXXX.

创建集合一般用 xxxOf() 方法，比如 listOf、mutableSetOf等。由于底层的结构

常见的集合中：

- listOf() 返回 ArraysUtilJVM$ArrayList 或 SingletonList，不可变。
- mutableListOf() 返回 ArrayList。
- mapOf() 返回 LinkedHashMap

## 和 Java 集合之间的对应关系

Kotlin 集合编译后的字节码映射为 Java 集合：

| Kotlin | Java |
| -------- | ------ |
| `List` | `java.util.List` |
| `MutableList` | `java.util.List` |
| `Set` | `java.util.Set` |
| `Map` | `java.util.Map` |
| `Collection` | `java.util.Collection` |

- Kotlin 只读集合和可变集合编译后都是 Java 可变接口，区别只在编译期。
- Java 调用 Kotlin 返回的 `List` 时，可以修改，Kotlin 不保证不可变。
- Java 的 `List` 在 Kotlin 中视为平台类型 `(Mutable)List<T!>!`，可读可写。

## 常用操作符

### 1. 转换

| 操作符 | 作用 | 示例 |
| -------- | ------ | ------ |
| `map` | 元素转换 | `list.map { it * 2 }` |
| `flatMap` | 转换并展平 | `list.flatMap { listOf(it, it) }` |
| `filter` | 过滤 | `list.filter { it > 0 }` |
| `filterNot` | 反向过滤 | `list.filterNot { it > 0 }` |
| `mapNotNull` | 转换并过滤 null | `list.mapNotNull { it.toIntOrNull() }` |
| `flatten` | 展平嵌套集合 | `listOf(listOf(1), listOf(2)).flatten()` |
| `zip` | 合并两个集合 | `listA.zip(listB) { a, b -> a + b }` |
| `unzip` | 拆分 Pair 集合 | `pairs.unzip()` |

### 2. 聚合

| 操作符 | 作用 | 说明 |
| -------- | ------ | ------ |
| `fold` | 带初始值累积 | `list.fold(0) { acc, i -> acc + i }` |
| `reduce` | 无初始值累积 | 空集合抛异常 |
| `sum` | 求和 | 数字集合 |
| `average` | 平均值 | 数字集合 |
| `count` | 计数 | 可带条件 |
| `maxOrNull` / `minOrNull` | 最大/最小 | 空集合返回 null |
| `maxByOrNull` / `minByOrNull` | 按条件最大/最小 | 空集合返回 null |

### 3. 排序

| 操作符 | 作用 |
| -------- | ------ |
| `sorted` | 自然排序 |
| `sortedBy` | 按选择器排序 |
| `sortedDescending` | 降序 |
| `sortedByDescending` | 按选择器降序 |
| `sortedWith` | 自定义 Comparator |

### 4. 分组与关联

| 操作符 | 作用 | 返回 |
| -------- | ------ | ------ |
| `groupBy` | 按 key 分组 | `Map<K, List<T>>` |
| `associate` | 自定义键值对 | `Map<K, V>` |
| `associateBy` | 指定 key，value 是元素 | `Map<K, T>` |
| `associateWith` | 指定 value，key 是元素 | `Map<T, V>` |
| `partition` | 按条件分两组 | `Pair<List<T>, List<T>>` |

### 5. 查找与判断

| 操作符 | 作用 |
| -------- | ------ |
| `find` / `firstOrNull` | 找第一个匹配 |
| `any` | 是否有匹配 |
| `all` | 是否全部匹配 |
| `none` | 是否无匹配 |
| `contains` | 是否包含 |
| `isEmpty` / `isNotEmpty` | 是否为空 |

### 6. 取子集

| 操作符 | 作用 |
| -------- | ------ |
| `take(n)` | 取前 n 个 |
| `takeLast(n)` | 取后 n 个 |
| `drop(n)` | 去掉前 n 个 |
| `dropLast(n)` | 去掉后 n 个 |
| `slice(range)` | 取指定范围 |
| `distinct` | 去重 |
| `distinctBy` | 按选择器去重 |

## 惰性求值

Kotlin 中用 Sequence 来惰性求值。

| 特性 | `Iterable` | `Sequence` |
| ------ | ----------- | ----------- |
| 求值 | 立即求值 | 惰性求值 |
| 中间操作 | 生成新集合 | 返回新 Sequence |
| 内存 | 每步生成中间集合 | 无中间集合 |
| 性能 | 小数据量快 | 大数据量、链式多时快 |
| 终端操作 | 无 | `toList`、`first`、`count` 触发执行 |

```kotlin
// Iterable：每步生成新集合
val result = (1..1_000_000)
    .map { it * 2 }       // 生成 100 万列表
    .filter { it % 3 == 0 } // 再生成列表
    .take(10)             // 再生成列表

// Sequence：惰性，只计算前 10 个
val result = (1..1_000_000).asSequence()
    .map { it * 2 }
    .filter { it % 3 == 0 }
    .take(10)
    .toList()             // 终端操作，触发执行
```

Sequence 的使用场景：

- 大数据量（十万以上）。
- 链式操作多。
- 只需部分结果（`take`、`first`）。
- 避免中间集合内存开销。

Sequence 也有开销，小数据量可能比 Iterable 慢；`sequence { }` 构建器用 `yield` 发射元素。

比如模仿一个分页的网络请求。

```kotlin
fun fetchAllUsers(): Sequence<User> = sequence {
    var currentPage = 1
    while (true) {
        val response = api.getUsers(page = currentPage) // 假设这是阻塞式分页请求
        if (response.items.isEmpty()) break
        
        yieldAll(response.items) // 把这一页的数据逐条吐出给下游
        currentPage++
    }
}

// 实际调用：如果只需要前 25 个活跃用户，且每页 20 条，它只会自动请求第 1 页和第 2 页，绝不会多请求第 3 页
val activeUsers = fetchAllUsers()
    .filter { it.isActive }
    .take(25)
    .toList()
```

## 线程安全

Kotlin 中的集合都是非线程安全的，如果需要用到线程安全的集合，要用 Java 自带的线程安全集合。协程中用 `Mutex` 保护共享集合，或用 `Channel`、`Flow` 传递数据。
