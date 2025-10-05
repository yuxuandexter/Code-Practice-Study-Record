"""
Three Sum — Problem Description

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Approach (Two Pointers):
- Sort the array
- For each index i, skip duplicates for nums[i]
- Use two pointers l and r to search pairs whose sum equals -nums[i]

Time: O(n^2), Space: O(1) extra (excluding output)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # just two sum extension but core concept is to utilize sort to reduce time complexity
        sorted_nums = sorted(nums)
        seen_val = set()
        all_tuplets = []
        
        prev_num1s = []
        # loop through sorted nums and begin with idx1
        for idx1, num1 in enumerate(sorted_nums):
            # one worst case is to have many 0 to cause time limit
            # escape duplicate nums1
            if num1 in prev_num1s:
                continue

            # assign two points like two sum
            l, r = idx1 + 1, len(nums) - 1
            target_value = 0 - num1
            while l < r:
                num2 = sorted_nums[l]
                num3 = sorted_nums[r]
                sum_val =  num2 + num3

                # compare with target value
                # larger than target value to decrease r

                if sum_val > target_value:
                    r -= 1
                elif sum_val < target_value:
                    l += 1
                else:
                    value_tuple = tuple(sorted((num1, num2, num3)))
                    if value_tuple not in seen_val:
                        seen_val.add(value_tuple)
                        all_tuplets.append([num1, num2, num3])
                        prev_num1s.append(num1)
                    l += 1
                    r -= 1
                    # accelerate inner loop for duplicate values
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1


                

        return all_tuplets


if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))  # [[-1, -1, 2], [-1, 0, 1]]


