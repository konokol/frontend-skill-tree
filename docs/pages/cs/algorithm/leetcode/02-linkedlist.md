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

## [25.K个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group)

难度：⭐️⭐️⭐️⭐️

给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

**解法一** 模拟

本题细节较多，核心思路是找到需要翻转的序列，对该序列的链表进行翻转。

<details>
  <summary>模拟</summary>

  ```java
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(-1);
        ListNode pre = dummy;
        pre.next = head;
        ListNode tail = head;
        while (tail != null) {
            for (int i = 0; i < k - 1; i++) {
                if (tail.next != null) {
                    tail = tail.next;
                } else {
                    return dummy.next;
                }
            }
            ListNode next = tail.next;
            ListNode[] temp = reverse(head, tail);
            pre.next = temp[0];
            pre = temp[1];
            pre.next = next;
            head = next;
            tail = head;
        }
        return dummy.next;
    }

    private ListNode[] reverse(ListNode head, ListNode tail) {
        ListNode pre = tail.next;
        ListNode p = head;
        while(pre != tail) {
            ListNode next = p.next;
            p.next = pre;
            pre = p;
            p = next;
        }
        return new ListNode[]{tail, head};
    }
  ```
</details>

## [138.随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer)

难度：⭐️⭐️⭐️

给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。


**解法一** 递归 + 哈希表

使用额外空间（哈希表）保存已经复制过的链表，复制每个节点时，先从哈希表中查，能查到直接返回，查不到则新创建节点，递归复制next和random。需要额外注意的是，每次创建后应当立即将新节点放到哈希表中，然后再递归，否则会栈溢出。

<details>
  <summary>递归+哈希表</summary>

  ```java
    private Map<Node, Node> cache = new HashMap<>();

    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        Node copy = cache.get(head);
        if (copy == null) {
            copy = new Node(head.val);
            cache.put(head, copy);
            copy.next = copyRandomList(head.next);
            copy.random = copyRandomList(head.random);
        }
        return copy;
    }
  ```
</details>

**解法二** 迭代