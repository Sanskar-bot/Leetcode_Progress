# ============================================================
#  Problem : Linked List Cycle II
#  URL     : https://leetcode.com/problems/linked-list-cycle-ii/
#  Solution: https://leetcode.com/solutions/floyds-cycle-detection-two-phases-on-tim-sg7o/
#  Date    : 2026-10-30
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A fast pointer (2 steps) and a slow pointer (1 step) will meet inside the cycle if one exists. At that meeting point, the distance from `head` to the cycle start equals the distance from the meeting point forward to the cycle start, so a second pass finds the start.

# Approach
1. Phase 1: move `slow` one step and `fast` two steps while `fast` and `fast.next` exist. If they meet, there is a cycle. If `fast` reaches the end, return `None`.
2. Phase 2: keep one pointer at the meeting point and put the other at `head`. Move both one step at a time until they are equal.
3. The node where they meet is the start of the cycle. Return it.

Why phase 2 works: let `a` be the distance from `head` to the cycle start, and `c` the cycle length. When `slow` and `fast` meet, `slow` has walked `a + b` steps (where `b` is how far into the cycle it is), and `fast` has walked twice as many, so `a + b` is a multiple of `c`. That means walking `a` more steps from the meeting point lands exactly on the cycle start, the same place a pointer from `head` reaches after `a` steps.

# Complexity
- Time complexity: $$O(n)$$, because phase 1 and phase 2 each take at most a linear number of steps.

- Space complexity: $$O(1)$$, because only two pointers are used.

# Code

# --- CODE ---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        while fast and fast.next:

            slow=slow.next
            fast=fast.next.next

            if(fast == slow):
                return self.valuecheck(fast , head)
        return None

    def valuecheck (self , fast , slow):
        while ( fast!=slow):
            fast=fast.next
            slow=slow.next

        return fast

