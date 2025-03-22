# 链表

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
