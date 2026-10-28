# ============================================================
#  Problem : Merge Intervals
#  URL     : https://leetcode.com/problems/merge-intervals/
#  Solution: https://leetcode.com/solutions/python-sort-one-pass-merge-on-log-n-by-s-jjoq/
#  Date    : 2026-10-19
#  Author  : Sanskar_phougat
# ============================================================

# ----- WRITE-UP -----
# Intuition
Two intervals can only overlap if they are next to each other once sorted by start time. So if I sort first, I only need to compare each interval with the one being built, not with every other interval.

# Approach
1. Sort the intervals by their start value.
2. Walk through them with an index `i`. Take the current interval as `start` and `end`.
3. While the next interval starts at or before `end` (`<=`, so touching intervals like `[1,4]` and `[4,5]` merge), absorb it by setting `end = max(end, next_end)`. Using `max` keeps the end correct when one interval sits fully inside another, like `[1,10]` and `[2,3]`.
4. When the next interval no longer overlaps, append `[start, end]` to the result and continue from there.

# Complexity
- Time complexity: $$O(n \log n)$$. The sort dominates, and the merge pass is $$O(n)$$ because `i` only moves forward.
- Space complexity: $$O(n)$$ for the result and the sorted copy.

# Code

# ----- CODE -----
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        intervals = sorted(intervals)
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1
            while i < len(intervals) and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                i += 1
            result.append([start, end])
        return result
