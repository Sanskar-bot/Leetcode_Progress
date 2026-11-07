# ============================================================
#  Problem : Reverse Words in a String III
#  URL     : https://leetcode.com/problems/reverse-words-in-a-string-iii/
#  Solution: https://leetcode.com/solutions/reverse-words-in-a-string-iii-two-pointe-gjyi/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Reverse Words in a String III | LeetCode 557

## Intuition

The objective is to reverse each individual word in a string while maintaining the original order of the words.

We can achieve this using the **Two Pointers technique**.

Instead of reversing the entire string or splitting it into separate words, we identify the boundaries of each word using spaces and reverse the characters within those boundaries.

Since Python strings are immutable, we first convert the string into a list of characters so that individual characters can be swapped.

## Approach

1. Convert the input string into a list of characters to allow in-place swapping.
2. Append an extra space at the end of the list. This acts as a sentinel character and ensures that the last word is also processed inside the loop.
3. Maintain a pointer `wstart` that tracks the starting index of the current word.
4. Traverse the character list:
   - Whenever a space is encountered, it indicates the end of the current word.
   - Use two pointers, `wstart` and `wend`, to reverse the characters between these boundaries.
   - Move `wstart` to the position immediately after the space.
5. Remove the extra space appended at the beginning of the process.
6. Convert the character list back into a string and return the result.

The two-pointer reversal works by swapping the characters at both ends and moving the pointers towards the centre until they meet.

## Complexity

- **Time Complexity:** O(n), where n is the length of the string. Each character is traversed and processed a constant number of times.

- **Space Complexity:** O(n), because we convert the immutable string into a mutable character list. The additional list requires linear space.

# Code

# --- CODE ---
class Solution:
    def reverseWords(self, s: str) -> str:

        s = list(s)
        s.append(' ')

        wstart = 0

        def rev(wstart, wend):
            while wstart < wend:
                s[wstart], s[wend] = s[wend], s[wstart]
                wstart += 1
                wend -= 1

        for i in range(len(s)):
            if s[i] == ' ':
                rev(wstart, i - 1)
                wstart = i + 1

        s.pop()

        return "".join(s)

