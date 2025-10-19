"""
Longest Common Prefix — Problem Description

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Approach:
- Initialize the candidate prefix as the first string. For each subsequent string,
  shrink the prefix while it is not a prefix of the current string.

Complexity:
- Time: O(total length of all strings)
- Space: O(1)
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while prefix and not s.startswith(prefix):
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix


if __name__ == "__main__":
    tests = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interspecies", "interstellar", "interstate"],
        [""],
        [],
    ]
    solver = Solution()
    for arr in tests:
        print(arr, "->", solver.longestCommonPrefix(arr))


