# 哈希表

--- 

## [49.字母异位词分组](https://leetcode.cn/problems/group-anagrams)

难度：⭐️⭐️⭐️

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。**字母异位词** 是由重新排列源单词的所有字母得到的一个新单词。 

> 示例 1: 

> 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]   
> 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]   

**解法一** 哈希表  

使用哈希表，key是重排序的后的单词，值是字母异位词分组的List。

时间复杂度：O(nklogk)  
空间复杂度：O(nk)

<details>
  <summary>哈希表</summary>

  ```java
  class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for (String str: strs) {
            String key = getKey(str);
            if (result.containsKey(key)) {
                result.get(key).add(str);
            } else {
                List<String> arr = new ArrayList<>();
                arr.add(str);
                result.put(key, arr);
            }
        }
        return new ArrayList<>(result.values());
    }

    private String getKey(String str) {
        char[] ch = str.toCharArray();
        Arrays.sort(ch);
        return new String(ch);
    }
   }
   ```
</details>

---

## [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence)

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

**示例 1：**

> 输入：nums = [100,4,200,1,3,2]  
> 输出：4  
> 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。  

**示例 2：**

> 输入：nums = [0,3,7,2,5,8,4,6,0,1]  
> 输出：9  

**示例 3：**

> 输入：nums = [1,0,1,2]  
> 输出：3  

**提示：**

- 0 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

**方法一**：哈希表

使用哈希表实现重复元素滤重，遍历哈希表，当值 n+1 也在哈希表中时，说明是连续的，开始循环，直到找到不在哈希表中的元素，即为当前元素。

*注意*

- 遍历的是哈希表，不要遍历原数组，否则当原数组中存在大量重复元素时会超时。
- 内层循环开始计算长度时，先判断一下是否是连续序列的第一个元素，否则会存在大量的重复循环，比如 1..10000，如果不加这个判断，会多出来9999次无用的判断。

时间复杂度：O(n)  
空间复杂度：O(n)  

<details>
<summary>哈希表去重</summary>

```java
class Solution {

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
            if (!set.contains(num - 1)) { // 连续序列的第一个元素才计数
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
}
```
</details>

**方法二**：排序

对数组排序，循环记录当次连续的长度。注意当相邻元素相等时，不计长度。可以用两个指针，也可以用哈希表。

用哈希表时：

时间复杂度：O(nlogn)  
空间复杂度：O(n)  

<details>
<summary>排序 + 哈希表</summary>

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        int max = 0;
        Set<Integer> set = new HashSet<>();
        Arrays.sort(nums);
        int curMax = 1;
        for (int n: nums) {
            if (!set.contains(n - 1)) {
                curMax = 1;
            } else if (!set.contains(n)){
                curMax++;
            }
            max = Math.max(curMax, max);
            set.add(n);
        }
        return max;
    }
}

```
</details>

用双指针时(耗时最短的解法)：

时间复杂度：O(nlogn)  
空间复杂度：O(1) 

<details>
<summary>排序 + 双指针</summary>

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length < 2) {
            return nums.length;
        }
        Arrays.sort(nums);
        int max = 1;
        int length = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                continue;
            } else if (nums[i] == nums[i - 1] + 1) {
                length++;
            } else {
                max = Math.max(max, length);
                length = 1;
            }
        }
        return Math.max(max, length);
    }
}
```
</details>
