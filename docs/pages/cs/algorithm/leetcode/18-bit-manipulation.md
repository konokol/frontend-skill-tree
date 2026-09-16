# 位运算

[67.二进制求和](https://leetcode.cn/problems/add-binary/description)

难度：难度：⭐️

给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

**示例 1：**

> **输入:** a = "11", b = "1"  
> **输出：** "100"

**示例 2：**

> **输入：** a = "1010", b = "1011"  
> **输出：** "10101"
 

**提示：**

- 1 <= a.length, b.length <= 104
- a 和 b 仅由字符 '0' 或 '1' 组成
- 字符串如果不是 "0" ，就不含前导零


**解法一**：循环

使用循环，每次1位，左移然后按位与。

<details>
    <summary> 按位处理 </summary>
    
```java
    public String addBinary(String a, String b) {
        int m = a.length();
        int n = b.length();
        int carry = 0;
        StringBuilder builder = new StringBuilder();
        int i = m - 1;
        int j = n - 1;
        while (i >= 0 || j >= 0) {
            int aa = i >= 0 ? a.charAt(i--) - '0' : 0;
            int bb = j >= 0 ? b.charAt(j--) - '0' : 0;
            int v = aa + bb + carry;
            // 0 1 2 3
            builder.append(v % 2);
            carry = v / 2;
        }
        if (carry > 0) {
            builder.append(carry);
        }
        return builder.reverse().toString();
    }

```
</details>
