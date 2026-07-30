# 双指针

## [42.接雨水](https://leetcode.cn/problems/trapping-rain-water/description)

难度：⭐️⭐️⭐️

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

**解法一** 双指针

从两端向中间移动，维护左右两边的最大高度，雨水量取决于两边较小值。

<details>
  <summary>双指针</summary>

```java
public int trap(int[] height) {
    if (height == null || height.length == 0) {
        return 0;
    }
    int left = 0;
    int right = height.length - 1;
    int leftMax = 0;
    int rightMax = 0;
    int water = 0;
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                water += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                water += rightMax - height[right];
            }
            right--;
        }
    }
    return water;
}
```
</details>

**解法二** 动态规划

先预处理出每个位置左边最大值和右边最大值，然后遍历计算每个位置能接的雨水。

<details>
  <summary>动态规划</summary>

```java
public int trap(int[] height) {
    int n = height.length;
    if (n == 0) return 0;

    // 左边最大值数组
    int[] leftMax = new int[n];
    leftMax[0] = height[0];
    for (int i = 1; i < n; i++) {
        leftMax[i] = Math.max(leftMax[i - 1], height[i]);
    }

    // 右边最大值数组
    int[] rightMax = new int[n];
    rightMax[n - 1] = height[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        rightMax[i] = Math.max(rightMax[i + 1], height[i]);
    }

    // 计算每个位置能接的雨水
    int water = 0;
    for (int i = 0; i < n; i++) {
        water += Math.min(leftMax[i], rightMax[i]) - height[i];
    }

    return water;
}
```
</details>

**解法三** 单调栈

使用栈保存下标，遇到比栈顶低的柱子就计算积水，利用单调栈的性质减少计算量。

<details>
  <summary>单调栈</summary>

```java
public int trap(int[] height) {
    int n = height.length;
    Deque<Integer> stack = new ArrayDeque<>();
    int water = 0;

    for (int i = 0; i < n; i++) {
        while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
            int top = stack.pop();
            if (stack.isEmpty()) break;
            int left = stack.peek();
            int right = i;
            int width = right - left - 1;
            int heightDiff = Math.min(height[left], height[right]) - height[top];
            water += width * heightDiff;
        }
        stack.push(i);
    }

    return water;
}
```
</details>

