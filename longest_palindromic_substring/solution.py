"""
Longest Palindromic Substring — Problem Description

Given a string s, return the longest palindromic substring in s.

Intuition:
- A palindrome mirrors around its center. For each index, expand around
  it as the center to check both odd-length and even-length palindromes.

Approach:
- For each index i, expand with (l=i, r=i) for odd lengths and (l=i, r=i+1)
  for even lengths while s[l] == s[r]. Track the max substring.

Complexity:
- Time: O(n^2) in the worst case (expanding around each center)
- Space: O(1)
"""

from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # odd length and even length
        # use expansion to check condition
        # reduce time complexity to n^2

        max_len = 0
        max_str = ""

        for (i, letter) in enumerate(s):

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp_str = s[l:r+1]
                if len(temp_str) > max_len:
                    max_len = len(temp_str)
                    max_str = temp_str
                l -= 1
                r +=1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp_str = s[l:r+1]
                if len(temp_str) > max_len:
                    max_len = len(temp_str)
                    max_str = temp_str
                l -= 1
                r +=1
        return max_str


if __name__ == "__main__":
    examples: List[str] = [
        "babad",  # possible answers: "bab" or "aba"
        "cbbd",   # answer: "bb"
        "a",      # answer: "a"
        "ac",     # answer: "a" or "c"
        ""        # answer: ""
    ]
    solver = Solution()
    for example in examples:
        print(example, "->", solver.longestPalindrome(example))


