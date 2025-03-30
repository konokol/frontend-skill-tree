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
    public int[][] merge(int[][] intervals) {
        int start = 0;
        int end = 0;
        Arrays.sort(intervals, (int[] a, int[] b) -> {
            return a[0] - b[0];
        });
        List<int[]> resultList = new ArrayList<>();
        resultList.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int[] range = intervals[i];
            int[] merged = resultList.get(resultList.size() - 1);
            if (range[0] > merged[1]) {
                resultList.add(range);
            } else {
                merged[1] = Math.max(range[1], merged[1]);
            }
        }
        return resultList.toArray(new int[resultList.size()][]);
    }
  ```
</details>
