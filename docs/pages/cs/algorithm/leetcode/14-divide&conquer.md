# 分治

---

## [23.合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists)

难度：⭐️⭐️⭐️⭐️

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

**解法一** 顺序合并

两两合并，按顺序合并。*注意不能排序，否则会超时*

<details>
  <summary>顺序合并</summary>

  ```java
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode head = null;
        for (int i = 0; i < lists.length; i++) {
            head = mergeLists(head, lists[i]);
        }
        return head;
    }

    private ListNode mergeLists(ListNode list1, ListNode list2) {
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
            if (p1 == null) {
                p.next = p2;
            }
            if (p2 == null) {
                p.next = p1;
            }
        }
        return dummy.next;
    }
  ```

</details>

**解法二** 分治

将数组分成两部分，头尾排序，递归调用。

<details>
  <summary>分治</summary>

```java
    public ListNode mergeKLists(ListNode[] lists) {
        return merge(lists, 0, lists.length - 1);
    }

    private ListNode merge(ListNode[] lists, int start, int end) {
        if (start == end) {
            return lists[start];
        } else if (start > end) {
            return null;
        } else {
            int mid = (end + start) >> 1;
            return mergeLists(merge(lists, start, mid), merge(lists, mid + 1, end));
        }
    }

    private ListNode mergeLists(ListNode list1, ListNode list2) {
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
            if (p1 == null) {
                p.next = p2;
            }
            if (p2 == null) {
                p.next = p1;
            }
        }
        return dummy.next;
    }
```

</details>

**解法三** 优先级队列

将所有链表的头结点加入优先级队列中，最前面的即为最小值，每次循环，将最小值排序并将最小值的next入队，直到队列为空。

<details>
  <summary>优先级队列</summary>

  ```java
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> queue = new PriorityQueue<>((ListNode n1, ListNode n2) -> {
            return n1.val - n2.val;
        });
        for (ListNode node : lists) {
            if (node != null) {
                queue.offer(node);
            }
        }
        ListNode head = new ListNode(-1);
        ListNode p = head;
        while (!queue.isEmpty()) {
            ListNode min = queue.poll();
            p.next = min;
            if (min.next != null) {
                queue.offer(min.next);
            }
            p = p.next;
        }
        return head.next;
    }
  ```

</details>

## [108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree)

难度：⭐️⭐️

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

**示例 1：**

![1](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

> 输入：nums = [-10,-3,0,5,9]  
> 输出：[0,-3,9,-10,null,5]  
> 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：  
> ![1.1](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

**示例 2：**

![2](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

> 输入：nums = [1,3]  
> 输出：[3,1]  
> 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。

**提示：**

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- nums 按 严格递增 顺序排列

**解法一** 中序遍历

二叉搜索树的任意节点，左子树所有的值都比其小，右子树所有值都比其大。所以实际的思路就是不断划分子数组，每个子数组的中点是根节点，左边就是左子树，右边是右子树。

<details>

<summary>中序遍历</summary>

```java
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return bfs(nums, 0, nums.length - 1);
    }

    private TreeNode bfs(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = bfs(nums, left, mid - 1);
        node.right = bfs(nums, mid + 1, right);
        return node;
    }
}
```

</details>
