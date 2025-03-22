# 滑动窗口

[3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters)

难度：⭐️⭐️⭐️

给定一个字符串 s ，请你找出其中不含有重复字符的 **最长** 子串 的长度。

**解法一：** 滑动窗口 + 哈希表

使用Set保存遍历过的的字符，再用快慢指针分别记录子串的头和尾，遇到重复的字符后，慢指针往右走直到无重复字符。

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

