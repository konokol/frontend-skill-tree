# 图论

## [200.岛屿数量](https://leetcode.cn/problems/number-of-islands)

难度：⭐️⭐️

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

**示例 1：**

> 输入：grid = [  
> ['1','1','1','1','0'],  
> ['1','1','0','1','0'],  
> ['1','1','0','0','0'],  
> ['0','0','0','0','0']  
>]
>输出：1

**示例 2：**

> 输入：grid = [
> ['1','1','0','0','0'],  
> ['1','1','0','0','0'],  
> ['0','0','1','0','0'],  
> ['0','0','0','1','1']  
>]
>输出：3

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m`, `n <= 300`
- `grid[i][j]` 的值为 '0' 或 '1'

**解法一** DFS 深度优先

使用递归的解法，访问过的位置做标记，分别向上下左右4个方向递归访问。

时间复杂度：O(mn)  
空间复杂度：O(mn)  

<details>
  <summary>DFS递归</summary>

```java
class Solution {

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
}
```

</details>

**解法二** BFS 广度优先

和 DFS 类似，遍历到每个节点后，将这个节点的一圈都入队列。虽然时间复杂度和空间复杂度和空间复杂度都和 DFS 一样，因为存位置需要用int[]，实际会更慢一点。

时间复杂度：O(mn)  
空间复杂度：O(mn)  

<details>
  <summary>BFS</summary>

```java
class Solution {

    private int[][] directions = new int[][] {
        new int[] {-1, 0},
        new int[] {0, -1},
        new int[] {1, 0},
        new int[] {0, 1},
    };

    public int numIslands(char[][] grid) {

        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    bfs(grid, i, j);
                }
            }
        }
        return count;
    }

    private void bfs(char[][] grid, int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {x, y});
        grid[x][y] = '#';
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] p = queue.poll();
                for (int[] d : directions) {
                    int r = p[0] - d[0];
                    int c = p[1] - d[1];
                    if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length) {
                        continue;
                    }
                    if (grid[r][c] == '1') {
                        queue.offer(new int[] {r, c});
                        grid[r][c] = '#';
                    }
                }
            }
            
        }
    }
}
```

</details>

## [207. 课程表](https://leetcode.cn/problems/course-schedule)

难度：⭐️⭐️⭐️

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程  `bi` 。

例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。
请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**

> 输入：numCourses = 2, prerequisites = [[1,0]]  
> 输出：true  
> 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

**示例 2：**

> 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]  
> 输出：false  
> 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。  

**提示：**

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- prerequisites[i] 中的所有课程对 互不相同

**解法一** 广度优先

经典的拓扑排序算法，构建有向图，判读是否成环，按照步骤：

1. 先构建每门课程完成后下一门可修课程的数组，即出度，同时记录每门课程先修的数量，即入度
2. 使用队列开始广度遍历，先找到前序课程为 0 的课（入度为0），加入队列访问它
3. 然后访问其下一门课，将下一门课的入度减一，当下一门课的入度减为0后，加入队列

重复上述过程，直到访问完所有入度为0的课，记录一共可以访问到多少节点。
当访问的节点树和课程总数相同时，即所有的课程都可以修完。

时间复杂度：O(m + n)  
空间复杂度：O(m + n)  

<details>
  <summary>广度优先</summary>

```java
class Solution {

    public boolean canFinish(int numCourses, int[][] prerequisites) {

        int prev[] = new int[numCourses]; // 入度
        List<Integer>[] nexts = new List[numCourses]; // 出度
        Arrays.setAll(nexts, i -> new ArrayList<>());
        for (int i = 0; i < prerequisites.length; i++) {
            int u = prerequisites[i][1];
            int v = prerequisites[i][0];
            nexts[u].add(v);
            prev[v]++;
        }

        // 入度为 0 入队列，代表这门课没有先修课程
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (prev[i] == 0) {
                queue.offer(i);
            }
        }

