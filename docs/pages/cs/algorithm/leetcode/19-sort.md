# 排序算法

## [33.搜索排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array)

难度：⭐️⭐️

整数数组 `nums` 按升序排列，数组中的值 互不相同 。

`在传递给函数之前，nums` 在预先未知的某个下标 `k（0 <= k < nums.length）`上进行了 旋转，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 从 0 开始 计数）。例如， `[0,1,2,4,5,6,7]` 在下标 3 处经旋转后可能变为 `[4,5,6,7,0,1,2]` 。

给你 旋转后 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

**解法一** 二分查找

## [34.排序数组中查找元素首尾位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array)

难度：⭐️⭐️

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

**解法一** 二分查找

二分查找到元素后，分别向左和向右搜索，直到找到第一个不想等的位置。也可以用2次二分查找。

<details>
  <summary>二分查找</summary>

  ```java
    public int[] searchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                left = mid;
                while(left > 0 && nums[left] == nums[left - 1]) {
                    left--;
                }
                right = mid;
                while(right < nums.length - 1 && nums[right] == nums[right + 1]) {
                    right++;
                }
                return new int[]{left, right};
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = right - 1;
            }
        }
        return new int[]{-1, -1};
    }
  ```
</details>

## [35.搜索插入的位置](https://leetcode.cn/problems/search-insert-position)

难度：⭐️

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

**解法一** 二分查找

<details>
  <summary>二分查找</summary>

  ```java
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
  ```
</details>

## [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/description)

难度：⭐️⭐️

给你一个满足下述两条属性的 `m x n` 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 `target` ，如果 `target` 在矩阵中，返回 `true` ；否则，返回 `false` 。

**解法一** 按行二分查找

按行遍历矩阵，对每一行进行二分查找。

<details>
  <summary>按行二分查找</summary>

  ```java
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int i = 0; i < matrix.length; i++) {
            if (binarySearch(matrix[i], target)) {
                return true;
            }
        }
        return false;
    }

    private boolean binarySearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target == nums[mid]) {
                return true;
            } else if (target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
  ```
</details>

**解法二** Z字形遍历

从右上或者左下开始遍历。

<details>
  <summary>Z字形遍历</summary>
  
  ```java
     public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int x = 0, y = n - 1;
        while (x < m && y >= 0) {
            if (matrix[x][y] == target) {
                return true;
            }
            if (matrix[x][y] < target) {
                x++;
            } else {
                y--;
            }
        }
        return false;
    }
  ```
</details>

## [153.寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array)

难度：⭐️⭐️⭐️

已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 旋转 后，得到输入数组。例如，原数组 `nums = [0,1,2,4,5,6,7]` 在变化后可能得到：
若旋转 4 次，则可以得到 `[4,5,6,7,0,1,2]`
若旋转 7 次，则可以得到 `[0,1,2,4,5,6,7]`
注意，数组 `[a[0], a[1], a[2], ..., a[n-1]]` 旋转一次 的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

**解法一** 二分查找

二分查找，右侧有序则向左搜索。

<details>
  <summary>二分查找</summary>

  ```java
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return nums[left];
    }
  ```

</details>