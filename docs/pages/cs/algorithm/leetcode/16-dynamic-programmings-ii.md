# 多维动态规划

## [62. 不同路径](https://leetcode.cn/problems/unique-paths/description)

难度：⭐️⭐️

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

![](../../../../img/adxmsI-image.png)

**解法一** 动态规划

由于只能向右和向下走，很容易找到状态转移方程 `dp[i][j] = dp[i - 1][j] + dp[i][j - 1]`，注意考虑边界情况。

<details>
  <summary>动态规划</summary>

  ```java
      public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        dp[0][0] = 1;
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i - 1][0];
        }
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j - 1];
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
            }
        }
        return dp[m - 1][n - 1];
    }
  ```
</details>

