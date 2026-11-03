# ============================================================
#  Problem : Intersection of Two Linked Lists
#  URL     : https://leetcode.com/problems/intersection-of-two-linked-lists/
#  Solution: https://leetcode.com/solutions/two-pointers-switch-heads-onm-time-o1-sp-0m97/
#  Date    : 2026-10-30
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
If the two lists have different lengths, pointers moving in step will not reach the intersection at the same time. But if each pointer walks its own list and then the other list, both walk the same total distance, so the length difference cancels out and they land on the intersection together.

# Approach
1. Start `a` at `headA` and `b` at `headB`.
2. While `a != b`:
   - Move `a` one step. If `a` is `None`, jump to `headB`.
   - Move `b` one step. If `b` is `None`, jump to `headA`.
3. Return `a`. It is the intersection node, or `None` if the lists do not intersect.

Why it works: let A have `x` nodes before the intersection, B have `y`, and both share `c` nodes. Pointer `a` travels `x + c + y` to reach the intersection after switching, and pointer `b` travels `y + c + x`. These are equal, so they meet there at the same time. With no intersection, both pointers travel `lenA + lenB` and become `None` together, so the loop ends and returns `None`. If the lengths are equal, they meet before any switch happens.

# Complexity
- Time complexity: $$O(n + m)$$, because each pointer walks at most both lists once.

- Space complexity: $$O(1)$$, because only two pointers are used and neither list is modified.

# Code

# --- CODE ---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

