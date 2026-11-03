# ============================================================
#  Problem : Balanced Binary Tree
#  URL     : https://leetcode.com/problems/balanced-binary-tree/
#  Solution: https://leetcode.com/solutions/balanced-binary-tree-bottom-up-dfs-with-c0rz0/
#  Date    : 2026-11-03
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
My initial thought was to calculate the height of the left and right subtrees for every node and check whether their height difference is at most 1.

Instead of maintaining a separate variable to track whether the tree is balanced, I can use -1 as a special indicator to represent an unbalanced subtree. This allows the recursive function to communicate both height and balance information through its return value.

# Approach
1. Use recursive DFS to calculate the height of each subtree.
2. If the current node is None, return 0.
3. Recursively calculate the heights of the left and right subtrees.
4. If either subtree returns -1, propagate -1 upwards because the subtree is already unbalanced.
5. Check whether the absolute difference between the left and right subtree heights is greater than 1. If so, return -1.
6. Otherwise, return 1 + max(left, right) to calculate the current node's height.
7. Finally, check whether the root returns -1. If it does, the tree is unbalanced; otherwise, it is balanced.

# Complexity
- Time complexity: O(n)
  - Each node is visited exactly once, and each height and balance check takes constant time.

- Space complexity: O(h)
  - The recursive DFS uses stack space proportional to the height of the tree. In the worst case (skewed tree), this becomes O(n), while for a balanced tree, it is O(log n).

# Code

# --- CODE ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        balanced=1
        def depth ( node , balanced ):
            if node is None:
                return 0

            left=depth(node.left ,balanced)
            right=depth(node.right , balanced)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1+max(left , right )

         
        if(depth(root , balanced ) == -1):
            return False 
        else:
            return True

