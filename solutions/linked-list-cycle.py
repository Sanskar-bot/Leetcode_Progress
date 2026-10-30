# ============================================================
#  Problem : Linked List Cycle
#  URL     : https://leetcode.com/problems/linked-list-cycle/
#  Solution: https://leetcode.com/solutions/slow-and-fast-pointers-floyds-cycle-dete-nfzf/
#  Date    : 2026-10-30
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
If the list has a cycle, a fast pointer moving two steps at a time will eventually lap a slow pointer moving one step at a time, like two runners on a circular track. If there is no cycle, the fast pointer simply reaches the end of the list.

# Approach
1. Start `slow` and `fast` at `head`.
2. While `fast` and `fast.next` exist:
   - Move `slow` one step and `fast` two steps.
   - If `slow` and `fast` are the same node, there is a cycle, so return `True`.
3. If the loop ends, `fast` reached the end of the list, so there is no cycle. Return `False`.

The condition `fast and fast.next` guards both `fast.next` and `fast.next.next` from being read on `None`.

# Complexity
- Time complexity: $$O(n)$$. Without a cycle, `fast` reaches the end in about n/2 steps. With a cycle, `fast` catches `slow` within one extra lap around the cycle.

- Space complexity: $$O(1)$$, because only two pointers are used.

# Code

# --- CODE ---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while fast and fast.next:
             
            fast=fast.next.next
            slow=slow.next

            if(fast == slow):
                return True
                
        return False

