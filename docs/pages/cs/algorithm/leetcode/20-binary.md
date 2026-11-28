# 二分查找

---

## [4.寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays)

难度：⭐️⭐️⭐️⭐️

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log (m+n))` 。

**示例 1：**

> 输入：nums1 = [1,3], nums2 = [2]  
> 输出：2.00000  
> 解释：合并数组 = [1,2,3] ，中位数 2  

**示例 2：**

> 输入：nums1 = [1,2], nums2 = [3,4]  
> 输出：2.50000  
> 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5  

**提示：**

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10<sup>6</sup> <= nums1[i], nums2[i] <= 10<sup>6</sup>

**解法一** 合并数组（时间复杂度不符合要求）

并不是真正合并两个数组，只是不断比较，然后找到中间位置，同时在遍历的过程中，记录 2 个数。最终根据奇偶用记录的 2 个数来计算中位数。

时间复杂度：O(m + n)  
空间复杂度：O(1)  

<details>

<summary>合并</summary>

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int mid = (m + n) / 2;
        int index = 0;
        int i = 0;
        int j = 0;
        int[] value = new int[] { Integer.MAX_VALUE, Integer.MAX_VALUE };
        while (index < mid + 1) {
            int cur = Integer.MAX_VALUE;
            if (i < m && j < n) {
                if (nums1[i] < nums2[j]) {
                    cur = nums1[i++];
                } else {
                    cur = nums2[j++];
                }
            } else if (i >= m) {
                cur = nums2[j++];
            } else {
                cur = nums1[i++];
            }
            value[0] = value[1];
            value[1] = cur;
            index++;
        }
        if ((m + n) % 2 == 0) {
            return (value[0] + value[1]) / 2D;
        } else {
            return (double)value[1];
        }
    }
}
```

</details>

**解法二** 二分查找

中位数把两个数组划分成两段，左半长度 == 右半长度（或者左半多一个元素）。只需要找到两个数组上的划分点 `i` 和 `j`，使得：

- nums1[0..i-1] 和 nums2[0..j-1] 组成左半段
- nums1[i..m-1] 和 nums2[j..n-1] 组成右半段
- i + j = (m + n + 1) / 2，即两端的长度一样
- `nums1[i-1] <= nums2[j]` 且 `nums2[j-1] <= nums1[i]`，即左半段的最大值要小于右半段的最小值（同一个数组都是有序的，因此只需要比较另一个数组）

根据以上条件，使用二分查找，不断缩小区间，找到满足条件的分割点。

找到分割点后，中位数在分割点附近的 4 个区间断点中，根据奇偶划分即可。

小技巧：注意到左边区间可能多一个元素，注意初始i的右边界是m。由于区间端点需要比大小，如果 i 或 j 超出了数组范围，用 Integer.MIN_VALUE 和 Integer.MAX_VALUE 来当做超出区间的值，能少写很多比较条件。

时间复杂度：O(log min(m, n))  
空间复杂度：O(1)  

<details>

<summary>二分查找</summary>

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int m = nums1.length;
        int n = nums2.length;
        // 左：nums1[0..i-1] + nums2[0..j-1]
        // 右：nums1[i..m-1] + nums2[j..n-1]

        // nums2[j-1] < num1[i] && num1[i-1] < nums2[j]
        int half = (m + n + 1) / 2;
        int left = 0;
        int right = m;
        while (left <= right) {
            // i + j = half
            int i = left + (right - left) / 2;
            int j = half - i;

            int nums1Left = i <= 0 ? Integer.MIN_VALUE : nums1[i - 1];
            int nums1Right = i >= m ? Integer.MAX_VALUE : nums1[i];
            int nums2Left = j <= 0 ? Integer.MIN_VALUE : nums2[j - 1];
            int nums2Right = j >= n ? Integer.MAX_VALUE: nums2[j];

            if (nums1Left > nums2Right) {
                // i 太大
                right = i - 1;
            } else if (nums1Right < nums2Left) {
                // i 太小
                left = i + 1;
            } else {
                int maxLeft = Math.max(nums2Left, nums1Left);
                int minRight = Math.min(nums1Right, nums2Right);
                if ((m + n) % 2 == 0) {
                    return (maxLeft + minRight) / 2D;
                } else {
                    return (double)maxLeft;
                }
            }
        }
        return -1D;

    }
}
```

</details>

---

## [35.搜索插入位置](https://leetcode.cn/problems/search-insert-position)

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

难度：⭐️⭐️⭐️

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
