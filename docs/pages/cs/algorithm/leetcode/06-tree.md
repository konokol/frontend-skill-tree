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