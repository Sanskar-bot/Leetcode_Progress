# ============================================================
#  Problem : Remove Nth Node From End of List
#  URL     : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#  Solution: https://leetcode.com/solutions/two-pointers-one-pass-ol-time-o1-space-p-iyvo/
#  Date    : 2026-10-30
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The node to remove is the n-th from the end. If one pointer starts n nodes ahead of another and both move at the same speed, then when the front pointer reaches the last node, the back pointer is sitting just before the node to remove. That gives the position in a single pass, without counting the length first.

# Approach
1. Start `fast` and `slow` at `head`.
2. Move `fast` forward `n` steps to create a gap of `n` nodes.
3. If `fast` is now `None`, then `n` equals the length of the list, so the head is the node to remove. Return `head.next`.
4. Otherwise, move both pointers one step at a time while `fast.next` exists. When the loop ends, `fast` is on the last node and `slow` is on the node just before the target.
5. Skip the target with `slow.next = slow.next.next`.
6. Return `head`.

The check in step 3 handles the only case where the target has no node before it. A dummy node before the head would remove that special case.

# Complexity
- Time complexity: $$O(L)$$, where L is the length of the list, because the list is traversed once.

- Space complexity: $$O(1)$$, because only two pointers are used.

# Code

# --- CODE ---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        if fast is None:          # head is the target, no node before it
            return head.next

        while fast.next:          # stops slow one node BEFORE the target
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head

