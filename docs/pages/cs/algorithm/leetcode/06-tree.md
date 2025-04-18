# 二叉树

## [94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal)

难度：⭐️

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

**解法一** 递归

<details>
  <summary>递归</summary>
  
  ```java
  public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        traversal(res, root);
        return res;
    }

    private void traversal(List<Integer> list, TreeNode root) {
        if (root == null) {
            return;
        }
        if (root.left != null) {
            traversal(list, root.left);
        }
        list.add(root.val);
        if (root.right != null) {
            traversal(list, root.right);
        }
    }
  ```

</details>


**解法二** 迭代

使用栈，循环中将左子树一直入栈，直至叶子结点，访问叶子结点，中间结点，中间结点的右结点。

<details>
  <summary>栈迭代</summary>

  ```java
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        while(!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            res.add(root.val);
            root = root.right;
        }
        return res;
    }
  ```
</details>

## [98.验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree)

难度：⭐️⭐️

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

- 节点的左子树只包含 小于 当前节点的数。
- 节点的右子树只包含 大于 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

**解法一** 递归

按照条件直接递归。

<details>
  <summary>直接递归</summary>
  
  ```java
  public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        boolean isLeftBst = true;
        if (root.left != null) {
            int maxLeft = max(root.left);
            if (maxLeft >= root.val) {
                return false;
            }
        }
        if (root.right != null) {
            int minRight = min(root.right);
            if (minRight <= root.val) {
                return false;
            }
        }
        return isValidBST(root.left) && isValidBST(root.right);
    }

    private int min(TreeNode root) {
        if (root == null) {
            return Integer.MAX_VALUE;
        }
        int value = root.val;
        int min = Math.min(min(root.left), min(root.right));
        return Math.min(min, value);
    }

    private int max(TreeNode root) {
        if (root == null) {
            return Integer.MIN_VALUE;
        }
        int value = root.val;
        int max = Math.max(max(root.left), max(root.right));
        return Math.max(max, value);
    }
  ```
</details>

<details>
  <summary>优化版本的递归</summary>

  ```java
  ```
</details>

**解法二** 中序遍历

## [102. 二叉树的层次遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal)

难度：⭐️⭐️

给你二叉树的根节点 `root` ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

**方法一** 队列

使用队列，第一层循环条件是队列非空，每次进入循环时，队列中恰好是当前层的元素，记录其位置n，遍历队列中n个元素之后，当前层刚好遍历结束。

<details>
  <summary>广度优先层次遍历</summary>

  ```java
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> list = new ArrayList<>();
        if (root == null) {
            return list;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> layer = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                layer.add(node.val);
                if (node.left != null) {
                    queue.add(node.left);
                }
                if (node.right != null) {
                    queue.add(node.right);
                }
            }
            if (!layer.isEmpty()) {
                list.add(layer);
            }
        }
        return list;
    }
  ```

</details>


## [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree)

难度：⭐️

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

**解法一** 深度优先

<details>
  <summary>递归</summary>

  ```java
    public int maxDepth(TreeNode root) {
      return root == null ? 0 : Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
  ```
</details>

**解法二** 广度优先

层次遍历。使用队列，循环开始时，队列中放的始终是当前层的结点，记录当前层的节点数。遍历的同时，将下一层节点放入队列中。

<details>
  <summary>广度优先遍历</summary>

  ```java
  public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            depth++;
        }
        return depth;
    }
  ```
</details>

## [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal)

难度：⭐️⭐️⭐️⭐️

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的先序遍历， `inorder` 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

**解法一** 递归

前序数组的第一个元素是根节点，找到根节点在中序数组的下标，对数组进行拆分。

<details>
  <summary>递归</summary>

  ```java
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }

    private TreeNode buildTree(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd) {
        if (preStart > preEnd) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[preStart]);
        int mid = inStart;
        while (inorder[mid] != root.val) {
            mid++;
        }
        int leftLength = mid - inStart;
        int rightSize = inEnd - mid;
        //[ [...] mid [...]]
        root.left = buildTree(preorder, preStart + 1, preStart + leftLength, inorder, inStart, mid - 1);
        root.right = buildTree(preorder, preStart + 1 + leftLength, preEnd, inorder, mid + 1, inEnd);
        return root;
    }
  ```
</details>

## [108. 有序数组转二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree)

难度：⭐️

给你一个整数数组 `nums` ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

**解法一** 中序遍历

平衡二叉搜索树的根节点一定在数字的中间位置，因此递归将数字不断拆分即可得到平衡二叉树。

