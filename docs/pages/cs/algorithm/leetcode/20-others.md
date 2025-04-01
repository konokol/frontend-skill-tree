# 技巧题

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