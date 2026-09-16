# 哈希表

## [49.字母异位词分组](https://leetcode.cn/problems/group-anagrams)

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。字母异位词 是由重新排列源单词的所有字母得到的一个新单词。 

示例 1: 

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"] 
输出: [["bat"],["nat","tan"],["ate","eat","tea"]] 

**解法一** 哈希表  

使用哈希表，key是重排序的后的单词，值是字母异位词分组的List。

<details>
  <summary>哈希表</summary>

  ```java
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new LinkedHashMap<>();
        for (String str : strs) {
            String key = genKey(str);
            List<String> list = map.get(key);
            if (list == null) {
                list = new LinkedList<>();
            }
            list.add(str);
            map.put(key, list);
        }
        return new ArrayList<>(map.values());
    }

    private int[] dict = new int[26];
    private String genKey(String str) {
        Arrays.fill(dict, 0);
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            dict[c - 'a']++;
        }
        StringBuilder builder = new StringBuilder();
        for(int i = 0; i < dict.length; i++) {
            if (dict[i] > 0) {
                builder.append('a' + i).append(dict[i]);
            }
        }
        return builder.toString();
    }
  ```
</details>
