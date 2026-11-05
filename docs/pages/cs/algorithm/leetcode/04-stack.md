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

### [71. 简化路径](https://leetcode.cn/problems/simplify-path/description)

难度：⭐️⭐️

给你一个字符串 `path` ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 `'/'` 开头），请你将其转化为 更加简洁的规范路径。  

在 Unix 风格的文件系统中规则如下：

- 一个点 `'.'` 表示当前目录本身。
- 此外，两个点 `'..'` 表示将目录切换到上一级（指向父目录）。
- 任意多个连续的斜杠（即，`'//'` 或 `'///'`）都被视为单个斜杠 `'/'`。
- 任何其他格式的点（例如，`'...'` 或 `'....'`）均被视为有效的文件/目录名称。

返回的 简化路径 必须遵循下述格式： 

- 始终以斜杠 `'/'` 开头。
- 两个目录名之间必须只有一个斜杠 `'/'` 。
- 最后一个目录名（如果存在）不能 以 `'/'` 结尾。
- 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 `'.'` 或 `'..'`）。

返回简化后得到的 **规范路径** 。

**示例 1：**

> 输入：path = "/home/"  
> 输出："/home"  
> 解释：  
> 应删除尾随斜杠。  

**示例 2：**

> 输入：path = "/home//foo/"  
> 输出："/home/foo"  
> 解释：  
> 多个连续的斜杠被单个斜杠替换。  

**示例 3：**

> 输入：path = "/home/user/Documents/../Pictures"  
> 输出："/home/user/Pictures"  
> 解释：  
> 两个点 ".." 表示上一级目录（父目录）。  

**示例 4：**

> 输入：path = "/../"  
> 输出："/"  
> 解释：  
> 不可能从根目录上升一级目录。  

**示例 5：**

> 输入：path = "/.../a/../b/c/../d/./"  
> 输出："/.../b/d"  
> 解释：  
> "..." 在这个问题中是一个合法的目录名。  

**提示：**

- 1 <= path.length <= 3000
- path 由英文字母，数字，'.'，'/' 或 '_' 组成。
- path 是一个有效的 Unix 风格绝对路径。

**解法一** 栈 

使用栈，题目中输入都是合法的路径，根据 `/` 分割字符串，遇到 `..` 出栈一次，遇到 `.` 则不做任何处理，其他情况都入栈，最后将栈中字符用 `/` 拼接起来。

注意，栈中只存路径名，不存分隔符，能简化很多逻辑。

<details>
<summary>栈</summary>
    
```java
class Solution {
    public String simplifyPath(String path) {
        String[] paths = path.split("/");
        Deque<String> deque = new LinkedList<>();

        for (String p: paths) {
            if ("..".equals(p)) {
                if (!deque.isEmpty()) {
                    deque.pop();
                }
            } else if (p.length() > 0 && !".".equals(p)) {
                deque.push(p);
            }
        }
        StringBuilder builder = new StringBuilder();
        if (deque.isEmpty()) {
            return "/";
        } else {
            while (!deque.isEmpty()) {
                builder.append('/').append(deque.removeLast());
            }
            return builder.toString();
        }
    }
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
        int[] left = new int[heights.length];
        int[] right = new int[heights.length];
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < heights.length; i++) {
            while (!deque.isEmpty() && heights[i] <= heights[deque.peek()]) {
                deque.pop();
            }
            left[i] = deque.isEmpty() ? -1 : deque.peek();
            deque.push(i);
        }
        deque.clear();
        for (int i = heights.length - 1; i >= 0; i--) {
            while (!deque.isEmpty() && heights[i] <= heights[deque.peek()]) {
                deque.pop();
            }
            right[i] = deque.isEmpty() ? heights.length : deque.peek();
            deque.push(i);
        }

        int max = 0;
        for (int i = 0; i < heights.length; i++) {
            max = Math.max(max, heights[i] * (right[i] - left[i] - 1));
        }
        return max;
    }
```
</details>

<details>
    <summary>单调栈 + 常数优化</summary>
    
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

## [155. 最小栈](https://leetcode.cn/problems/min-stack)

难度：⭐️⭐️

设计一个支持 `push` `，pop` `，top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

- MinStack() 初始化堆栈对象。
- void push(int val) 将元素val推入堆栈。
- void pop() 删除堆栈顶部的元素。
- int top() 获取堆栈顶部的元素。
- int getMin() 获取堆栈中的最小元素。

**解法一** 单数组

使用一个数组，单独保存最小值，pop 和 push 时，重新计算最小值。

时间复杂度：pop操作是O(n)，其他是O(1)  
空间复杂度：O(n)

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

**解法二** 使用双栈

使用一个额外的栈，每次 push 时都放当前栈中最小的元素。

时间复杂度：O(1)  
空间复杂度：O(n)  

<details>
  <summary>双栈</summary>

```java
class MinStack {

    private Deque<Integer> stack;
    private Deque<Integer> minStack;

    public MinStack() {
        stack = new ArrayDeque<>();
        minStack = new ArrayDeque<>();
        minStack.push(Integer.MAX_VALUE);
    }
    
    public void push(int value) {
        stack.push(value);
        minStack.push(Math.min(value, minStack.peek()));
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
```
</details>

也可以不用 Deque，直接用基本的数组来实现，时间复杂度和空间复杂度一样。

<details>
  <summary>双数组</summary>

```java
class MinStack {

    private Deque<Integer> stack;
    private Deque<Integer> minStack;

    public MinStack() {
        stack = new ArrayDeque<>();
        minStack = new ArrayDeque<>();
        minStack.push(Integer.MAX_VALUE);
    }
    
    public void push(int value) {
        stack.push(value);
        minStack.push(Math.min(value, minStack.peek()));
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
```
</details>

**解法三** 链表

时间复杂度：O(1)  
空间复杂度：O(n)  

使用链表，头结点表示栈顶，结点同时有值和最小值，每次入栈更新最小值。

<details>
  <summary>链表</summary>

```java
class MinStack {

    private Deque<Integer> stack;
    private Deque<Integer> minStack;

    public MinStack() {
        stack = new ArrayDeque<>();
        minStack = new ArrayDeque<>();
        minStack.push(Integer.MAX_VALUE);
    }
    
    public void push(int value) {
        stack.push(value);
        minStack.push(Math.min(value, minStack.peek()));
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
```
</details>

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
