# ============================================================
#  Problem : Binary Tree Postorder Traversal
#  URL     : https://leetcode.com/problems/binary-tree-postorder-traversal/
#  Solution: https://leetcode.com/solutions/recursive-postorder-traversal-left-right-3vvh/
#  Date    : 2026-11-01
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Postorder traversal visits the left subtree first, then the right subtree, and the node itself last. That definition is already recursive: the postorder of a tree is the postorder of its left subtree, followed by the postorder of its right subtree, followed by the root value.

# Approach
1. If `root` is `None`, return an empty list (base case).
2. Otherwise, return the postorder of `root.left`, joined with the postorder of `root.right`, joined with `[root.val]`.

Each call handles one node and trusts the recursion to handle the subtrees. Compared with preorder and inorder, only the position of `[root.val]` changes.

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
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        return (self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val])

