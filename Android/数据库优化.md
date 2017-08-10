# Android SQLite数据库优化

## 建立索引

建立索引的语句：
```Java
//为整张表建立索引
CREATE INDEX index_name ON table_name;
//创建单列索引
CREATE INDEX index_name ON table_name (column_name);
```
需要注意的是，索引会使查询的速度加快，但是却会使插入，删除和更新的速度变慢，在数据量比较小的时候，新建索引反而会增大数据库的大小。

## 编译SQL语句

对于需要重复执行很多次的SQL语句，可以编译成SQLiteStatement语句。

## 使用事务

批量操作，可以使用事务，减少反复数据库文件的IO操作。

## 其它的优化

- db.query语句，只返回需要的列；
- 遍历cursor时，提前通过curcor.getColumnIndex()获取到index，不在循环中做；
- ContentValue底层是用HashMap实现的，根据需要指定容量；
- db和cursor对象及时关闭；
- 耗时的操作放在子线程；

[Android 中 SQLite 性能优化](https://zhuanlan.zhihu.com/p/25447017)
