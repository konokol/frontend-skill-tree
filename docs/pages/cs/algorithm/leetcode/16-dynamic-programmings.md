# 动态规划

## [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs)

难度：⭐️

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**解法一** 动态规划

状态转移方程是一个斐波拉契数列，f(n) = f(n-1) + f(n-2)，其中f(0) = 0, f(1) = 1。

<details>
  <summary>斐波拉契数列</summary>
  
  ```java
    public int climbStairs(int n) {
        int l1 = 0;
        int l2 = 1;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum = l1 + l2;
            l1 = l2;
            l2 = sum;
        }
        return sum;
    }
  ```
</details>

## [118.杨辉三角](https://leetcode.cn/problems/pascals-triangle/description)

难度：⭐️

给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

![杨辉三角](../../../../img/pascal-triangle-animated2.gif)

**解法一** 动态规划

杨辉三角的每一列的元素满足条件`f(n)[i] = f(n - 1)[i] + f(n-1)[i-1]`，根据条件直接循环。

<details>
  <summary>动态规划</summary>

  ```java
    public List<List<Integer>> generate(int numRows) {
         List<List<Integer>> ans = new ArrayList<>(numRows);
         // f(n)[i] = f(n - 1)[i] + f(n-1)[i-1]
         for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>(i + 1);
            for (int j = 0; j < i + 1; j++) {
                if (j == 0 || j == i) {
                    row.add(1);
                } else {
                    List<Integer> last = ans.get(i - 1);
                    row.add(last.get(j) + last.get(j - 1));
                }
            }
            ans.add(row);
         }
         return ans;
    }
  ```
</details>

## [139.单词拆分](https://leetcode.cn/problems/word-break/description)

难度：⭐️⭐️⭐️

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 `s` 则返回 `true`。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

**解法一** 动态规划

dp[i]表示子串s[0, i]是否可以满足题设条件。状态转移方程为`dp[i] = dp[j] + dict.contains(s[j, i])`

<details>
  <summary>动态规划</summary>

  ```java
    public boolean wordBreak(String s, List<String> wordDict) {
        // dp[i] = dp[j] && wordDict.contains(s[j, i])
        Set<String> dict = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && dict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
  ```
</details>

## [198.打家劫舍](https://leetcode.cn/problems/house-robber/description)

难度：⭐️

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

**解法一** 动态规划

用dp[][]数组表示到第i家时，偷或者不偷可以偷盗到的最大值，答案为数组的最后一组值。

<details>
  <summary>二维数组</summary>

  ```java
    public int rob(int[] nums) {
        int[][] dp = new int[nums.length][2];
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                dp[i][0] = 0;
                dp[i][1] = nums[i];
            } else {
                dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
                dp[i][1] = dp[i - 1][0] + nums[i];
            }
        }
        int[] ans = dp[nums.length - 1];
        return Math.max(ans[0], ans[1]);
    }
  ```
</details>

用二维数组空间复杂度更高，可以精简空间，第i个位置，回溯到i-1和i-2的位置。

<details>
  <summary>一维数组</summary>

  ```java
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }
        return dp[nums.length - 1];
    }
  ```
</details>

基于上一种写法，还可以继续优化空间复杂度，只用2个int记录i-1和i-2的值。

<details>
  <summary>两个数字</summary>

  ```java
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        int last1 = nums[0];
        int last0 = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) {
            int temp = last0;
            last0 = Math.max(last1 + nums[i], last0);
            last1 = temp;
        }
        return last0;
    }
  ```
</details>

## [*279.完全平方数](https://leetcode.cn/problems/perfect-squares/description)

难度：⭐️⭐️⭐️

给你一个整数 `n` ，返回 **和** 为 `n` 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，`1`、`4`、`9` 和 `16` 都是完全平方数，而 `3` 和 `11` 不是。

**解法一**：动态规划

f[i]表示和为i的完全平方数的最小值，则计算f[i]需要从1遍历到√i，f[i]的最大值为i（1+1+...+1），遍历到位置j时，一定可以组成i的组合为 j * j + 1+1+...+1，因此状态转移方程为f[i] = min(j, f[i - j*j])

<details>
  <summary>动态规划</summary>

  ```java
    public int numSquares(int n) {
        int[] f = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int min = Integer.MAX_VALUE;
            for (int j = 1; j * j <= i; j++) {
                min = Math.min(min, f[i - j * j] + 1);
            }
            f[i] = min;
        }
        return f[n];
    }
  ```
</details>

## [*300.最长增长子序列](https://leetcode.cn/problems/longest-increasing-subsequence/description)

难度：⭐️⭐️⭐️

给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7] `是数组 `[0,3,1,6,2,2,7]` 的子序列。

**解法一** 动态规划

用dp[i]表示子数组nums[0,i]的答案，状态转移方程为`dp[i] = max(..., dp[j])`，其中需要满足`num[i] > nums[j]`。

<details>
  <summary>动态规划</summary>

  ```java
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 1;
        int ans = 1;
        for (int i = 1; i < nums.length; i++) {
            int max = 1;
            for(int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    max = Math.max(max, dp[j] + 1);
                }
            }
            dp[i] = max;
            ans = Math.max(ans, max);
        }
        return ans;
    }
  ```
</details>

**解法二** 贪心 + 二分查找

## [322.零钱兑换](https://leetcode.cn/problems/coin-change/description)

难度：⭐️⭐️⭐️

给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。

**解法一** 动态规划

用dp[i]表示`amount==i`的解，找到状态转移方程 `dp[i] = min(dp[i - coin[0]], ... , dp[i - coin[j]])`，注意特殊情况，dp[i]无解时，存-1

<details>
  <summary>动态规划</summary>

  ```java
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        dp[0] = 0;
        // dp[i] = min(dp[i - coins[j]] ...) + 1;
        for (int i = 1; i <= amount; i++) {
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] > i) {
                   continue; 
                }
                if (dp[i - coins[j]] < 0) {
                    continue;
                }
                min = Math.min(min, dp[i - coins[j]] + 1);
            }
            dp[i] = min == Integer.MAX_VALUE ? -1 : min;
        }
        return dp[amount];
    }
  ```

</details>

**解法二** 回溯



