# 贪心算法

## [45.跳跃游戏II](https://leetcode.cn/problems/partition-labels/description)

难度：⭐️⭐️⭐️

给定一个长度为 `n` 的 `0` 索引整数数组 `nums`。初始位置为 `nums[0]`。

每个元素 `nums[i]` 表示从索引 `i` 向后跳转的最大长度。换句话说，如果你在 `nums[i]` 处，你可以跳转到任意 `nums[i + j]` 处:

- 0 <= j <= nums[i] 
- i + j < n
  
返回到达 `nums[n - 1]` 的最小跳跃次数。生成的测试用例可以到达 `nums[n - 1]`。

**解法一** 正向查找

贪心算法，记录每次可以到达的最远位置，记为边界，从左往右遍历，遇到边界，次数+1。注意只需要遍历到n-1的位置。

<details>
  <summary>正向查找</summary>

  ```java
    public int jump(int[] nums) {
        int max = 0;
        int step = 0;
        int end = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            max = Math.max(nums[i] + i, max);
            if (i == end) {
                step++;
                end = max;
            }
        }
        return step;
    }
  ```
</details>


## [55.跳跃游戏](https://leetcode.cn/problems/jump-game/description)

难度：⭐️⭐️

给你一个非负整数数组 `nums` ，你最初位于数组的 **第一个下标** 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 `true` ；否则，返回 `false` 。

**解法一** 贪心算法

记录可以到达的最远的距离，如果最远的距离小于当前位置，说明当前位置不可达，返回false。否则更新最远位置。

<details>
  <summary>贪心</summary>

  ```java
    public boolean canJump(int[] nums) {
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (max < i) {
                return false;
            }
            max = Math.max(max, nums[i] + i);
        }
        return true;

    }
  ```
</details>

## [121.买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description)

难度：⭐️⭐️

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

**解法一** 贪心

由于只能买卖一次，只需要找到一个递增数列，最大值为递增数列的首尾差。采用一次遍历的方式，每一天只能买入和卖出，一次遍历，当前元素比最小值小，最小值记为当前元素，即买入价格。否则，当天卖出，计算卖出的最大利润。

<details>
  <summary>贪心</summary>

  ```java
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] <= min) {
                min = prices[i];
            } else {
                maxProfit = Math.max(maxProfit, prices[i] - min);
            }
        }
        return maxProfit;
    }
  ```

</details>
