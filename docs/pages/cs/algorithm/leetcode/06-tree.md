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

## [102. 二叉树的层次遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal)

难度：⭐️⭐️

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

**方法一** 队列

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


