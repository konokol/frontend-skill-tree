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
