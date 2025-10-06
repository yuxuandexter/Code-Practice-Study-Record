"""
Container With Most Water — Problem Description

Given n non-negative integers `height[i]` where each represents a vertical line at
index i with height `height[i]`, find two lines that together with the x-axis form
a container that holds the most water. Return the maximum amount of water it can store.

Approach (Two Pointers, Tag: two pointers):
- Use two pointers at the ends of the array.
- At each step, compute area = (right_index - left_index) * min(height[left], height[right]).
- Move the pointer at the shorter line inward to potentially find a taller boundary.

Example:
  Input:  height = [1,8,6,2,5,4,8,3,7]
  Output: 49
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # apply two pointer to track  max_water

        l, r = 0, len(height) - 1

        # track max_water
        max_water = 0

        while l < r:
            # track value at pointers
            left_height = height[l]
            right_height = height[r]

            min_height = min(left_height, right_height)
            covered_water = (r - l) * min_height
            
            # update max_water
            if covered_water > max_water:
                max_water = covered_water
            
            # update l and r; update small one
            if left_height < right_height:
                l += 1
            else:
                r -= 1
        
        return max_water


if __name__ == "__main__":
    # basic sanity run
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # Expected: 49


