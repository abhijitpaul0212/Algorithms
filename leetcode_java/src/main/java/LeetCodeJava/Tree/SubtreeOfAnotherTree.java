package LeetCodeJava.Tree;

// https://leetcode.com/problems/subtree-of-another-tree/

import LeetCodeJava.DataStructure.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class SubtreeOfAnotherTree {

    // V0
    // IDEA : DFS
    // TODO : fix below
//    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
//
//        if (root == null) {
//            return false;
//        }
//
////        if (root == null && subRoot != null){
////            return false;
////        }
//
//
//        // check
//
//        // case 1)
//        if (isSame(root, subRoot)){
//            return true;
//        }
//
//        // case 2)
//        return isSame(root.left, subRoot) || isSame(root.right, subRoot);
//    }
//
//    private Boolean isSame(TreeNode node1, TreeNode node2){
//
//        if (node1 == null || node2 == null){
//            return node1 == null && node2 == null;
//        }
//
////        if (node1.val != node2.val){
////            return false;
////        }
//
//        return node1.val == node2.val && isSame(node1.left, node2.left) && isSame(node1.right, node2.right);
//    }


    // V1
    // IDEA : DFS
    // https://leetcode.com/problems/subtree-of-another-tree/editorial/
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {

        // If this node is Empty, then no tree is rooted at this Node
        // Hence, "tree rooted at node" cannot be equal to "tree rooted at subRoot"
        // "tree rooted at subRoot" will always be non-empty, as per constraints
        if (root == null) {
            return false;
        }

        // Check if the "tree rooted at root" is identical to "tree roooted at subRoot"
        if (isIdentical(root, subRoot)) {
            return true;
        }

        // If not, check for "tree rooted at root.left" and "tree rooted at root.right"
        // If either of them returns true, return true
        // NOTE !!! either left or right tree equals subRoot is acceptable
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    /** NOTE !!! check this help func */
    private boolean isIdentical(TreeNode node1, TreeNode node2) {

        // If any of the nodes is null, then both must be null
        if (node1 == null || node2 == null) {
            return node1 == null && node2 == null;
        }

        // If both nodes are non-empty, then they are identical only if
        // 1. Their values are equal
        // 2. Their left subtrees are identical
        // 3. Their right subtrees are identical
        return node1.val == node2.val && isIdentical(node1.left, node2.left) && isIdentical(node1.right, node2.right);
    }

    // V2
    // IDEA : STRING MATCH
    // https://leetcode.com/problems/subtree-of-another-tree/editorial/
    public boolean isSubtree_2(TreeNode root, TreeNode subRoot) {
        // Serialize given Nodes
        StringBuilder rootList = new StringBuilder();
        serialize(root, rootList);
        String r = rootList.toString();

        StringBuilder subRootList = new StringBuilder();
        serialize(subRoot, subRootList);
        String s = subRootList.toString();

        // Check if s is in r
        return kmp(s, r);
    }

    // Function to serialize Tree
    private void serialize(TreeNode node, StringBuilder treeStr) {
        if (node == null) {
            treeStr.append("#");
            return;
        }

        treeStr.append("^");
        treeStr.append(node.val);
        serialize(node.left, treeStr);
        serialize(node.right, treeStr);
    }

    // Knuth-Morris-Pratt algorithm to check if `needle` is in `haystack` or not
    private boolean kmp(String needle, String haystack) {
        int m = needle.length();
        int n = haystack.length();

        if (n < m)
            return false;

        // longest proper prefix which is also suffix
        int[] lps = new int[m];
        // Length of Longest Border for prefix before it.
        int prev = 0;
        // Iterating from index-1. lps[0] will always be 0
        int i = 1;

        while (i < m) {
            if (needle.charAt(i) == needle.charAt(prev)) {
                // Length of Longest Border Increased
                prev += 1;
                lps[i] = prev;
                i += 1;
            } else {
                // Only empty border exist
                if (prev == 0) {
                    lps[i] = 0;
                    i += 1;
                } else {
                    // Try finding longest border for this i with reduced prev
                    prev = lps[prev - 1];
                }
            }
        }

        // Pointer for haystack
        int haystackPointer = 0;
        // Pointer for needle.
        // Also indicates number of characters matched in current window.
        int needlePointer = 0;

        while (haystackPointer < n) {
            if (haystack.charAt(haystackPointer) == needle.charAt(needlePointer)) {
                // Matched Increment Both
                needlePointer += 1;
                haystackPointer += 1;
                // All characters matched
                if (needlePointer == m)
                    return true;
            } else {
                if (needlePointer == 0) {
                    // Zero Matched
                    haystackPointer += 1;
                } else {
                    // Optimally shift left needlePointer. Don't change haystackPointer
                    needlePointer = lps[needlePointer - 1];
                }
            }
        }
        return false;
    }

    // V3
    // IDEA : TREE HASH
    // https://leetcode.com/problems/subtree-of-another-tree/editorial/
    // CONSTANTS
    final int MOD_1 = 1000000007;
    final int MOD_2 = 2147483647;

    // Hashing a Node
    long[] hashSubtreeAtNode(TreeNode node, boolean needToAdd) {

        if (node == null)
            return new long[] { 3, 7 };

        long[] left = hashSubtreeAtNode(node.left, needToAdd);
        long[] right = hashSubtreeAtNode(node.right, needToAdd);

        long left1 = (left[0] << 5) % MOD_1;
        long right1 = (right[0] << 1) % MOD_1;
        long left2 = (left[1] << 7) % MOD_2;
        long right2 = (right[1] << 1) % MOD_2;

        long[] hashpair = { (left1 + right1 + node.val) % MOD_1,
                (left2 + right2 + node.val) % MOD_2 };

        if (needToAdd)
            memo.add(hashpair);

        return hashpair;
    }

    // Vector to store hashed value of each node.
    List<long[]> memo = new ArrayList<>();

    public boolean isSubtree_4(TreeNode root, TreeNode subRoot) {

        // Calling and adding hash to List
        hashSubtreeAtNode(root, true);

        // Storing hashed value of subRoot for comparison
        long[] s = hashSubtreeAtNode(subRoot, false);

        // Check if hash of subRoot is present in memo
        for (long[] m : memo) {
            if (m[0] == s[0] && m[1] == s[1])
                return true;
        }

        return false;
    }

}
