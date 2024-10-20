# LeetCode常见算法题

## 数组/字符串

### [合并2个有序数组](https://leetcode.cn/problems/merge-sorted-array/description)

合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

**解法一**  顺序法  
第一次遍历把元素都移到num1的末尾，第二次从前往后遍历插入。

**解法二**  倒序法  
从后往前遍历

### [移除数组中指定元素](https://leetcode.cn/problems/remove-element/description/)

给你一个数组 `nums` 和一个值 `val`，你需要 原地 移除所有数值等于 `val` 的元素。元素的顺序可能发生改变。然后返回 `nums` 中与 `val` 不同的元素的数量。

**解法一** 2次循环直接移动  

**解法二**  快慢指针  
相等元素移动快指针，不同元素直接赋值。  

**解法三**  快慢指针优化，打乱顺序  
左右指针，元素相等时，将右指针上元素赋值给当前位置，右指针左移。

## 链表

## 哈希表

### [同构字符串](https://leetcode.cn/problems/isomorphic-strings)

给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。  
如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。  
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。 

**解法** 哈希表  
使用2个Hash表分别存s->t和t-s的映射，遍历检查正反都能隐射上。

### [单词规律](https://leetcode.cn/problems/word-pattern)

给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。  
这里的 “遵循” 指完全匹配，例如， `pattern` 里的每个字母和字符串 `s` 中的每个非空单词之间存在着双向连接的对应规律。

**解法** 哈希表  
和同构字符串的解法一样，也是用2个哈希表。

### [有效的字母异位词](https://leetcode.cn/problems/valid-anagram)

给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。

**解法一** 哈希表  
使用哈希表，key是字符，value是字符出现的次数。2次遍历，第一次向哈希表中插值，第二次从哈希表中删值。哈表表如果被清空，说明字符串是字母异位词。

**解法二** 排序
先对字符串排序，按序排的字符一样，说明字符串是字母异位词。

### [字母异位词分组](https://leetcode.cn/problems/group-anagrams)

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。字母异位词 是由重新排列源单词的所有字母得到的一个新单词。 

示例 1: 

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"] 
输出: [["bat"],["nat","tan"],["ate","eat","tea"]] 

**解法** 哈希表  
使用哈希表，key是重排序的后的单词，值是字母异位词分组的List。

## 栈

## 堆

## 树

### [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view)

给定一个二叉树的根节点 `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**解法一** 

使用层次遍历，记录最右边的节点。

### [530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst)

给你一个二叉搜索树的根节点 `root` ，返回 树中任意两不同节点值之间的最小差值。差值是一个正数，其数值等于两值之差的绝对值。

**解法**

中序遍历二叉搜索树，序列一定是升序的，所以只需要记录遍历的前一个节点即可。 

二叉搜索树遍历有3种方法：  

- 递归，先遍历左子树，读当前节点，再次遍历右节点。
- 栈，先将左子树全入栈，读当前节点，再将右节点入栈。
- Morris遍历

### [202. 快乐数](https://leetcode.cn/problems/happy-number)

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
- 如果这个过程 结果为 1，那么这个数就是快乐数。

如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

**解法一** 哈希表

计算每个每个位数上平方和，存在哈希表中，下次遍历如果哈希表中存在元素，说明有环不是快乐数。

**解法二** 快慢指针

计算每个位数的平方和，慢指针每次只算一次，快指针算2次，当快慢指针相等了，说明有环。比方法一更省内存。

## 图

## 双指针

## 滑动窗口

## 回溯

## 分治

## 动态规划

## 查找

## 排序

## 矩阵

## 区间

## 数学

[颠倒二进制位](https://leetcode.cn/problems/add-binary/description)

颠倒给定的 32 位无符号整数的二进制位。

**解法一**：循环

使用循环，每次1位，左移然后按位与。