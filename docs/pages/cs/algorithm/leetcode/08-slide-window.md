# 滑动窗口

## [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters)

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

## [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string)

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
