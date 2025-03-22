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