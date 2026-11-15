# ============================================================
#  Problem : Number of Sub-arrays With Odd Sum
#  URL     : https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
#  Solution: https://leetcode.com/solutions/prefix-sum-parity-count-evenodd-prefixes-gba8/
#  Date    : 2026-11-15
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A sub-array sum is odd only when its prefix sum has a **different parity** than the prefix before it. So instead of checking every sub-array, we track how many prefix sums are even vs odd as we scan the array. Every time the current prefix is even, it pairs with all previous odd prefixes (and vice versa) to form an odd-sum sub-array.

# Approach
We use a running prefix sum and count parities:

- `even` = number of prefix sums seen so far that are even (start with `even = 1` for the empty prefix of sum 0).
- `odd` = number of prefix sums seen so far that are odd.

For each element `x`:
1. Add it to `prefix`.
2. If `prefix` is **even**: every earlier **odd** prefix forms an odd-sum sub-array → `count += odd`, then increment `even`.
3. If `prefix` is **odd**: every earlier **even** prefix forms an odd-sum sub-array → `count += even`, then increment `odd`.

Return `count % (10**9 + 7)`.

# Complexity
- Time complexity: $$O(n)$$ — single pass through the array.
- Space complexity: $$O(1)$$ — only a few counters.

# Code
```python3
class Solution:
    def numOfSubarrays(self, arr: list[int]) -&gt; int:
        even, odd = 1, 0      # empty prefix (sum 0) counts as even
        prefix = 0
        count = 0
        for x in arr:
            prefix += x
            if prefix % 2 == 0:
                count += odd      # pair with earlier odd prefixes
                even += 1
            else:
                count += even     # pair with earlier even prefixes
                odd += 1
        return count % (10**9 + 7)

# --- CODE ---


