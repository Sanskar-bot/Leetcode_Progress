# ============================================================
#  Problem : Middle of the Linked List
#  URL     : https://leetcode.com/problems/middle-of-the-linked-list/
#  Solution: https://leetcode.com/solutions/slow-and-fast-pointers-on-time-o1-space-f9g8q/
#  Date    : 2026-10-30
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
If one pointer moves twice as fast as another, then when the fast pointer reaches the end of the list, the slow pointer has covered exactly half of it. So the slow pointer is sitting on the middle node.

# Approach
1. Start two pointers, `slow` and `fast`, at `head`.
2. While `fast` and `fast.next` both exist:
   - Move `slow` one step: `slow = slow.next`.
   - Move `fast` two steps: `fast = fast.next.next`.
3. When the loop ends, return `slow`.

The condition checks `fast` first so that `fast.next` is never read on `None` (even-length lists), and checks `fast.next` so that `fast.next.next` is never read on `None` (odd-length lists). For an even-length list this returns the second middle node, as the problem requires.

# Complexity
- Time complexity: $$O(n)$$, because `fast` visits each node at most once.

- Space complexity: $$O(1)$$, because only two pointers are used.

# Code

# --- CODE ---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        prev=head
        curr=head
        while curr and curr.next:
            prev=prev.next
            curr=curr.next.next
        return prev

