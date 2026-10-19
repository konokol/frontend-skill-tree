# 滑动窗口

---

## [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters)

难度：⭐️⭐️⭐️

给定一个字符串 s ，请你找出其中不含有重复字符的 **最长** 子串 的长度。

**解法一：** 滑动窗口 + 哈希表

使用Set保存遍历过的的字符，再用快慢指针分别记录子串的头和尾，遇到重复的字符后，慢指针往右走直到无重复字符，无重复子串则走快指针。注意判断条件是 `slow < fast`。

<details>
  <summary>滑动窗口</summary>

  ```java
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int slow = 0;
        int fast = 0;
        int max = 0;
        while (slow <= fast && fast < s.length()) {
            char s2 = s.charAt(fast);
            char s1;
            if (set.contains(s2)) {
                do {
                    s1 = s.charAt(slow);
                    set.remove(s1);
                    slow++;
                } while (s1 != s2);
            } else {
                fast++;
                set.add(s2);
            }
            max = Math.max(max, fast - slow);
        }
        return max;
    }
  ```
</details>

---

## [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring)

难度：⭐️⭐️⭐️

给定两个字符串 `s` 和 `t`，长度分别是 `m` 和 `n`，返回 `s` 中的 **最短窗口** 子串，使得该子串包含 `t` 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 `""`。

测试用例保证答案唯一。

**示例 1：**

> 输入：s = "ADOBECODEBANC", t = "ABC"  
> 输出："BANC"  
> 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

**示例 2：**

> 输入：s = "a", t = "a"  
> 输出："a"  
> 解释：整个字符串 s 是最小覆盖子串。

**示例 3:**

> 输入: s = "a", t = "aa"  
> 输出: ""  
> 解释: t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。
 
**提示：**

- m == s.length
- n == t.length
- 1 <= m, n <= 10<sup>5</sup>
- s 和 t 由英文字母组成

**解法一：**滑动窗口 + 哈希表

使用哈希表分别记录每个字符出现的频率，在更新滑动窗口的过程中遍历两个集合判断是否满足条件，如果满足条件，尝试压缩滑动窗口的左边界。

时间复杂度：O(nm)  
空间复杂度：O(m + C)，C 是字符集的大小

<details>
  <summary>哈希表</summary>

```java
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }
        Map<Character, Integer> dict = new HashMap<>();
        Map<Character, Integer> subDict = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            dict.put(c, dict.getOrDefault(c, 0) + 1);
        }
        int left = 0;
        int right = 0;
        int rl = 0;
        int rr = Integer.MAX_VALUE;
        while (right < s.length()) {
            char rc = s.charAt(right);
            subDict.put(rc, subDict.getOrDefault(rc, 0) + 1);
            while (contains(dict, subDict)) {
                char lc = s.charAt(left);
                subDict.put(lc, subDict.getOrDefault(lc, 1) - 1);
                if (rr - rl > right - left) {
                    rl = left;
                    rr = right;
                }
                left++;
            }
            right++;
        }
        if (rr - rl > s.length()) {
            return "";
        } else {
            return s.substring(rl, rr + 1);
        }
    }

    private boolean contains(Map<Character, Integer> dict, Map<Character, Integer> subDict) {
        for (Map.Entry<Character, Integer> entry : dict.entrySet()) {
            Character c = entry.getKey();
            int count = entry.getValue();
            int subCount = subDict.getOrDefault(c, 0);
            if (count > subCount) {
                return false;
            }
        }
        return true;
    }
}
```
</details>

**解法二：**滑动窗口 + 数组

解法一中，每移动一个字符都需要计算整个集合是否匹配，这部分可以优化成常数级。用一个 `int[]` 来记录字符的频率，同时统计 `t` 中字符种类，用一个变量表示共有多少个字符已经满足了条件，滑动窗口中，对于遍历到的字符，如果是 `t` 中的字符，把频次增加。当所有的字符都满足频次后，尝试缩小滑动窗口的左边界。

*这个解法中，也可以直接基于解法一，用哈希表存字符频率，但是由于存在装箱的开销，实际执行的时间不如数组*

时间复杂度：O(n + m)  
空间复杂度：O(m + C)，C 是字符集的大小

<details>
  <summary>数组</summary>

```java
class Solution {
    public String minWindow(String s, String t) {
        int m = s.length();
        int n = t.length();
        if (m < n) return "";

        int[] need = new int[128];
        int[] window = new int[128];
        for (char c : t.toCharArray()) {
            need[c]++;
        }
        int required = 0;
        for (int i: need) {
            if (i > 0) required++;
        }

        int min = m + 1;
        int minStart = 0;
        int start = 0;
        int end = 0;
        int formed = 0;
        while (end < m) {
            char c = s.charAt(end);
            window[c]++;
            if (need[c] > 0 && window[c] == need[c]) {
                formed++;
            }
            for (;start <= end && formed == required; start++) {
                if (end - start + 1 < min) {
                    min = end - start + 1;
                    minStart = start;
                }
                c = s.charAt(start);
                window[c]--;
                if (need[c] > 0 && window[c] < need[c]) {
                    formed--;
                }
            }
            end++;
        }
        if (min == m + 1) {
            return "";
        } else {
            return s.substring(minStart, minStart + min);
        }
    }
}
```
</details>

---

## [239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum) 

难度：⭐️⭐️⭐️⭐️

给你一个整数数组 `nums`，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

**解法一** 优先级队列

优先级队列保存滑动窗口的元素，优先级队列的元素是一个int数组，第一位保存数值，第二位保存下标。滑动窗口中，找到值最大的元素，值相同的看下标最大的。

<details>
  <summary>优先级队列</summary>

  ```java
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] result = new int[nums.length - k + 1];
        PriorityQueue<int[]> queue = new PriorityQueue<>((int[] p, int[] q) -> {
            return p[0] != q[0] ? q[0] - p[0] : q[1] - p[1];
        });
        for (int i = 0; i < k; i++) {
            queue.offer(new int[] { nums[i], i });
        }
        result[0] = queue.peek()[0];
        for (int i = k; i < nums.length; i++) {
            queue.offer(new int[] { nums[i], i});
            while (queue.peek()[1] <= i - k) {
                queue.poll();
            }
            result[i - k + 1] = queue.peek()[0];
        }
        return result;
    }
  ```
</details>

---

## [438. 字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string)

难度：⭐️⭐️⭐️

给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

**解法一** 滑动窗口

在长度为n的子串内，使用数组记录子串中每个字符出现的次数，和p中字符出现的次数做对比。需要注意的记录字符串出现的次数用长度为26的数组，用哈希表会超时。

<details>
  <summary>滑动窗口</summary>

  ```java 
        public List<Integer> findAnagrams(String s, String p) {
            List<Integer> result = new ArrayList<>();
            if (s.length() < p.length()) {
                return result;
            }
            int[] dict = new int[26];
            for (int i = 0; i < p.length(); i++) {
                char c = p.charAt(i);
                dict[c - 'a'] = dict[c - 'a'] + 1;
            }
            int[] subDict = new int[26];
            for (int i = 0; i < s.length() - p.length() + 1; i++) {
                Arrays.fill(subDict, 0);
                for (int j = 0; j < p.length(); j++) {
                    char c = s.charAt(i + j);
                    subDict[c - 'a'] = subDict[c - 'a'] + 1;
                }
            
                boolean eq = true;
                for (int j = 0; j < 26; j++) {
                    if (dict[j] != subDict[j]) {
                        eq = false;
                        break;
                    }
                }
                if (eq) {
                    result.add(i);
                }
            }
            return result;
        }
    ```
</details>

