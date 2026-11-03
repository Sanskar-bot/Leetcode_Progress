# ============================================================
#  Problem : Maximum Depth of Binary Tree
#  URL     : https://leetcode.com/problems/maximum-depth-of-binary-tree/
#  Solution: https://leetcode.com/solutions/recursive-dfs-return-depth-on-time-oh-sp-j3tk/
#  Date    : 2026-11-02
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The depth of a tree depends only on the depths of its two subtrees. An empty tree has depth 0, and any other tree is one level (the root) plus the deeper of its two subtrees. That definition is already recursive.

# Approach
1. If `root` is `None`, return 0 (base case: no node, no levels).
2. Otherwise, ask for the depth of the left subtree and the depth of the right subtree.
3. Return `1 + max(left, right)`. The 1 counts the current node, and `max` keeps the longer side.

Each call trusts the recursion to give the correct depth for its children and only combines the two answers. The values are built on the way back up, starting from the `None` children at the bottom.

# Complexity
- Time complexity: $$O(n)$$, because every node is visited exactly once.

- Space complexity: $$O(h)$$ for the recursion stack, where `h` is the height of the tree. This is $$O(\log n)$$ for a balanced tree and $$O(n)$$ for a chain-shaped tree.

# Code

# --- CODE ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

