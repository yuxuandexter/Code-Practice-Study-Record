"""
Palindrome Number — Problem Description

Given an integer x, return true if x is a palindrome, and false otherwise.

Approach (Two Pointers):
- Convert the number to a string and compare characters from both ends moving inward.
- Time: O(k), Space: O(1) extra where k is number of digits.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # half iter steps
        x_str = str(x)
        iter_steps = len(x_str) //2 
        l, r = 0, len(x_str) - 1

        status = True
        idx = 0
        while idx < iter_steps:
            left_val = x_str[l + idx]
            right_val = x_str[r - idx]
            if left_val == right_val:
                idx += 1
            else:
                status = False
                break
        
        return status


if __name__ == "__main__":
    print(Solution().isPalindrome(121))   # True
    print(Solution().isPalindrome(-121))  # False
    print(Solution().isPalindrome(10))    # False


