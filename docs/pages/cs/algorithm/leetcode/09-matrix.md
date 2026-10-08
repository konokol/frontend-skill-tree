# 矩阵

## [48.旋转图像](https://leetcode.cn/problems/rotate-image)

难度：⭐️⭐️⭐️

给定一个 `n × n` 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 `90` 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

**解法一** 原地旋转

顺时针循环，每次将4个位置的值轮换。为了防止旋转之后恢复原状，只需要遍历1/2。

<details>
  <summary>原地旋转</summary>

  ```java
    public void rotate(int[][] matrix) {
      int n = matrix.length;
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < (n + 1) / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n - i - 1] = temp;
            }
        }
    }
  ```
</details>

**解法二** 翻转

先水平翻转，再沿主对角线翻转。


<details>
  <summary>两次翻转</summary>

  ```java
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        // 水平翻转
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - i - 1][j];
                matrix[n - i - 1][j] = temp;
            }
        }

        // 主对角线翻转
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
  ```
</details>


## [54.螺旋矩阵](https://leetcode.cn/problems/spiral-matrix)

难度：⭐️⭐️⭐️

给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

**解法一** 按层遍历

记录上下左右边界，在循环中向4个方向移动。

<details>
  <summary>循环按层遍历</summary>
  
  ```java
  public List<Integer> spiralOrder(int[][] matrix) {
        int left = 0;
        int top = 0;
        int right = matrix[0].length - 1;
        int bottom = matrix.length - 1;
        List<Integer> list = new ArrayList<>();
        int count = matrix.length * matrix[0].length;
        while (true) {
            // right
            for (int i = left; i <= right; i++) {
                list.add(matrix[top][i]);
            }
            if (++top > bottom) break;
            // bottom
            for (int i = top; i <= bottom; i++) {
                list.add(matrix[i][right]);
            }
            if (--right < left) break;
            // left
            for (int i = right; i >= left; i--) {
                list.add(matrix[bottom][i]);
            }
            if (--bottom < top) break;
            // up
            for (int i = bottom; i >= top; i--) {
                list.add(matrix[i][left]);
            }
            if (++left > right) break;
        }
        return list;
    }
  ```
</details>

## [73. 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes)

难度：⭐️⭐️⭐️

给定一个 `m x n` 的矩阵，如果一个元素为 `0` ，则将其所在行和列的所有元素都设为 `0` 。请使用 原地 算法。

**解法一** 标记数组

用 2 个数组，分别记录行和列的数组中是否有 0，第一次遍历填充标记数组，第二次遍历，对矩阵中元素置零。

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

## [240.搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix-ii)

难度：⭐️⭐️

编写一个高效的算法来搜索 `m x n` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

**解法一** Z字形遍历

从右上或者左下开始遍历。

<details>
  <summary>Z字形遍历</summary>
  
  ```java
     public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int x = 0, y = n - 1;
        while (x < m && y >= 0) {
            if (matrix[x][y] == target) {
                return true;
            }
            if (matrix[x][y] < target) {
                x++;
            } else {
                y--;
            }
        }
        return false;
    }
  ```
</details>

**解法二** 按行二分查找

按行遍历矩阵，对每一行进行二分查找。

<details>
  <summary>按行二分查找</summary>

  ```java
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int i = 0; i < matrix.length; i++) {
            if (binarySearch(matrix[i], target)) {
                return true;
            }
        }
        return false;
    }

    private boolean binarySearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target == nums[mid]) {
                return true;
            } else if (target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
  ```
</details>

## [289.生命游戏](https://leetcode.cn/problems/game-of-life)

难度：⭐️⭐️⭐️

根据 [百度百科](https://baike.baidu.com/item/%E5%BA%B7%E5%A8%81%E7%94%9F%E5%91%BD%E6%B8%B8%E6%88%8F/22668799?fromtitle=%E7%94%9F%E5%91%BD%E6%B8%B8%E6%88%8F&fromid=2926434) ， 生命游戏 ，简称为 **生命** ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 `m × n` 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： `1` 即为 活细胞 （live），或 `0` 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是 同时 发生的。给你 `m x n` 网格面板 `board` 的当前状态，返回下一个状态。

给定当前 `board` 的状态，更新 `board` 到下一个状态。

**注意** 你不需要返回任何东西。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg)

> **输入**：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]  
> **输出**：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg)

> 输入：board = [[1,1],[1,0]]  
> 输出：[[1,1],[1,1]]

**提示：**

- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- board[i][j] 为 0 或 1

**解法一**：拷贝矩阵

拷贝一个 m * n 的矩阵存放原始值，计算状态时根据原始值更新。

代码：略

**解法二**：增加状态

由于之前的细胞只有 0 和 1 两种状态，一轮遍历的过程中如果直接改值，会导致丢失原始状态，无法保证“同时”，因此额外引入 2 个状态，共 4 个状态：
- -1，表示活细胞死亡，即 1 --> 0
- 0，死细胞状态不变
- 1，活细胞状态不变
- 2，死细胞复活，即 0 --> 1

遍历过程中，如果值是 -1 或 1，表示之前是活细胞，如果值是 0 或 2，表示之前是死细胞。

第二次再遍历，恢复成目标态。

<details>
    <summary>增加状态标记</summary>

```java
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        // calculate
        // -1(1 --> 0), 0, 1, 2 (0 --> 1)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int v = board[i][j];
                int liveCnt = 0;

                for (int r = i - 1; r <= i + 1; r++) {
                    for (int c = j - 1; c <= j + 1; c++) {
                        if (r == i && c == j) {
                            continue;
                        }
                        if (0 <= r && r < m && 0 <= c && c < n) {
                            liveCnt += (Math.abs(board[r][c]) == 1 ? 1 : 0);
                        }
                    }
                }
                // rule 1
                if (liveCnt < 2 && board[i][j] == 1) {
                    board[i][j] = -1;
                }
                // rule 3
                if (liveCnt > 3 && board[i][j] == 1) {
                    board[i][j] = -1;
                }
                // rule 4
                if (liveCnt == 3 && board[i][j] == 0) {
                    board[i][j] = 2;
                }
            }
        }

        // recover
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] < 1) {
                    board[i][j] = 0;
                } else if (board[i][j] > 0) {
                    board[i][j] = 1;
                }
            }
        }
    }
```
</details>