        int count = 0;
        while (!queue.isEmpty()) {
            // 上课
            count++;
            int u = queue.poll();
            List<Integer> next = nexts[u];
            for (int v: next) {
                // 入度减一，减掉一门已经完成的先修课程
                prev[v]--;
                if (prev[v] == 0) { // 入度为 0，即已经没有先修课程了
                    queue.offer(v);
                }
            }
        }
        return count == numCourses;
    }
}
```

</details>

**解法二** 深度优先遍历

深度优先遍历，采用三色标记法。先构建有向图，用数组 `visited` 记录每个节点的访问状态，分别是未访问(0)、访问中(1)、已访问(2)。对于每一个节点，dfs 刚开始标记成 1，结束是 2，如果在一次遍历过程中，遇到了 1 说明有环。

时间复杂度：O(m + n)  
空间复杂度：O(m + n)  

<details>
  <summary>广度优先</summary>

```java
class Solution {

    private int[] visited;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // 1.建图
        List<Integer>[] graph = new List[numCourses];
        for (int i = 0; i < prerequisites.length; i++) {
            int u = prerequisites[i][1];
            int v = prerequisites[i][0];
            if (graph[u] == null) {
                graph[u] = new ArrayList<>();
            }
            graph[u].add(v);
        }

        // 2.dfs 三色标记 0 未访问 1 访问中 2 已访问
        visited = new int[numCourses];
        for (int i = 0; i < visited.length; i++) {
            if (visited[i] == 0) {
                if (!dfs(graph, i)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean dfs(List<Integer>[] graph, int u) {
        visited[u] = 1; // 标记已经开始访问
        List<Integer> next = graph[u];
        if (next != null) {
            for (int v : next) {
                if (visited[v] == 1) {
                    return false;
                }
                if (visited[v] == 0) {
                    if (!dfs(graph, v)) {
                        return false;
                    }
                }
            }
        }
        visited[u] = 2; // 标记访问结束
        return true;
    }
}
```

</details>

---

## [208. 实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree)

难度：⭐️⭐️⭐️

[Trie](https://baike.baidu.com/item/%E5%AD%97%E5%85%B8%E6%A0%91/9825209?fr=aladdin)（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

- `Trie()` 初始化前缀树对象。
- `void insert(String word)` 向前缀树中插入字符串 `word` 。
- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。
- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

**解法一** 字典树

相当于一个26叉树，每一层代表单词中的一个字符，用isEnd表示是否到了单词的最后一个字母。

<details>
  <summary>字典树</summary>

  ```java
  class Trie {

    private Trie[] children;
    private boolean isEnd;

    public Trie() {
        children = new Trie[26];
        isEnd = false;
    }
    
    public void insert(String word) {
        Trie node = this;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (node.children[c - 'a'] == null) {
                node.children[c - 'a'] = new Trie();
            }
            node = node.children[c - 'a'];
        }
        node.isEnd = true;
    }
    
    public boolean search(String word) {
        Trie node =  searchPrefix(word);
        return node != null && node.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        Trie node =  searchPrefix(prefix);
        return node != null;
    }

    private Trie searchPrefix(String prefix) {
        Trie node = this;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if (node.children[c - 'a'] == null) {
                return null;
            }
            node = node.children[c - 'a'];
        }
        return node;
    }
  }
  ```
</details>


---

## [994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges)

难度：⭐️⭐️

在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

- 值 `0` 代表空单元格；
- 值 `1` 代表新鲜橘子；
- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 周围 `4` 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1` 。

**解法一** 多源层次遍历

使用层次遍历，先遍历一遍所有节点，将腐烂的橘子加入队列中，作为第一层，同时记录未腐烂的橘子的个数。
层次遍历，如果下一层有未腐烂的橘子，则深度加1，腐烂它，并将总个数减一，当遍历完之后，如果总数未归0，返回-1，否则返回深度。

时间复杂度：O(mn)  
空间复杂度：O(mn)

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
