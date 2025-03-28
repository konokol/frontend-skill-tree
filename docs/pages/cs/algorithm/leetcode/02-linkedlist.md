# 链表

## [2. 两数相加](https://leetcode.cn/problems/add-two-numbers)

难度：⭐️

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

![两数相加](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg)

**解法一** 直接相加

用头结点占位，遍历相加并保存进位标识。注意加上最后一个进位的值。

<details>
  <summary>两数相加</summary>
  
  ```java
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode p = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry > 0) {
            int v = 0;
            if (l1 != null) {
                v += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                v += l2.val;
                l2 = l2.next;
            }
            v += carry;
            if (v > 9) {
                v = v % 10;
                carry = 1;
            } else {
                carry = 0;
            }
            p.next = new ListNode(v);
            p = p.next;
        }
        return dummy.next;
    }
  ```
</details>


## [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/description/)

难度：⭐️

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**解法一** 迭代

直接循环，将指针每次都指向较小的节点。

<details>
    <summary>迭代</summary>
    ```java
    public ListNode mergeTwoLists1(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        ListNode dummy = new ListNode(-1);
        ListNode p = dummy;
        ListNode p1 = list1;
        ListNode p2 = list2;
        while (p1 != null && p2 != null) {
            if (p1.val < p2.val) {
                p.next = p1;
                p1 = p1.next;
            } else {
                p.next = p2;
                p2 = p2.next;
            }
            p = p.next;
        }
        if (p1 != null) {
            p.next = p1;
        } else if (p2 != null) {
            p.next = p2;
        }
        return dummy.next;
    }
    ```
</details>

**解法二** 递归

比较头结点，较小的节点的next作为一个子链表，递归和另一个链表比，返回较小节点。其中一个节点为空时，返回另一个节点，递归中止。

<details>
    <summary>递归放</summary>
    ```java
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val < list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
    ```
</details>

## [24.两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs)

难度：⭐️⭐️

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

**解法一** 直接交换

运用占位的前驱节点，同时记录前序节点和当前节点。

<details>
  <summary>直接交换</summary>

  ```java
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode pre = dummy;
        ListNode p = head;
        // 1 -> 2 -> 3
        while (p != null && p.next != null) {
            // 2
            ListNode next = p.next;
            // 1 -> 3
            p.next = next.next;
            // 2 -> 1 -> 3
            next.next = p;
            // * -> 2 -> 1 -> 3
            pre.next = next;
            pre = p;
            p = p.next;
        }
        return dummy.next;
    }
  ```
</details>