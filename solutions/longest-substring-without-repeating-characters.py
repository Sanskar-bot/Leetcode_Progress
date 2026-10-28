# ============================================================
#  Problem : Longest Substring Without Repeating Characters
#  URL     : https://leetcode.com/problems/longest-substring-without-repeating-characters/
#  Solution: https://leetcode.com/solutions/python-sliding-window-set-on-by-sanskar_-mh96/
#  Date    : 2026-10-19
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A valid substring has no repeated characters. Instead of checking every substring, I can keep a "window" that always holds unique characters and slide it across the string.

# Approach
1. Keep a `set` called `seen` with the characters currently in the window, plus two pointers: `left` and `right`.
2. Move `right` forward one character at a time.
3. If `s[right]` is already in `seen`, the window has a duplicate. Remove `s[left]` from the set and move `left` forward until the duplicate is gone.
4. Add `s[right]` to the set, then update the answer with the window size, `right - left + 1`.
5. After the loop, return the largest size seen.

# Complexity
- Time complexity: $$O(n)$$. Each character is added to the set once and removed at most once, so both pointers only move forward.
- Space complexity: $$O(min(n, m))$$, where m is the size of the character set, because the window never holds more than one of each character.

# Code

# --- CODE ---
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxlen = 0
        for right in range(len(s)):
            while s[right] in seen:      # duplicate: shrink from the left
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxlen = max(maxlen, right - left + 1)
        return maxlen

