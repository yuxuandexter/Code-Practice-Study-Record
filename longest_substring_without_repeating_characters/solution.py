"""
Longest Substring Without Repeating Characters — Problem Description

Given a string s, find the length of the longest substring without repeating
characters.

Approaches:
- Brute force expand from each index until a repeat → O(n^2)
- Sliding window with a set or map to track characters → O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force method
        # loop through all characters
        max_len = 0
        max_str = ""
        for idx in range(len(s)):
            cur_idx = idx
            # loop through subsequence strings to count unique characters
            temp_str = s[idx]
            temp_unique_count = 1
            for next_idx in range(len(s[cur_idx + 1:])):
                #convert to global index
                conver_next_idx = next_idx + cur_idx + 1
                next_str = s[conver_next_idx]
                # update temp_str and count unique character
                if next_str in temp_str:
                    break
                else:
                    temp_str += s[conver_next_idx]
                    temp_unique_count += 1
            
            # update max len and max str
            if temp_unique_count > max_len:
                max_str = temp_str
                max_len = temp_unique_count
        return max_len


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
    print(Solution().lengthOfLongestSubstring("bbbbb"))     # 1
    print(Solution().lengthOfLongestSubstring("pwwkew"))    # 3


