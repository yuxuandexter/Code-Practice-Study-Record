"""
Two Sum — Problem Description

Given an integer array nums and an integer target, return indices of the two
numbers such that they add up to target.

Constraints:
- Exactly one solution exists.
- You may not use the same element twice.
- Indices can be returned in any order.

Example:
  Input:  nums = [2, 7, 11, 15], target = 9
  Output: [0, 1]  # because nums[0] + nums[1] == 9
"""

from typing import List, Dict


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of the two numbers that add up to target.

    Uses a single-pass hashtable that maps value -> index seen so far.
    Raises ValueError if no solution is found.
    """
    index_by_value: Dict[int, int] = {}

    for current_index, current_value in enumerate(nums):
        complement: int = target - current_value
        if complement in index_by_value:
            return [index_by_value[complement], current_index]
        index_by_value[current_value] = current_index

    raise ValueError("No two sum solution exists for the given input")


if __name__ == "__main__":
    example_nums = [2, 7, 11, 15]
    example_target = 9
    print(two_sum(example_nums, example_target))  # Expected: [0, 1]


