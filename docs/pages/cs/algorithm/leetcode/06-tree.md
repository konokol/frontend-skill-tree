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