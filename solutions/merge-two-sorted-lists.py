# ============================================================
#  Problem : Merge Two Sorted Lists
#  URL     : https://leetcode.com/problems/merge-two-sorted-lists/
#  Solution: https://leetcode.com/solutions/two-pointers-merge-onm-time-o1-space-pyt-wmcu/
#  Date    : 2026-10-30
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Both lists are already sorted, so the smallest remaining node is always at the front of one of them. If I repeatedly take the smaller front node and attach it to the result, the merged list comes out sorted.

# Approach
1. Handle the empty cases: if one list is empty, return the other.
2. Pick the smaller head as the head of the result. Keep `sortedp` as a pointer to the last node of the merged list so far.
3. While both `list1p` and `list2p` are not `None`:
   - Compare `list1p.val` and `list2p.val`.
   - Attach the smaller node to `sortedp.next` and move that list's pointer forward.
   - Move `sortedp` forward.
4. When one list runs out, the rest of the other list is already sorted, so attach it with `sortedp.next = list1p if list1p else list2p`.
5. Return the head of the merged list.

No new nodes are created. The existing nodes are just relinked.

# Complexity
- Time complexity: $$O(n + m)$$, because each node of both lists is visited once.

- Space complexity: $$O(1)$$, because only a few pointers are used and the nodes are reused.

# Code

# --- CODE ---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        list1p=list1
        list2p=list2
        if(list1p==None):
            return list2
        if(list2p==None):
            return list1
        if(list1p.val<=list2p.val):
            sortedp=list1p
            sortedh=list1p
            list1p=list1p.next
        else:
            sortedp=list2p
            sortedh=list2p
            list2p=list2p.next

        while list1p and list2p:
            if(list1p.val<=list2p.val):
                print(list1p.val)
                sortedp.next=list1p
                list1p=list1p.next
                sortedp=sortedp.next
                
            else:
                print(list2p.val)
                sortedp.next=list2p
                list2p=list2p.next
                sortedp=sortedp.next
        sortedp.next = list1p if list1p else list2p
        return sortedh

