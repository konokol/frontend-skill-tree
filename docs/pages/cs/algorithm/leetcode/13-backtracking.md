# 回溯

## [46.全排列](https://leetcode.cn/problems/permutations/description)

难度：⭐️⭐️⭐️⭐️

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

**解法一** 回溯

定义递归函数 backtrack(first,output) 表示从左往右填到第 first 个位置，当前排列为 output。first左边是已经填充的数，右边是未填充的。小技巧，用元素交换的方式来做标记数组。

<details>
  <summary>回溯</summary>

  ```java
    private List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        List<Integer> output = new ArrayList<>();
        for (int num : nums) {
            output.add(num);
        }
        backtrace(nums.length, output, 0);
        return ans;
    }

    private void backtrace(int n, List<Integer> output, int first) {
        if (first == n) {
            ans.add(new ArrayList<>(output));
        }
        for (int i = first; i < n; i++) {
            Collections.swap(output, first, i);
            backtrace(n, output, first + 1);
            Collections.swap(output, first, i);
        }
    }
  ```
</details>

