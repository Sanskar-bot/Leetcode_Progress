# ============================================================
#  Problem : Lowest Common Ancestor of a Binary Tree
#  URL     : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#  Solution: https://leetcode.com/solutions/recursive-dfs-return-p-q-or-lca-on-time-jhpl2/
#  Date    : 2026-11-02
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
If I search a subtree for `p` and `q`, there are only a few things it can tell me: it contains neither, it contains one of them, or it contains both. If `p` and `q` are found in two different child subtrees of a node, that node must be their lowest common ancestor.

# Approach
1. `search(node)` returns `p` or `q` if one of them is in this subtree, the LCA if both are, and `None` otherwise.
2. If `node` is `None`, return `None`. If `node` is `p` or `q`, return `node` (if one is an ancestor of the other, that ancestor is the LCA, so there is no need to look deeper).
3. Search the left and right children once each and store the results in `left` and `right`.
4. If both are non-`None`, `p` and `q` are on different sides, so return `node`.
5. Otherwise, return whichever side is non-`None` (or `None` if both are).
6. Return `search(root)`.

# Complexity
- Time complexity: $$O(n)$$, because every node is visited at most once.

- Space complexity: $$O(h)$$ for the recursion stack, where `h` is the height of the tree.

# Code

# --- CODE ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca=0

        def search(node):
            if node is None:
                return 
            if node == q or node == p:
                return node 

            left = search(node.left)          # change 1: call each child once and store it
            right = search(node.right)

            if left and right:                # change 2: both sides found something
                return node
            return left or right  
        
        return search(root)

