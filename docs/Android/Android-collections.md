# Android中对集合的优化

在Android中，为了节约内存，使用了SparseArray来代替key是Int的HashMap，除此之外，还有ArrayMap和ArraySet.

## SparseArray

`SparseArray<V>`可以用来代替`HashMap<Integer,V>`，使用SparseArray可以节省内存空间，但是并不能提高查找效率。

SparseArray内部，使用两个数组来分别存储key和value，插入时，如果如果key存在，直接覆盖，没有则新插入key和value. 查找时，先从key的数组中用二分查找找到key，然后直接根据key的index去查找value数组中的value值。删除时，还是先查找到key的index，然后把相应位置的value标记为DELETED，其中DELETED是一个Object对象，并标记可以GC。gc方法中，遍历数组，遇到有位置的元素被删除了，就把后面未删除的元素前移。

- `SparseArray<V>`     --> `Map<Integer, V>`
- `SparseIntArray`     --> `Map<Integer, Integer>`
- `SparseBooleanArray` --> `Map<Integer, Boolean>`
- `SparseLongArray`    --> `Map<Integer, Long>`

## ArrayMap

ArrayMap可以用来代替`ArrayMap<K,V>`，和SparseArray类似，ArrayMap中也有两个数组，一个是int类型mHashes，专门用来存key的hash值，有序排列，另外还有一个Object类型的数组mArray，用来放真正的key和value，其中根据key的hash值算出一个index，然后，把key放在mArray[index]的位置，把value放在mArray[index + 1]的位置。

数组扩容时，大于8个直接扩大到1.5倍，大于4个的时候，扩大到8，小于4个的时候，扩大到4个。

此外ArrayMap中还有两个缓存，是两个静态数组，mBaseCache和mBaseTwiceCache，扩容的时候，会把原来旧的数组赋值给这两个cache，扩容重新分配内存空间的时候，会优先取两个cache。也就是说，另外在新建另外一个ArrayMap时，可以直接取缓存，不用去新申请空间，这样也就节省了空间。

删除时，根据key的hash值找到index，如果只有一个元素，直接把两个数组赋值成空数组，如果hash数组的长度大于8且map的大小小于hash数组长度的1/3，则重新分配数组空间，否则，把相应位置的元素删了，后面的元素往前移动。
