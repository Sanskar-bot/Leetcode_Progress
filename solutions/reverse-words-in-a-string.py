# ============================================================
#  Problem : Reverse Words in a String
#  URL     : https://leetcode.com/problems/reverse-words-in-a-string/
#  Solution: https://leetcode.com/solutions/reverse-words-in-a-string-two-pointers-o-x82n/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Reverse Words in a String | LeetCode 151

## Intuition

The objective is to reverse the order of words in a string while ensuring that there are no unnecessary leading, trailing, or consecutive spaces in the result.

We can approach this by treating each word as an individual element and reversing their order using the **Two Pointers technique**.

The key observation is that once the words are separated, we only need to swap the words at the beginning and end of the collection, gradually moving towards the centre.

## Approach

1. First, separate the string into individual words. This also automatically handles multiple spaces and removes leading and trailing spaces.
2. Initialize two pointers:
   - `start` at the first word.
   - `end` at the last word.
3. While `start` is less than `end`:
   - Swap the words at these two positions.
   - Move `start` one position forward.
   - Move `end` one position backward.
4. Continue until both pointers meet or cross.
5. Finally, combine the reversed words into a single string with exactly one space between consecutive words.

This approach avoids manually reversing characters and focuses only on rearranging the order of words.

## Complexity

- **Time Complexity:** O(n), where n is the length of the input string. Splitting, reversing the word list, and joining the words each take linear time.

- **Space Complexity:** O(n), as we create a separate collection of words and a resulting string.
# Code

# --- CODE ---
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()

        start=0
        end=len(s)-1

        while start<end:
            s[start] , s[end] = s[end] , s[start]
            start+=1
            end-=1

        return " ".join(s)

