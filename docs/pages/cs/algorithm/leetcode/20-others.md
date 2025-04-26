# 技巧题

## [31. 下一个排列](https://leetcode.cn/problems/next-permutation/description)

难度：⭐️⭐️⭐️

整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，`arr = [1,2,3]` ，以下这些都可以视作 arr 的排列：`[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1]` 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，`arr = [1,2,3]` 的下一个排列是 `[1,3,2]` 。
类似地，`arr = [2,3,1]` 的下一个排列是 `[3,1,2]` 。
而 `arr = [3,2,1]` 的下一个排列是 `[1,2,3]` ，因为 `[3,2,1]` 不存在一个字典序更大的排列。
给你一个整数数组 `nums` ，找出 `nums` 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。

**解法一** 两遍扫描

从后往前搜索，找到第一个降序序列，第二遍搜索，找到比顶点前一个元素小的元素，交换，将剩下的元素反转。

<details>
  <summary>两遍扫描</summary>

  ```java
    public void nextPermutation(int[] nums) {
        // 1 4 6 5 4 3 2 1
        int i = nums.length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[i] >= nums[j]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    private void reverse(int[] nums, int i) {
        int left = i;
        int right = nums.length - 1;
        while (left < right) {
            swap(nums, left, right);
            left++;
            right--;
        }
    }
  ```

</details>

## [75.颜色分类](https://leetcode.cn/problems/sort-colors/description)

难度：⭐️⭐️

给定一个包含红色、白色和蓝色、共 `n` 个元素的数组 `nums` ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 `0`、 `1` 和 `2` 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

**解法一** 双指针

左右指针分别指向头尾，遇到2移动到数组尾部，遇到0移动到数组头部。

<details>
  <summary>双指针</summary>

  ```java
    public void sortColors(int[] nums) {
        int p0 = 0;
        int p2 = nums.length - 1;
        for (int i = 0; i <= p2; i++) {
            while (i <= p2 && nums[i] == 2) {
                int temp = nums[p2];
                nums[p2] = nums[i];
                nums[i] = temp;
                p2--;
            }
            if (nums[i] == 0) {
                int temp = nums[p0];
                nums[p0] = nums[i];
                nums[i] = temp;
                p0++;
            }
        }
    }
  ```
</details>

**解法二** 记录次数

第一次循环计算每种颜色的数量，第二次循环根据数量分别设置值

<details>
  <summary>记录次数</summary>

  ```java
  public void sortColors(int[] nums) {
        int r = 0;
        int w = 0;
        int b = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                r++;
            } else if (nums[i] == 1) {
                w++;
            } else {
                b++;
            }
        }
        int rw = r + w;
        for (int i = 0; i < nums.length; i++) {
            if (i < r) {
                nums[i] = 0;
            } else if (i < rw) {
                nums[i] = 1;
            } else {
                nums[i] = 2;
            }
        }
    }

  ```
</details>

## [136.只出现一次的数字](https://leetcode.cn/problems/single-number)

难度：⭐️

给你一个 **非空** 整数数组 `nums` ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

**解法一** 异或

数字 n^n = 0，n^0 = n，将所有的数字异或一遍，结果就是只出现一次的数字。

<details>
  <summary>异或</summary>

  ```java
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int i = nums.length; i > 0; i--) {
            ans ^= nums[i-1];
        }
        return ans;
    }
  ```
</details>

## [169.多数元素](https://leetcode.cn/problems/majority-element)

难度：⭐️

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

**解法一** Boyer-Moore 投票算法

遍历数组，对每个数字进行投票，与自身数字相同的，票数+1，否则票数-1，票数归零后重新选择数字。则众数得到的票数一定>0。

<details>
  <summary>投票算法</summary>

  ```java
    public int majorityElement(int[] nums) {
        int candidate = nums[0];
        int votes = 1;
        for (int i = 1; i < nums.length; i++) {
            if (votes <= 0) {
                candidate = nums[i];
                votes++;
            } else if (nums[i] == candidate) {
                votes++;
            } else {
                votes--;
            }
        }
        return candidate;
    }
  ```
</details>

**解法二** 哈希表

对每个数字计数，取value最大的数。

<details>
  <summary>哈希表</summary>

  ```java
   public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() > nums.length / 2) {
                return entry.getKey();
            }
        }
        return -1;
    }
  ```
</details>

**解法三** 排序

对数组进行排序，排序后，最中间的位置一定是众数。

<details>
  <summary>排序</summary>

  ```java
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
  ```
</details>

**解法四** 分治递归

将数组分成两半，分别求两边的众数，两边众数相同时，结果即为该值；否则计算刚刚算出来的2个数组中的众数的数量，取数量更多的数组。递归该过程，当数组只有一个元素时，递归结束。

<details>
  <summary>排序</summary>

  ```java
    public int majorityElement(int[] nums) {
        return majority(nums, 0, nums.length);
    }

    private int majority(int[] nums, int start, int end) {
        if (end - start == 1) {
            return nums[start];
        }
        int mid = start + (end - start) / 2;
        int left = majority(nums, start, mid);
        int right = majority(nums, mid, end);
        if (left == right) {
            return left;
        }
        int leftCount = count(nums, start, end, left);
        int rightCount = count(nums, start, end, right);
        if (leftCount < rightCount) {
            return right;
        } else {
            return left;
        }

    }

    private int count(int[] nums, int start, int end, int target) {
        int count = 0;
        for (int i = start; i < end; i++) {
            if (nums[i] == target) {
                count++;
            }
        }
        return count;
    }
  ```
</details>
