# ============================================================
#  Problem : Longest Common Prefix
#  URL     : https://leetcode.com/problems/longest-common-prefix/
#  Solution: https://leetcode.com/solutions/shrinking-prefix-prefix-safe-check-with-r79tu/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The common prefix of all strings can never be longer than the first string, so start with `strs[0]` as the answer and shorten it whenever another string disagrees. A prefix must match from the very start of the string, so the check has to compare only the beginning, not any substring in the middle.

# Approach
- Set `result = strs[0]`.
- For every other string `i`, shrink it one character at a time from the end until it matches the start of `result`.
- To test "does `i` match the start of `result`?", compare against `result[:len(i)]`. This slice is the same length as `i`, so `i in result[:len(i)]` is true only when the two are exactly equal, which makes it a prefix check and not a substring check.
- Once `i` matches, set `result = i`. This is the common prefix so far.
- If `i` shrinks to an empty string, `result` becomes `""` and stays empty for the remaining strings.
- Return `result` after all strings are processed.

# Complexity
- Time complexity:
$$O(S)$$, where $$S$$ is the total number of characters across all strings, since each string is shortened at most its own length.

- Space complexity:
$$O(1)$$ extra space, apart from the slices created while shrinking.

# Code

# --- CODE ---
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = strs[0]

        for i in strs[1:]:
            while i:
                if i in result[:len(i)]:
                    break
                i = i[:-1]
            result = i

        return result