<details>
  <summary>中序遍历</summary>

  ```java
    public TreeNode sortedArrayToBST(int[] nums) {
        return bst(nums, 0, nums.length - 1);
    }

    private TreeNode bst(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = (left + right) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = bst(nums, left, mid - 1);
        root.right = bst(nums, mid + 1, right);
        return root;
    }
  ```
</details>

## [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list)

难度：⭐️⭐️

给你二叉树的根结点 `root` ，请你将它展开为一个单链表：

- 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。
- 展开后的单链表应该与二叉树 先序遍历 顺序相同。

**解法一** 先序遍历

使用栈，先序遍历二叉树。遍历过程中，对节点进行处理。

<details>
  <summary>非递归先序遍历</summary>

  ```java
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        TreeNode dummy = new TreeNode(-1);
        TreeNode p = dummy;
        dummy.right = root;
        Deque<TreeNode> stack = new LinkedList<>();
        stack.push(root);
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            p.right = node;
            p.left = null;
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
            p = p.right;
        }
    }
  ```
</details>

## [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view)

难度：⭐️⭐️

给定一个二叉树的 根节点 `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**解法一** 非递归深度优先

深度优先前序遍历，使用哈希表保存遍历到的每一层的深度和第一个访问到的节点。

<details>
  <summary>哈希表 + 深度优先</summary>

  ```java
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        Deque<TreeNode> stack = new ArrayDeque<>();
        Deque<Integer> depthStack = new ArrayDeque<>();
        Map<Integer, Integer> map = new LinkedHashMap<>();
        TreeNode p = root;
        stack.push(root);
        depthStack.push(0);
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            int depth = depthStack.pop();
            if (!map.containsKey(depth)) {
                map.put(depth, node.val);
            }
            if (node.left != null) {
                stack.push(node.left);
                depthStack.push(depth + 1);
            }
            if (node.right != null) {
                stack.push(node.right);
                depthStack.push(depth + 1);
            }
        }
        return new ArrayList<>(map.values());
    }
  ```
</details>

**解法二** 层次遍历

层次遍历，每一层的最后一个节点即为最右侧节点。

<details>
  <summary>哈希表 + 深度优先</summary>

  ```java
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> list = new LinkedList<>();
        if (root == null) {
            return list;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (i == size - 1) {
                    list.add(node.val);
                }
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
        return list;
    }
  ```
</details>

**解法三** 递归 + 深度遍历

递归遍历的过程中，记录层数。


## [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree)

难度：⭐️

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

**方法一** 递归

<details>
  <summary>递归</summary>

  ```java
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        }
        TreeNode left = invertTree(root.right);
        TreeNode right = invertTree(root.left);
        root.left = left;
        root.right = right;
        return root;
    }
  ```
</details>

**解法二** 广度优先遍历

层次遍历。仍然使用队列，遍历每一层的每个节点时，将每个节点的左右节点交换。

<details>
  <summary>层次遍历</summary>

  ```java
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                TreeNode temp = node.left;
                node.left = node.right;
                node.right = temp;

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
        return root;
   }
  ```
</details>

## [230. 二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst)

难度：⭐️⭐️

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 小的元素（从 `1` 开始计数）。

**解法一** 深度优先遍历

<details>
  <summary>深度优先遍历</summary>

  ```java
    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode p = root;
        int i = 0;
        stack.push(p);
        while (!stack.isEmpty()) {
            while(p != null) {
                stack.push(p);
                p = p.left;
            }
            TreeNode node = stack.pop();
            i++;
            if (i == k) {
                return node.val;
            }
            p = node.right;
        }
        return -1;
    }
  ```
</details>


## [543. 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree)

难度：⭐️⭐️

给你一棵二叉树的根节点，返回该树的 **直径** 。

二叉树的 **直径** 是指树中任意两个节点之间最长路径的 **长度** 。这条路径可能经过也可能不经过根节点 `root` 。

两节点之间路径的 **长度** 由它们之间边数表示。

**解法一** 深度遍历

递归解法计算二叉树的深度，取左子树和右子树的最大深度之和。由于可能不经过根节点，需要在遍历的过程中记录最大深度。

<details>
  <summary>深度遍历</summary>

  ```java
    private int ans;
    public int diameterOfBinaryTree(TreeNode root) {
        ans = 1;
        depth(root);
        return ans - 1;
    }

    private int depth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = depth(root.left);
        int right = depth(root.right);
        ans = Math.max(ans, left + right + 1);
        return 1 + Math.max(left, right);
    }
  ```

</details>

