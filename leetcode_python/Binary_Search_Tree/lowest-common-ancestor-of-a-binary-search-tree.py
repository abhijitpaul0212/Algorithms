"""

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

"""

# V0
# IDEA : LC 236
# V0
# IDEA : RECURSION + POST ORDER TRANSVERSAL
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        ### NOTE here
        # if not root or find p in tree or find q in tree
        # -> then we quit the recursion and return root

        ### NOTE : we compare `p == root` and  `q == root`
        if not root or p == root or q == root:
            return root
        ### NOTE here
        # -> WE DON'T need to have if root.left, if root.right logic, but get left, right directly (search to left, right)
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        ### NOTE here
        # find q and p on the same time -> LCA is the current node (root)
        # if left and right -> p, q MUST in left, right sub tree respectively

        ### NOTE : if left and right, means this root is OK for next recursive
        if left and right:
            return root
        ### NOTE here
        # if p, q both in left sub tree or both in right sub tree
        return left if left else right

# V0
# IDEA : RECURSION + POST ORDER TRANSVERSAL
### NOTE : we need POST ORDER TRANSVERSAL for this problem
#          -> left -> right -> root
#          -> we can make sure that if p == q, then the root must be p and q's "common ancestor"
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ### NOTE : we need to assign root.val, p, q to other var first (before they are changed)
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            ### NOTE : we need to `return` below func call   
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val: 
            ### NOTE : we need to `return` below func call   
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            ### NOTE : not root.val but root
            return root

# V0'
# IDEA : RECURSION + POST ORDER TRANSVERSAL
### NOTE : we need POST ORDER TRANSVERSAL for this problem
#          -> left -> right -> root
#          -> we can make sure that if p == q, then the root must be p and q's "common ancestor"
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root

        p_val = p.val
        q_val = q.val

        if root.val < p_val and root.val < q_val:
            return self.lowestCommonAncestor(root.right, p, q)

        elif root.val > p_val and root.val > q_val:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root

# V0''
# IDEA : TREE property + recursive (same code as LC 236)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root

        return left if left else right

# V0''
# IDEA : ITERATION
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node

# V0''
# IDEA : GO THROUGH ALL BST (no need to use BFS, or DFS, can just use BST property)
# THIS METHOD IS MORE GENERAL
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        pathp = self.findPath(root, p)
        pathq = self.findPath(root, q)
        res = root
        for i in range(1, min(len(pathp), len(pathq))):
            ### NOTE : we need to find Lowest common ancestor (LCA),
            #        -> so need to go through pathp, pathq, 
            #        -> and find the lowest overlap
            if pathp[i] == pathq[i]:
                res = pathp[i]
        return res

    def findPath(self, root, p):
        path = []
        ### NOTE : 
        #   -> here we use "BFS" like way go through the BST
        #   -> however, this is not a BFS, since we ONLY go throgh the BST with ONE ROUTE which has x
        #   -> (and also there is no queue here)
        while root.val != p.val:
            path.append(root)
            if p.val > root.val:
                root = root.right
            elif p.val < root.val:
                root = root.left
        # NOTE this : we append p to path
        path.append(p)
        return path

# V0'''
# IDEA : BST PROPERTY
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pointer = root
        while pointer:
            if p.val > pointer.val and q.val > pointer.val:
                pointer = pointer.right
            elif p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left
            else:
                return pointer

# V0''''
# IDEA : BST PROPERTY
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == q or root == p:
            return root
        if p.val < root.val and q.val < root.val:
            return  self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

# V1
# IDEA : RECURSION
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root

# V1''
# IDEA : ITERATION
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node

# V1'
# https://blog.csdn.net/coder_orz/article/details/51498796
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pointer = root
        while pointer:
            if p.val > pointer.val and q.val > pointer.val:
                pointer = pointer.right
            elif p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left
            else:
                return pointer
                
# V1''
# https://blog.csdn.net/coder_orz/article/details/51498796
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

# V1'''
# https://blog.csdn.net/coder_orz/article/details/51498796
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathp = self.findPath(root, p)
        pathq = self.findPath(root, q)
        res = root
        for i in xrange(1, min(len(pathp), len(pathq))):
            if pathp[i] == pathq[i]:
                res = pathp[i]
        return res


    def findPath(self, root, p):
        path = []
        while root.val != p.val:
            path.append(root)
            if p.val > root.val:
                root = root.right
            elif p.val < root.val:
                root = root.left
        path.append(p)
        return path

# V2 
# Time:  O(n)
# Space: O(1)
class Solution(object):
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
            # Keep searching since root is outside of [s, b].
            root = root.left if s <= root.val else root.right
        # s <= root.val <= b.
        return root