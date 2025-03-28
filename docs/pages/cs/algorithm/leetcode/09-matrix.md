# 矩阵

## [73. 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes)

给定一个 `m x n` 的矩阵，如果一个元素为 `0` ，则将其所在行和列的所有元素都设为 `0` 。请使用 原地 算法。

**解法一** 标记数组

用2个数组，分别记录行和列的数组中是否有0，第一次遍历填充标记数组，第二次遍历，对矩阵中元素置零。

<details>
  <summary>标记数组</summary>

  ```java
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        boolean[] r = new boolean[row];
        boolean[] c = new boolean[col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    r[i] = true;
                    c[j] = true;
                }
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (r[i] || c[j]) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
  ```
</details>
