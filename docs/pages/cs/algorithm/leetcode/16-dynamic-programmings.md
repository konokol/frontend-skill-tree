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
