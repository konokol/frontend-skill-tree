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

### [560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k)

难度：⭐️⭐️

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

**解法一**：穷举

2层遍历，穷举所有的组合。

<details>
  <summary>2层遍历穷举法</summary>
  ```Java
  public int subarraySum(int[] nums, int k) {
        int ret = 0;
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum == k) {
                    ret++;
                }
            }
        }
        return ret;
    }
  ```

</details>


**解法二**：哈希表  

使用哈希表，key为前缀和，value为该前缀和的数量。遍历时，同时记录前缀和为某个值的数量。

<details>
  <summary>哈希表记录前缀和</summary>
  ```Java
  public int subarraySum(int[] nums, int k) {
        // <sum, count>
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int count = 0;
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
  ```

</details>


## 链表

### [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/description/)

难度：⭐️

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**解法一**：迭代

直接循环，将指针每次都指向较小的节点。

**解法二**：递归

比较头结点，较小的节点的next作为一个子链表，递归和另一个链表比，返回较小节点。其中一个节点为空时，返回另一个节点，递归中止。

## 哈希表

### [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams)

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。字母异位词 是由重新排列源单词的所有字母得到的一个新单词。 

示例 1: 

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"] 
输出: [["bat"],["nat","tan"],["ate","eat","tea"]] 

**解法** 哈希表  
使用哈希表，key是重排序的后的单词，值是字母异位词分组的List。

### [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence)

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

**方法一**：哈希表

使用哈希表实现重复元素滤重，遍历哈希表，当值n+1也在哈希表中时，说明是连续的，开始循环，直到找到不在哈希表中的元素，即为当前元素。


<details>
  <summary>哈希表去重法</summary>
  ```java
  public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        // 先去重
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }
        int max = 1;
        for (Integer num : set) {
            // 不连续，从最小开始往上数
            if (!set.contains(num - 1)) {
                int curMax = 1;
                int it = num;
                while (set.contains(it + 1)) {
                    curMax++;
                    it++;
                }
                max = Math.max(max, curMax);
            }
        }
        return max;
    }
  ```
</details>


**方法二**：排序

对数组排序，循环记录当次连续的长度。注意当相邻元素相等时，不计长度。

### [205. 同构字符串](https://leetcode.cn/problems/isomorphic-strings)

给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。  
如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。  
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。 

**解法** 哈希表  
使用2个Hash表分别存s->t和t-s的映射，遍历检查正反都能隐射上。

### [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram)

给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。

**解法一** 哈希表  
使用哈希表，key是字符，value是字符出现的次数。2次遍历，第一次向哈希表中插值，第二次从哈希表中删值。哈表表如果被清空，说明字符串是字母异位词。

**解法二** 排序
先对字符串排序，按序排的字符一样，说明字符串是字母异位词。

### [290. 单词规律](https://leetcode.cn/problems/word-pattern)

给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。  
这里的 “遵循” 指完全匹配，例如， `pattern` 里的每个字母和字符串 `s` 中的每个非空单词之间存在着双向连接的对应规律。

**解法** 哈希表  
和同构字符串的解法一样，也是用2个哈希表。


## 栈

### [71. 简化路径](https://leetcode.cn/problems/simplify-path/description)

给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为 更加简洁的规范路径。  

在 Unix 风格的文件系统中规则如下：

- 一个点 '.' 表示当前目录本身。
- 此外，两个点 '..' 表示将目录切换到上一级（指向父目录）。
- 任意多个连续的斜杠（即，'//' 或 '///'）都被视为单个斜杠 '/'。
- 任何其他格式的点（例如，'...' 或 '....'）均被视为有效的文件/目录名称。

返回的 简化路径 必须遵循下述格式： 

- 始终以斜杠 '/' 开头。
- 两个目录名之间必须只有一个斜杠 '/' 。
- 最后一个目录名（如果存在）不能 以 '/' 结尾。
- 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。

返回简化后得到的 规范路径 。

**解法** 栈 

使用栈，题目中输入都是合法的路径，根据 `/` 分割字符串，遇到 `..` 出栈一次，遇到 `.` 则不做任何处理，其他情况都入栈，最后将栈中字符用 `/` 拼接起来。

需要注意的点是，栈中只存路径名，不存分隔符，能简化很多逻辑。

## 堆

## 树

### [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view)

给定一个二叉树的根节点 `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**解法一** 

使用层次遍历，记录最右边的节点。

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


### [530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst)

给你一个二叉搜索树的根节点 `root` ，返回 树中任意两不同节点值之间的最小差值。差值是一个正数，其数值等于两值之差的绝对值。

**解法**

中序遍历二叉搜索树，序列一定是升序的，所以只需要记录遍历的前一个节点即可。 

二叉搜索树遍历有3种方法：  

- 递归，先遍历左子树，读当前节点，再次遍历右节点。
- 栈，先将左子树全入栈，读当前节点，再将右节点入栈。
- Morris遍历

## 图

## 双指针

### [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water)  

难度：⭐️⭐️

给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

![例子](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg "aaa")

**解法一**：双指针  

左右指针像中间靠拢，取 最小高度 * 指针差值 为当次的最大面积。

<details>
  <summary>
    左右双指针
  </summary>
  ```Java
    public int maxArea(int[] height) {
        int max = 0;
        int left = 0;
        int right = height.length - 1;
        while (left < right) {
            int sum;
            if (height[left] < height[right]) {
                max = Math.max(max, height[left] * (right - left));
                left++;
            } else {
                max = Math.max(max, height[right] * (right - left));
                right--;
            }
        }
        return max;
    }
  ```
</details>

### [15. 三数之和](https://leetcode.cn/problems/3sum)  

难度：难度：⭐️⭐️⭐️

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

**解法一**：双指针

先排序，从头遍历，跳过重复的元素，从第i个位置开始，将区间[i+1, nums.length - 1]内的问题转换成有序数组的两数之和问题。难点在于去重，找到满足条件的📚之后，左右都要跳过相同的数。

<details>
  <summary> 双指针法 </summary>
  ```Java
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) continue;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sum = nums[left] + nums[right] + nums[i];
                if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                } else {
                    List<Integer> arr = new ArrayList<>();
                    arr.add(nums[i]);
                    arr.add(nums[left]);
                    arr.add(nums[right]);
                    ans.add(arr);
                    left++;
                    right--;
                    // 去重
                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                }
            }
        }
        return ans;
    }
  ```
</details>

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