# ============================================================
#  Problem : Top K Frequent Elements
#  URL     : https://leetcode.com/problems/top-k-frequent-elements/
#  Solution: https://leetcode.com/solutions/python-hashmap-count-sort-by-frequency-o-ecgs/
#  Date    : 2026-10-19
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The answer depends on how often each number appears, so the first step is to count frequencies. Once I have the counts, the problem reduces to picking the k numbers with the highest counts.

# Approach
1. Use a `defaultdict(int)` to count how many times each number appears in `nums`.
2. Sort the dict's keys by their count in descending order using `key=freq.get` and `reverse=True`.
3. Slice the first `k` elements with `[:k]` and return them.

# Complexity
- Time complexity: $$O(n \log n)$$. Counting takes O(n), and sorting up to n distinct elements takes O(n log n).
- Space complexity: $$O(n)$$ for the frequency dictionary.

This is the simple version. It can be improved to $$O(n \log k)$$ with a min-heap, or $$O(n)$$ with bucket sort.

# Code

# --- CODE ---
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq=defaultdict(int)
        for number in nums:
            freq[number]+=1
        return sorted(freq, key=freq.get , reverse=True )[:k]

