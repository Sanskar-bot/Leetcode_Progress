# ============================================================
#  Problem : Binary Tree Level Order Traversal
#  URL     : https://leetcode.com/problems/binary-tree-level-order-traversal/
#  Solution: https://leetcode.com/solutions/recursive-dfs-with-depth-on-time-python-3l841/
#  Date    : 2026-11-01
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Level order means grouping nodes by their depth. If I carry the depth down the recursion, each node knows which level's list it belongs to, so I can put its value straight into that list.

# Approach
1. Keep a result list `res`, where `res[d]` holds the values at depth `d`.
2. `levelo(node, depth)` visits one node. If `node` is `None`, return.
3. If `depth == len(res)`, this is the first node seen at this depth, so append a new empty list.
4. Append `node.val` to `res[depth]`.
5. Recurse on the left child, then the right child, with `depth + 1`. Visiting left before right keeps each level in left-to-right order.
6. Start with `levelo(root, 0)` and return `res`.

# Complexity
- Time complexity: $$O(n)$$, because every node is visited once.

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
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res=[]

        def levelo(root,depth):
            if root is None:
                return 
            if depth == len(res):
                res.append([])
            res[depth].append(root.val)
            levelo(root.left , depth+1)    
            levelo(root.right , depth+1)    
        
        levelo( root, 0)
        return res

