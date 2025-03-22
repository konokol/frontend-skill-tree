# 数组/字符串

## [88.合并2个有序数组](https://leetcode.cn/problems/merge-sorted-array/description)

难度：难度：⭐️

给你两个按 非递减顺序 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 合并 `nums2` 到 `nums1` 中，使合并后的数组同样按 非递减顺序 排列。

**注意**：最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` `，应忽略。nums2` 的长度为 `n` 。

**解法一**  排序法 

第一次遍历把元素都移到num1的末尾，直接调用Arrays.sort(nums)排序。

<details>
  <summary>排序法</summary>
  ```java
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = 0; i < n; i++) {
            nums1[m + i] = nums2[i];
        }
        Arrays.sort(nums1);
    }
  ```
</details>

**解法二**  双指针

双指针，倒序遍历，每次将较大的放入数组中

<details>
  <summary>倒序双指针</summary>
  ```java
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = m + n - 1; i >= 0; i--) {
            if (n == 0) {
                break;
            }
            if (m > 0 && nums1[m - 1] > nums2[n - 1]) {
                nums1[i] = nums1[m - 1];
                m--;
            } else {
                nums1[i] = nums2[n - 1];
                n--;
            }
        }
    }
  ```
</details>

## [移除数组中指定元素](https://leetcode.cn/problems/remove-element/description/)

给你一个数组 `nums` 和一个值 `val`，你需要 原地 移除所有数值等于 `val` 的元素。元素的顺序可能发生改变。然后返回 `nums` 中与 `val` 不同的元素的数量。

**解法一** 2次循环直接移动  

**解法二**  快慢指针  
相等元素移动快指针，不同元素直接赋值。  

**解法三**  快慢指针优化，打乱顺序  
左右指针，元素相等时，将右指针上元素赋值给当前位置，右指针左移。

## [560. 和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k)

难度：⭐️⭐️

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

**解法一** 穷举

2层遍历，穷举所有的组合。

<details>
  <summary>2层遍历穷举法</summary>
  ```Java
  public int subarraySum(int[] nums, int k) {
        int ret = 0;
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum == k) {
                    ret++;
                }
            }
        }
        return ret;
    }
  ```

</details>


**解法二** 哈希表  

使用哈希表，key为前缀和，value为该前缀和的数量。遍历时，同时记录前缀和为某个值的数量。

<details>
  <summary>哈希表记录前缀和</summary>
  ```Java
  public int subarraySum(int[] nums, int k) {
        // <sum, count>
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int count = 0;
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
  ```

</details>