"""
Merge Sorted Array — Problem Description

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums2 into nums1 as one sorted array.

The final sorted array should not be returned by the function, but instead be stored inside
the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.

This implementation uses O(m + n) extra space for simplicity. A classic optimal approach uses O(1)
extra space by filling nums1 from the end backwards.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2 = 0, 0
        merged = []

        # Merge until one list is exhausted
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1

        # Append any leftovers
        if p1 < m:
            merged.extend(nums1[p1:m])
        if p2 < n:
            merged.extend(nums2[p2:n])

        # Write back into nums1 in-place
        nums1[:m+n] = merged


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)  # Expected: [1, 2, 2, 3, 5, 6]


