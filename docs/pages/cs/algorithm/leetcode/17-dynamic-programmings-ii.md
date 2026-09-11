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
  <summary>动态规划</summary>

  ```java
  
  ```

</details>

## [72. 编辑距离](https://leetcode.cn/problems/edit-distance/description)

难度: ⭐️⭐️⭐️⭐️

给你两个单词 `word1` 和 `word2，` 请返回将 `word1` 转换成 `word2` 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符
 

**示例 1**：

**输入**：word1 = "horse", word2 = "ros"  
**输出**：3  
**解释**：  
horse -> rorse (将 'h' 替换为 'r')  
rorse -> rose (删除 'r')  
rose -> ros (删除 'e')  

**示例 2**：

**输入**：word1 = "intention", word2 = "execution"
**输出**：5
**解释**：  
intention -> inention (删除 't')  
inention -> enention (将 'i' 替换为 'e')  
enention -> exention (将 'n' 替换为 'x')  
exention -> exection (将 'n' 替换为 'c')  
exection -> execution (插入 'u')  
 

**提示**：

- `0 <= word1.length, word2.length <= 500`
- `word1` 和 `word2` 由小写英文字母组成

**解法一** 动态规划

对字符串 A 和字符串 B 编辑时等价的操作有 3 种：
- A 删除一个字符 或 B 插入一个字符
- A 插入一个字符 或 A 删除一个字符
- A 变换一个字符 或 B 变换一个字符

使用动态规划，定义数组 `dp[i][j]` 表示 A 的子串 A[0, i] 到 B 的子串 B[0, j] 的最小编辑距离，则 dp 的最后一个元素值即为此问题的解。

注意到 `A[0]` 表示 A 长度为 0 的子串，即空串，到 B[0, j] 的编辑距离是 j，此时一直对插入即可，同理 `B[0]` 也是一样，因此可以初始化 dp 的第 0 行和第 0 列的值。

对于 i > 0 且 j > 0 时，dp[i][j] 的取值可以从上一步计算出来：

- `dp[i - i][j]` 表示 A[0, i - 1] 到 B[0, j] 的最小编辑距离，在 A 的末尾追加一个一个字符即得到 A[0,i] 到 B[0, j] 的最小编辑距离 `dp[i][j] = dp[i - 1][j] + 1`；
- 同上，从 A[0, i] 到 B[0, j - 1] 的最小编辑距离，对 B 插入一个字符串，可以推导出来 `dp[i][j] = dp[i][j - 1] + 1`；
- 一样的，`dp[i - 1][j - 1]`，A 和 B 都少一个字符串，分两种情况讨论：1）`A[i] == B[j]`，有`dp[i][j] = dp[i - 1][j - 1]`，不做变换；1）`A[i] != B[j]`，`dp[i][j] = dp[i - 1][j - 1] + 1`，变换一个字符；

综合上面的三种情况，取最小值即可，可以得到状态转移方程：

当 `A[i] == B[j]`：  
`dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])`；

当 `A[i] != B[j]`：  
`dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)`；


<details>
    <suamary>动态规划</summary>

  ```java
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        if (m * n == 0) {
            return m + n;
        }
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i < m + 1; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j < n + 1; j++) {
            dp[0][j] = j;
        }
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]) + 1);
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
                }
            }
        }
        return dp[m][n];
    }
  
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
