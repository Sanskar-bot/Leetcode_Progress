# ============================================================
#  Problem : Group Anagrams
#  URL     : https://leetcode.com/problems/group-anagrams/
#  Solution: https://leetcode.com/solutions/group-anagrams-hashmap-26-letter-count-t-5x7m/
#  Date    : 2026-10-19
#  Author  : Sanskar_phougat
# ============================================================

# ----- WRITE-UP -----
# Intuition
Anagrams contain exactly the same letters in the same quantities. So if I turn each word into a "fingerprint" of its letter counts, all anagrams get the same fingerprint and can be grouped under it.

# Approach
1. Use a `defaultdict(list)` to map a fingerprint to the list of words that share it.
2. For each word, build a 26-slot list `count`, where index 0 is 'a' and index 25 is 'z'.
3. For each character, increment `count[ord(ch) - ord('a')]`.
4. Convert `count` to a tuple (lists are not hashable, tuples are) and use it as the dict key.
5. Append the word to that key's list. Return all the lists with `grouped.values()`.

# Complexity
- Time complexity: $$O(n \cdot k)$$, where n is the number of words and k is the length of the longest word. Each word is scanned once, with no sorting.
- Space complexity: $$O(n \cdot k)$$ to store the groups and keys (each key is a fixed 26-length tuple).

# Code

# ----- CODE -----
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped=defaultdict(list)
        for word in strs:
            count=[0]*26
            for s in word:
                count[ord(s) - ord('a')]+=1
            grouped[tuple(count)].append(word)
        return list(grouped.values())
