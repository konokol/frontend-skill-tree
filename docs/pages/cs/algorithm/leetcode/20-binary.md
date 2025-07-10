# 二分查找

## [162.寻找峰值](https://leetcode.cn/problems/find-peak-element/description)

峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 `nums[-1] = nums[n] = -∞` 。

你必须实现时间复杂度为 `O(log n)` 的算法来解决此问题。

 

示例 1：

输入：`nums = [1,2,3,1]`
输出：`2`
解释：`3` 是峰值元素，你的函数应该返回其索引 `2`。

示例 2：

输入：`nums = [1,2,1,3,5,6,4]`
输出：`1` 或 `5` 
解释：你的函数可以返回索引 `1`，其峰值元素为 `2`；
     或者返回索引 `5`， 其峰值元素为 `6`。

**解法一** 二分法 + 递归

将数组分成区间[i, j]取中间值mid，分3种情况讨论：

- mid 正好是峰值，直接返回
- num[mid - 1] > num[mid]，说明正在下坡，峰值一定在mid左边，递归查找区间[i, mid - 1]
- num[mid] < num[mid + 1]，说明正在上坡，峰值一定在mid右边，递归查找区间[mid + 1, j]

<details>
  <summary>二分法 + 递归</summary>

  ```java
    public int findPeakElement(int[] nums) {
        return peek(nums, 0, nums.length - 1);
    }

    private int peek(int[] nums, int start, int end) {
        if (start == end) {
            return start;
        } else if (start + 1 == end) {
            return nums[start] > nums[end] ? start : end;
        }
        int mid = start + (end - start) / 2;
        if (mid == 0) {
            return nums[mid] <= nums[mid + 1] ? -1 : mid;
        } else if (mid == nums.length - 1) {
            return nums[mid] > nums[mid - 1] ? mid : -1;
        } else {
            if (nums[mid - 1] < nums[mid] && nums[mid] > nums[mid + 1]) {
                return mid;
            } else if (nums[mid - 1] > nums[mid]) {
                return peek(nums, start, mid - 1);
            } else {
                return peek(nums, mid + 1, end);
            }
        }
    }
  ```
</details>