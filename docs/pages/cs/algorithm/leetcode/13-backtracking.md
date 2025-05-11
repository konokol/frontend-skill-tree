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

## [78.子集](https://leetcode.cn/problems/subsets/)

难度：⭐️⭐️⭐️⭐️

给你一个整数数组 `nums` ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

**解法一** 回溯

构建dfs(cur,n) 参数表示当前位置是 cur，原序列总长度为 n，cur位置的元素可以选中或不选中，根据该条件递归。

<details>
  <summary>回溯</summary>

  ```java
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> output = new LinkedList<>();
        backtrace(ans, output, nums, 0);
        return ans;
    }

    private void backtrace(List<List<Integer>> ans, List<Integer> output, int[] nums, int index) {
        if (index == nums.length) {
            ans.add(new ArrayList<>(output));
        } else {
            output.add(nums[index]);
            backtrace(ans, output, nums, index + 1);
            output.remove(output.size() - 1);
            backtrace(ans, output, nums, index + 1);
        }
    }
  ```
</details>

**解法二** 位运算

长度为n的数组，一共可以组成2^n个子数组，对于每一位数字，比特位是1认为使用该元素，0认为不使用。
