# ============================================================
#  Problem : Symmetric Tree
#  URL     : https://leetcode.com/problems/symmetric-tree/
#  Solution: https://leetcode.com/solutions/recursive-dfs-compare-mirror-pairs-on-ti-irub/
#  Date    : 2026-11-02
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A tree is symmetric if its left subtree is a mirror image of its right subtree. Two trees are mirrors if their roots have equal values, the left child of one mirrors the right child of the other, and the right child of one mirrors the left child of the other.

# Approach
1. `check(node1, node2)` tells whether the two subtrees are mirrors of each other.
2. If both are `None`, they match, so return `True`.
3. If only one is `None`, or the values differ, return `False`.
4. Otherwise, compare the outer pair (`node1.left` with `node2.right`) and the inner pair (`node1.right` with `node2.left`). Return `True` only if both pairs are mirrors.
5. Start with `check(root.left, root.right)`.

# Complexity
- Time complexity: $$O(n)$$, because each node is visited at most once.

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
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def check(node1, node2):
            if node1 is None and node2 is None:    # both empty: mirror
                return True
            if node1 is None or node2 is None:     # only one empty: not a mirror
                return False
            if node1.val != node2.val:             # values differ: not a mirror
                return False

            tf1 = check(node1.left, node2.right)   # outer pair
            tf2 = check(node1.right, node2.left)   # inner pair
            return tf1 and tf2

        return check(root.left, root.right)

