# 二分查找

---

## [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position)

难度：⭐

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

**示例 1:**

> 输入: nums = [1,3,5,6], target = 5  
> 输出: 2

**示例 2:**

> 输入: nums = [1,3,5,6], target = 2  
> 输出: 1  

**示例 3:**

> 输入: nums = [1,3,5,6], target = 7  
> 输出: 4  
 
**提示:**

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- nums 为 **无重复元素** 的 **升序** 排列数组
- -10<sup>4</sup> <= target <= 10<sup>4</sup>

**解法一** 二分查找

经典的二分查找，找不到时，返回终态的 left 或者 right 值即可。

时间复杂度：O(logn)  
空间复杂度：O(1)  

<details>
<summary>二分查找</summary>

```java
     public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid;
        while (left <= right) {
            mid = (right + left) >> 1;
            if (nums[mid] == target) {
                return mid;
            } else if (target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
```
</details>

---

## [162.寻找峰值](https://leetcode.cn/problems/find-peak-element)

峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。

你可以假设 `nums[-1] = nums[n] = -∞` 。

你必须实现时间复杂度为 `O(log n)` 的算法来解决此问题。

示例 1：

> 输入：`nums = [1,2,3,1]`  
> 输出：`2`  
> 解释：`3` 是峰值元素，你的函数应该返回其索引 `2`。

示例 2：

> 输入：`nums = [1,2,1,3,5,6,4]`  
> 输出：`1` 或 `5`   
> 解释：你的函数可以返回索引 `1`，其峰值元素为 `2`；
     或者返回索引 `5`， 其峰值元素为 `6`。

**解法一** 二分法 + 递归

将数组分成区间 [i, j] 取中间值mid，分3种情况讨论：

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
