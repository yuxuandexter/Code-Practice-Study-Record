"""
Merge Strings Alternately — Problem Description

Given two strings word1 and word2, merge them by adding letters in alternating
order, starting with word1. If a string is longer than the other, append the
additional letters onto the end of the merged string.

Complexity:
- Time: O(n + m)
- Space: O(1) extra space (output excluded)
"""

from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1p, w2p = 0, 0
        new_str = ""

        while w1p < len(word1) or w2p < len(word2):
            if w1p < len(word1):
                new_str += word1[w1p]
                w1p += 1
            if w2p < len(word2):
                new_str += word2[w2p]
                w2p += 1
        
        return new_str


if __name__ == "__main__":
    tests = [
        ("ab", "pqrs"),
        ("abc", "pqr"),
        ("", "xyz"),
        ("hello", ""),
    ]
    solver = Solution()
    for w1, w2 in tests:
        print(f"{w1!r}, {w2!r} -> {solver.mergeAlternately(w1, w2)}")


