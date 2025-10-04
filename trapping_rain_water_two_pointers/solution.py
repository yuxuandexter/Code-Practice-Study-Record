"""
Trapping Rain Water — Problem Description

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Approach (Two Pointers, Tag: two pointers):
- Maintain two pointers at the left and right ends, along with left_max and right_max.
- Move the pointer at the side with the smaller bar inward, updating the side's max.
- The water trapped at the current position is max_so_far - current_height on that side.

Example:
  Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # set up the left and right pointers
        left_idx, right_idx = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        # core logic is like climbing from right side or left side
        while left_idx < right_idx:
            # climb from left side due to higher bar in right side
            if height[left_idx] <= height[right_idx]:
                left_max = max(left_max, height[left_idx])
                # we calculate water per step so we will deduct max left bar - current left bar (pointer)
                water += (left_max - height[left_idx])
                # update left idx
                left_idx += 1
            else:
                right_max = max(right_max, height[right_idx])
                water += (right_max - height[right_idx])
                right_idx -= 1

        return water


if __name__ == "__main__":
    # basic sanity run
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected: 6


