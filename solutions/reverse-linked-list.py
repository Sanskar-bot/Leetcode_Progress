# ============================================================
#  Problem : Reverse Linked List
#  URL     : https://leetcode.com/problems/reverse-linked-list/
#  Solution: https://leetcode.com/solutions/iterative-pointer-reversal-on-time-o1-sp-yt5d/
#  Date    : 2026-10-30
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Reversing a linked list means making every node point to the node before it instead of the one after it. If I walk through the list once and flip each link as I go, the list ends up reversed. The only catch is that flipping a link loses the way forward, so I have to save the next node first.

# Approach
1. Keep two pointers: `pre` (the previous node, starts as `None`) and `cur` (the current node, starts at `head`).
2. While `cur` is not `None`:
   - Save the next node: `nxt = cur.next`.
   - Flip the link: `cur.next = pre`.
   - Move `pre` forward to `cur`.
   - Move `cur` forward to `nxt`.
3. When the loop ends, `cur` is `None` and `pre` is the last node of the original list, which is the new head. Return `pre`.

This also works for an empty list (returns `None`) and a one-node list (returns the same node) without any special cases.

# Complexity
- Time complexity: $$O(n)$$, because each node is visited exactly once.

- Space complexity: $$O(1)$$, because only a few pointers are used and the list is reversed in place.

# Code

# --- CODE ---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre=None
        cur=head

        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt

        return pre

