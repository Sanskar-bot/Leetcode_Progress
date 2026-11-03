# ============================================================
#  Problem : Binary Tree Inorder Traversal
#  URL     : https://leetcode.com/problems/binary-tree-inorder-traversal/
#  Solution: https://leetcode.com/solutions/recursive-inorder-traversal-left-node-ri-5jsa/
#  Date    : 2026-11-01
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Inorder traversal visits the left subtree first, then the node itself, then the right subtree. That definition is already recursive: the traversal of a tree is the traversal of its left subtree, followed by the root, followed by the traversal of its right subtree.

# Approach
1. If `root` is `None`, return an empty list (base case).
2. Start with an empty list `list1`.
3. If there is a left child, add the inorder traversal of the left subtree to `list1`.
4. Append `root.val`.
5. If there is a right child, add the inorder traversal of the right subtree to `list1`.
6. Return `list1`.

Each call handles one node and trusts the recursion to handle the subtrees.

# Complexity
- Time complexity: $$O(n)$$, because every node is visited once. (List joining adds extra copying, which can cost more on very skewed trees.)

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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        list1 = []

        if root is None:
            return list1

        if root.left:
            list1=list1+self.inorderTraversal(root.left)

        list1.append(root.val)

        if root.right:
            list1=list1+self.inorderTraversal(root.right)
            
        return list1

