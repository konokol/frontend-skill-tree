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

## [347.前K个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/description)

难度：⭐️⭐️

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

**解法一** 哈希表 + 优先级队列

使用哈希表保存每个元素出现的次数，遍历加入到优先级队列中，取优先级队列中前K个元素。

<details>
  <summary>哈希表+优先级队列</summary>

  ```java
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        Queue<int[]> queue = new PriorityQueue<>((int[] a, int[] b) -> {
            return a[1] - b[1];
        });
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            if (queue.size() < k) {
                queue.offer(new int[] {num, count});
            } else if (count > queue.peek()[1]) {
                queue.poll();
                queue.offer(new int[] {num, count});
            }
        }
        int[] ans = new int[k];
        for (int i = k; i > 0; i--) {
            ans[i - 1] = queue.poll()[0];
        }
        return ans;
    }
  ```
</details>
