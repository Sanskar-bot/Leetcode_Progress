# ============================================================
#  Problem : Diameter of Binary Tree
#  URL     : https://leetcode.com/problems/diameter-of-binary-tree/
#  Solution: https://leetcode.com/solutions/dfs-returning-depth-update-diameter-at-e-6x0p/
#  Date    : 2026-11-02
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The longest path in a tree bends at some node. At that node, the path length (in edges) is the depth of the left subtree plus the depth of the right subtree. So if I compute depths with recursion, I can check this sum at every node and keep the maximum.

# Approach
1. `walk(node)` returns the depth of the subtree rooted at `node` (0 for `None`).
2. At each node, get `left = walk(node.left)` and `right = walk(node.right)`.
3. Update the answer: `maxi = max(maxi, left + right)`, the longest path through this node.
4. Return `1 + max(left, right)` so the parent can use this node's depth.
5. Call `walk(root)` and return `maxi`.

# Complexity
- Time complexity: $$O(n)$$, because every node is visited once.

- Space complexity: $$O(h)$$ for the recursion stack, where `h` is the height of the tree.

# Code

# --- CODE ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0

        def walk(node):
            nonlocal maxi

            if node is None:
                return 0
            
            left=walk(node.left)
            right=walk(node.right)

            maxi=max(maxi,left+right)

            return 1+max(left , right)
            
        
        walk(root)
        return maxi

