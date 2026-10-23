# 哈希表

--- 

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
