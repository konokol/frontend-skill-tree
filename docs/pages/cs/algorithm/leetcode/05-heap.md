# 堆

## [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array);

难度：⭐️⭐️⭐️

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

**解法一** 快排

直接使用快排，时间复杂度是O(nlogn)，为了减少额外排序的次数，增加一个参数k，每次分割，只排k所在区间的数。

<details>
  <summary>快排</summary>

  ```java
    public int findKthLargest(int[] nums, int k) {
        return quickSort(nums, 0, nums.length - 1, nums.length - k);
    }

    private int quickSort(int[] nums, int left, int right, int k) {
        if (left >= right) {
            return nums[k];
        }
        int i = left - 1;
        int j = right + 1;
        int povit = nums[left + (right - left) / 2];
        while (i < j) {
            do { i++; } while (nums[i] < povit);
            do { j--; } while (povit < nums[j]);
            if (i < j) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
        if (k <= j) {
            return quickSort(nums, left, j, k);
        } else {
            return quickSort(nums, j + 1, right, k);
        }
    }
  ```

</details>
