# ============================================================
#  Problem : Binary Tree Zigzag Level Order Traversal
#  URL     : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#  Solution: https://leetcode.com/solutions/simple-dfs-reverse-odd-levels-python3-on-6js2/
#  Date    : 2026-11-03
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
My first idea was to do a DFS and flip the left/right visiting order on odd depths. That failed, because the flip leaks into deeper levels: a level's order is inherited from its parents' order. So I kept the DFS order fixed (always left, then right), which collects every level left-to-right, and handled the zigzag direction separately.

# Approach
1. Use a recursive DFS with a `depth` parameter and a list of lists `zigzag`.
2. If `depth == len(zigzag)`, this is the first node of a new level, so append an empty list.
3. Append the node's value to `zigzag[depth]`.
4. Always recurse left first, then right.
5. After the traversal, reverse every odd-indexed level (1, 3, 5, ...).
6. Return `zigzag`.

# Complexity
- Time complexity: $$O(n)$$. Each node is visited once, and reversing the odd levels touches each node at most once more.

- Space complexity: $$O(n)$$ for the output, plus $$O(h)$$ for the recursion stack, where $$h$$ is the height of the tree.

# Code

# --- CODE ---
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        zigzag = []

        def zz(node, depth):
            if node is None:
                return
            if depth == len(zigzag):
                zigzag.append([])

            zigzag[depth].append(node.val)

            # always left first, so every level is collected left-to-right
            zz(node.left, depth + 1)
            zz(node.right, depth + 1)

        zz(root, 0)

        # reverse the odd levels after the traversal is done
        for i in range(1, len(zigzag), 2):
            zigzag[i].reverse()

        return zigzag

