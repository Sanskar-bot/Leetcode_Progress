# ============================================================
#  Problem : Binary Tree Preorder Traversal
#  URL     : https://leetcode.com/problems/binary-tree-preorder-traversal/
#  Solution: https://leetcode.com/solutions/recursive-preorder-traversal-node-left-r-fj1w/
#  Date    : 2026-11-01
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Preorder traversal visits the node first, then the left subtree, then the right subtree. That definition is already recursive: the preorder of a tree is its root value, followed by the preorder of the left subtree, followed by the preorder of the right subtree.

# Approach
1. If `root` is `None`, return an empty list (base case).
2. Otherwise, return `[root.val]` joined with the preorder of `root.left`, then the preorder of `root.right`.

Each call handles one node and trusts the recursion to handle the subtrees. Compared with inorder, only the position of `[root.val]` changes.

# Complexity
- Time complexity: $$O(n)$$, because every node is visited once. (Joining lists adds extra copying, which can cost more on very skewed trees.)

- Space complexity: $$O(h)$$ for the recursion stack, where `h` is the height of the tree, not counting the output.

# Code

# --- CODE ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        list1=[]

        if root is None:
            return []
        
        return ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))

