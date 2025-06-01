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

## [64.最小路径和](https://leetcode.cn/problems/minimum-path-sum/description)

给定一个包含非负整数的 `m x n` 网格 `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

[](../../../../img/minpath.jpg)

**解法一** 动态规划

和62的解法相同，只需要记录上一步的最小值即可。

<details>
  <sumamry>动态规划</summary>

  ```java
  
  ```

</details>

## [1143.最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/description)

难度：⭐️⭐️⭐️

给定两个字符串 `text1` 和 `text2`，返回这两个字符串的最长 **公共子序列** 的长度。如果不存在 **公共子序列** ，返回 `0` 。

一个字符串的 **子序列** 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

- 例如，`"ace"` 是 `"abcde"` 的子序列，但 `"aec"` 不是 `"abcde"` 的子序列。
- 
两个字符串的 **公共子序列** 是这两个字符串所共同拥有的子序列。

**解法一** 动态规划

定义二维数组dp[][]，`dp[i][j]` 表示 `text1[0, i]` 和 `text2[0, j]`的最长公共子序列的长度，状态转移方程为：

- 当 `text1[i] ==  text[j]` 时，两个字符串都往前回溯一个字符，`dp[i][j] = dp[i - 1][j - 1] + 1`；
- 当 `text1[i] != text[j]` 时，分别把text1和text2往前回溯一个字符，取最大值；

可以将text1和text2转成字符数组，空间复杂度增加一点，但时间复杂度可以减低。

<details>
  <summary>动态规划</summary>

  ```java
    public int longestCommonSubsequence(String text1, String text2) {
        char[] t1 = text1.toCharArray();
        char[] t2 = text2.toCharArray();
        int n = t1.length;
        int m = t2.length;
        int[][] f = new int[n+1][m+1];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(t1[i] == t2[j]){
                    f[i+1][j+1] = f[i][j]+1;  
                } else {
                    f[i+1][j+1] = Math.max(f[i][j+1],f[i+1][j]);
                }
            }
        }
        return f[n][m];
    }
  ```
</details>
