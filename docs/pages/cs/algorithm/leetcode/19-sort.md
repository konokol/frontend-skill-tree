# 排序算法

## [34.在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array)

难度：⭐️⭐️

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

**解法一** 二分查找

二分查找到元素后，分别向左和向右搜索，直到找到第一个不想等的位置。

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
