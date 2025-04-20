# 图论

## [200.岛屿的数量](https://leetcode.cn/problems/number-of-islands)

难度：⭐️⭐️

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

**解法一** DFS

使用递归的解法，访问过的位置做标记，分别向上下左右4个方向递归访问。

<details>
  <summary>DFS递归</summary>

  ```java
  public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j =0; j < grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length) {
            return;
        }
        if (grid[r][c] != '1') {
            return;
        }
        grid[r][c] = '2';
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r + 1, c);
        dfs(grid, r, c - 1);
    }
  ```
</details>

## [994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges)

难度：⭐️⭐️

在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

- 值 `0` 代表空单元格；
- 值 `1` 代表新鲜橘子；
- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 周围 `4` 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1` 。

**解法一** 多源层次遍历

<details>
  <summary>多源层次遍历</summary>

  ```java
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    count++;
                }
            }
        }
        int ans = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            int depth = 0;
            for (int index = 0; index < size; index++) {
                int[] pos = queue.poll();
                int i = pos[0];
                int j = pos[1];
                // left
                if (i > 0 && grid[i - 1][j] == 1) {
                    grid[i - 1][j] = 2;
                    depth = 1;
                    queue.offer(new int[]{ i - 1, j});
                    count--;
                }
                // top
                if (j > 0 && grid[i][j - 1] == 1) {
                    grid[i][j - 1] = 2;
                    depth = 1;
                    queue.offer(new int[]{i, j - 1});
                    count--;
                }
                
                // right
                if (i < m - 1 && grid[i + 1][j] == 1) {
                    grid[i + 1][j] = 2;
                    depth = 1;
                    queue.offer(new int[]{i + 1, j});
                    count--;
                }
                // bottom
                if (j < n - 1 && grid[i][j + 1] == 1) {
                    grid[i][j + 1] = 2;
                    depth = 1;
                    queue.offer(new int[]{i, j + 1});
                    count--;
                }
            }
            ans += depth;
        }
        if (count > 0) {
            return -1;
        }
        return ans;
    }
  ```
</details>
