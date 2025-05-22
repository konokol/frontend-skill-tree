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

## [198.打家劫舍](https://leetcode.cn/problems/house-robber/description)

难度：⭐️

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

**解法一** 动态规划

用dp[][]数组表示到第i家时，偷或者不偷可以偷盗到的最大值，答案为数组的最后一组值。

<details>
  <summary>二维数组</summary>

  ```java
    public int rob(int[] nums) {
        int[][] dp = new int[nums.length][2];
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                dp[i][0] = 0;
                dp[i][1] = nums[i];
            } else {
                dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
                dp[i][1] = dp[i - 1][0] + nums[i];
            }
        }
        int[] ans = dp[nums.length - 1];
        return Math.max(ans[0], ans[1]);
    }
  ```
</details>

用二维数组空间复杂度更高，可以精简空间，第i个位置，回溯到i-1和i-2的位置。

<details>
  <summary>一维数组</summary>

  ```java
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }
        return dp[nums.length - 1];
    }
  ```
</details>

基于上一种写法，还可以继续优化空间复杂度，只用2个int记录i-1和i-2的值。

<details>
  <summary>两个数字</summary>

  ```java
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        int last1 = nums[0];
        int last0 = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) {
            int temp = last0;
            last0 = Math.max(last1 + nums[i], last0);
            last1 = temp;
        }
        return last0;
    }
  ```
</details>
