# ============================================================
#  Problem : Invert Binary Tree
#  URL     : https://leetcode.com/problems/invert-binary-tree/
#  Solution: https://leetcode.com/solutions/recursive-dfs-swap-children-at-every-nod-0zhj/
#  Date    : 2026-11-02
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Inverting a tree means every node's left and right children trade places. If I visit every node and swap its two children, the whole tree ends up mirrored.

# Approach
1. `check(node)` handles one node. If `node` is `None`, there is nothing to swap, so return.
2. Swap the node's children: `node.left, node.right = node.right, node.left`.
3. Recurse into `node.left` and `node.right` so every subtree is inverted too.
4. Call `check(root)` and return `root`. This also works for an empty tree, since `check(None)` just returns.

The tree is changed in place, so no new nodes are created.

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
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        def check(node):
            if node is None:    # both empty: mirror
                return
            node.left , node.right = node.right ,node.left
            

            check(node.left)   # outer pair
            check(node.right)   # inner pair

        check(root)
        return root

