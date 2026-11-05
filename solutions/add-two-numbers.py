# ============================================================
#  Problem : Add Two Numbers
#  URL     : https://leetcode.com/problems/add-two-numbers/
#  Solution: https://leetcode.com/solutions/recursion-with-carry-digit-by-digit-omax-3qh5/
#  Date    : 2026-11-03
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The lists store the digits in reverse order, so the first nodes are the ones place. That matches how addition by hand works: add the lowest digits first, keep the digit, and pass the carry to the next position.

# Approach
1. `addl(node1, node2, carry)` returns the head of the sum list from these nodes onward.
2. If both nodes are `None` and `carry == 0`, there is nothing left to add, so return `None`.
3. Read each digit, using 0 when a list has run out, and compute `total = v1 + v2 + carry`.
4. Create a node with `total % 10`, and set its `next` to the recursive call on the next nodes with `total // 10` as the new carry.
5. Return the node. The `carry == 0` check in step 2 is what creates the extra final node when the last addition carries (for example `[5] + [5]` gives `[0,1]`).

# Complexity
- Time complexity: $$O(\max(n, m))$$, because each call handles one position.

- Space complexity: $$O(\max(n, m))$$ for the recursion stack and the new result list.

# Code

# --- CODE ---
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        def addl(node1, node2, carry):
            if node1 is None and node2 is None and carry == 0:
                return None

            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0
            total = v1 + v2 + carry

            node = ListNode(total % 10)
            node.next = addl(node1.next if node1 else None,
                             node2.next if node2 else None,
                             total // 10)
            return node

        return addl(l1, l2, 0)

