package LeetCodeJava.Tree;

// https://leetcode.com/problems/binary-tree-inorder-traversal/description/

import LeetCodeJava.DataStructure.TreeNode;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BinaryTreeInorderTraversal {

    /**
     * recursion
     */
    class SolutionV1 {
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> res = new ArrayList<>();
            helper(root, res);
            return res;
        }

        public void helper(TreeNode root, List<Integer> res) {
            if (root != null) {
                helper(root.left, res);
                res.add(root.val);
                helper(root.right, res);
            }
        }
    }

    /**
     * iteration
     */
    class SolutionV2 {
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> res = new ArrayList<>();
            Stack<TreeNode> stack = new Stack<>();
            TreeNode curr = root;
            while (curr != null || !stack.isEmpty()) {
                while (curr != null) {
                    stack.push(curr);
                    curr = curr.left;
                }
                curr = stack.pop();
                res.add(curr.val);
                curr = curr.right;
            }
            return res;
        }

    }

}
