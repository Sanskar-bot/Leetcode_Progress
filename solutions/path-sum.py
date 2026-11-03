# ============================================================
#  Problem : Path Sum
#  URL     : https://leetcode.com/problems/path-sum/
#  Solution: https://leetcode.com/solutions/path-sum-recursive-dfs-with-root-to-leaf-f473/
#  Date    : 2026-11-03
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
My initial thought was to traverse the tree recursively while maintaining the sum of the nodes visited along the current path.

As I move down the tree, I add the current node's value to the accumulated sum. Since each recursive call receives its own sum, I don't need to manually subtract values while backtracking.

A path is considered valid only when it reaches a leaf node and its accumulated sum equals the target sum.

# Approach
1. Use recursive DFS to traverse the binary tree.
2. If the current node is None, return False because no valid path exists through it.
3. Add the current node's value to the accumulated path sum.
4. Check whether the current node is a leaf (both left and right children are None).
5. If it is a leaf, compare the accumulated sum with the target sum and return the result.
6. Otherwise, recursively explore the left and right subtrees.
7. Return `left or right` because finding a valid path in either subtree is sufficient.
8. Start the recursion from the root with an initial sum of 0.

# Complexity
- Time complexity: O(n)
  - Each node is visited at most once.

- Space complexity: O(h)
  - The recursive call stack requires space proportional to the height of the tree. In the worst case, O(n) for a skewed tree and O(log n) for a balanced tree.

# Code

# --- CODE ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        sum=0
        def pathsum(node , psum):
            if node is None:
                return False
            
            psum=psum+node.val

            

            if node.left is None and node.right is None:
                if psum == targetSum:
                    return True
                else:
                    return False
            
            

            left=pathsum(node.left , psum)
            right=pathsum(node.right , psum)

            

            return left or right 

        return pathsum(root , 0)

