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

---

## [202. 快乐数](https://leetcode.cn/problems/happy-number)

难度：⭐⭐

编写一个算法来判断一个数 `n` 是不是快乐数。

「快乐数」 定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
- 如果这个过程 结果为 1，那么这个数就是快乐数。

如果 `n` 是 **快乐数** 就返回 `true` ；不是，则返回 `false` 。

**示例 1：**

> 输入：n = 19  
> 输出：true  
> 解释：  
> 1<sup>2</sup> + 9<sup>2</sup> = 82  
> 8<sup>2</sup> + 2<sup>2</sup> = 68  
> 6<sup>2</sup> + 8<sup>2</sup> = 100  
> 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1  

**示例 2：**

> 输入：n = 2  
> 输出：false  

**提示：**

- 1 <= n <= 2<sup>31</sup> - 1

**解法一** 哈希表

计算每个每个位数上平方和，存在哈希表中，下次遍历如果哈希表中存在元素，说明有环不是快乐数。

时间复杂度：O(n)  
空间复杂度：O(n)  

<details>
<summary>哈希表</summary>

```java
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();

        while (true) {
            if (n == 1) {
                return true;
            }
            if (set.contains(n)) {
                return false;
            }
            set.add(n);
            int value = 0;
            while (n > 0) {
                int d = n % 10;
                n = n / 10;
                value += d * d;
            }
            if (value == 1) {
                return true;
            }
            
            n = value;
        }
    }
}
```
</details>

**解法二** 快慢指针（Floyd 判圈法）

和判断链表是否成环思路一样，计算每个位数的平方和，慢指针每次只算一次，快指针算两次，当快慢指针相等了，说明有环。比方法一更省内存。

时间复杂度：O(n)  
空间复杂度：O(1)  

<details>
<summary>快慢指针</summary>

```java
class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;
        while (true) {
            int next = next(fast);
            if (fast == 1 || next == 1) {
                return true;
            }
            slow = next(slow);
            fast = next(next);
            if (slow == fast) {
                return false;
            }
        }
    }

    private int next(int n) {
        int next = 0;
        while (n > 0) {
            int d = n % 10;
            n = n / 10;
            next += d * d;
        }
        return next;
    }
}
```
</details>

---

## [205. 同构字符串](https://leetcode.cn/problems/isomorphic-strings)

难度：⭐️

给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。  
如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。  
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。 

**解法** 哈希表  
使用 2 个 Hash 表分别存 s->t 和 t-s 的映射，遍历检查正反都能映射上。

时间复杂度：O(n)  
空间复杂度：O(n)  

<details>
<summary>快慢指针</summary>

```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Character> s2t = new HashMap<>();
        Map<Character, Character> t2s = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char sc = s.charAt(i);
            char tc = t.charAt(i);
            if ((s2t.containsKey(sc) && s2t.get(sc) != tc)) {
                return false;
            }
            if (t2s.containsKey(tc) && t2s.get(tc) != sc) {
                return false;
            }
            s2t.put(sc, tc);
            t2s.put(tc, sc);
        }

        return true;
    }
}
```
</details>

---

### [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram)

难度：⭐️

给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。

**示例 1:**

> 输入: s = "anagram", t = "nagaram"  
> 输出: true  

**示例 2:**

> 输入: s = "rat", t = "car"  
> 输出: false  
 

**提示:**

- 1 <= s.length, t.length <= 5 * 10<sup>4</sup>
- s 和 t 仅包含小写字母

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

**解法一** 哈希表  
使用哈希表，key是字符，value是字符出现的次数。2次遍历，第一次向哈希表中插值，第二次从哈希表中删值。哈表表如果被清空，说明字符串是字母异位词。由于题目中只包含小写字母，可以用 `int[26]` 来当哈希表。

如果扩展到 Unicode 字符集，可以用 `HashMap` 存。

时间复杂度：O(n)  
空间复杂度：O(S)，S 为字符集的大小

<details>
<summary>快慢指针</summary>

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] map = new int[26];
        for (char c: s.toCharArray()) {
            map[c - 'a']++;
        }
        for (char c: t.toCharArray()) {
            map[c - 'a']--;
            if (map[c - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
}
```
</details>

**解法二** 排序

先对字符串排序，按序排的字符一样，说明字符串是字母异位词。

时间复杂度：O(nlogn)  
空间复杂度：O(logn)  
