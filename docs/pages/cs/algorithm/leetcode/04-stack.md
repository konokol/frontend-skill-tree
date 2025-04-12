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

