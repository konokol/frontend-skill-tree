# 栈

## [20.有效的括号](https://leetcode.cn/problems/valid-parentheses)

难度：⭐️

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

提示：  
- 1 <= s.length <= 104
- s 仅由括号 '()[]{}' 组成

**解法一** 栈

依次入栈，看栈中的字符是否相等。

<details>
  <summary>栈</summary>

  ```java
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (stack.isEmpty()) {
                stack.push(c);
            } else {
                char top = stack.peek();
                if (c - top == 1 || c - top == 2) {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }
        }
        return stack.isEmpty();
    }
  ```
</details>

---

## [84. 柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram)

难度：⭐️⭐️⭐️⭐️

给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

> 输入：heights = [2,1,5,6,2,3]  
> 输出：10  
> 解释：最大的矩形为图中红色区域，面积为 10

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

> 输入： heights = [2,4]  
> 输出： 4  
 
**提示：**

- 1 <= heights.length <=10<sup>5</sup>
- 0 <= heights[i] <= 10<sup>5</sup>

**解法一** 单调栈

核心思路是对于每一个高度 h，分别向左和向右扩展，找到比 h 小的第一个位置，此时就是以 h 为高可以围成的最大矩形。如果直接用双重层循环去找会超时，因此可以使用单调递增栈，记录递增的下标，遇到一个非递增的位置时结束本次查找。

时间复杂度：O(n)  
空间复杂度：O(n)

<details>
    <summary>单调栈</summary>
    
```java
    public int largestRectangleArea(int[] heights) {
        Deque<Integer> deque = new ArrayDeque<>();
        int max = 0;
        for (int i = 0; i <= heights.length; i++) {
            int h = (i == heights.length ? 0 : heights[i]);
            while (!deque.isEmpty() && h < heights[deque.peek()]) {
                int height = heights[deque.pop()];
                int left = deque.isEmpty() ? -1 : deque.peek();
                max = Math.max(max, height * (i - left - 1));
            }
            deque.push(i);
        }
        return max;
    }
```
</details>

---

## [155. 最小栈](https://leetcode.cn/problems/min-stack/description)

难度：⭐️⭐️

设计一个支持 `push` `，pop` `，top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

- MinStack() 初始化堆栈对象。
- void push(int val) 将元素val推入堆栈。
- void pop() 删除堆栈顶部的元素。
- int top() 获取堆栈顶部的元素。
- int getMin() 获取堆栈中的最小元素。

**解法一** 使用数组

<details>
  <summary>数组</summary>

```java
class MinStack {

    private int min = Integer.MAX_VALUE;
    private int capcity = 30000;
    private int[] elements;
    private int index = -1;

    public MinStack() {
        elements = new int[capcity];
    }
    
    public void push(int val) {
        if (index >= elements.length - 1) {
            int[] temp = elements;
            elements = new int[(temp.length >> 1) + temp.length];
            System.arraycopy(temp, 0, elements, 0, temp.length);
        }
        elements[++index] = val;
        min = Math.min(min, val);
    }
    
    public void pop() {
        int top = elements[index];
        if (top == min) {
            min = Integer.MAX_VALUE;
            for (int i = 0; i < index; i++) {
                min = Math.min(min, elements[i]);
            }
        }
        index--;
        if (index < (elements.length >> 1) && index > capcity) {
            int[] temp = elements;
            elements = new int[elements.length >> 1];
            System.arraycopy(temp, 0, elements, 0, elements.length);
        }
    }
    
    public int top() {
        return elements[index];
    }
    
    public int getMin() {
        return min;
    }
}
```
</details>

**解法二** 使用原生的集合

---

## [739. 每日温度](https://leetcode.cn/problems/daily-temperatures/description)

难度：⭐️⭐️⭐️

给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。

**解法一** 单调栈

使用栈保存温度的下标，栈中的顺序是从栈底到栈顶递增。

<details>
  <summary>单调栈</summary>

  ```java
    public int[] dailyTemperatures(int[] temperatures) {
        int[] ans = new int[temperatures.length];
        Deque<Integer> stack = new LinkedList<>();
        for (int i = 0; i < temperatures.length; i++) {
            int t = temperatures[i];
            while (!stack.isEmpty() && t > temperatures[stack.peek()]) {
                int top = stack.pop();
                ans[top] = i - top;
            }
            stack.push(i);
        }
        return ans;
    }
  ```

</details>
