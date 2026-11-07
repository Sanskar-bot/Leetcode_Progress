# ============================================================
#  Problem : Longest Repeating Character Replacement
#  URL     : https://leetcode.com/problems/longest-repeating-character-replacement/
#  Solution: https://leetcode.com/solutions/sliding-window-window-size-max-frequency-r6ar/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
For any window of the string, the cheapest way to make it all one letter is to keep its most frequent letter and replace the rest. So a window is valid when `window size - count of most frequent letter <= k`. This suggests a sliding window that keeps growing while it is valid and slides forward when it is not.

# Approach
- Use a dictionary `counts` to store how many times each letter appears in the current window.
- Move `right` through the string, adding `s[right]` to `counts`, and update `max_freq` (the highest count of any single letter seen in a window).
- If `(right - left + 1) - max_freq > k`, the window needs too many replacements, so remove `s[left]` from `counts` and move `left` forward by one.
- After each step, update `best` with the current window size `right - left + 1`.
- `max_freq` is never lowered when the window shrinks. This is safe because the window can only grow beyond its previous best when a letter's real count exceeds the old `max_freq`, and at that point `max_freq` is updated anyway.
- Return `best`.

# Complexity
- Time complexity:
$$O(n)$$, where $$n$$ is the length of the string. Each character is added once and `left` only moves forward.

- Space complexity:
$$O(1)$$, since `counts` holds at most 26 uppercase letters.

# Code

# --- CODE ---
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_freq = 0
        best = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])

            if (right - left + 1) - max_freq > k:    # too many replacements needed
                counts[s[left]] -= 1                 # shrink from the left
                left += 1

            best = max(best, right - left + 1)

        return best

