"""
Median of Two Sorted Arrays — Problem Description

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays. The overall run time complexity
should be O(log (m + n)).

Approaches:
- Brute force (two-pointer merge) → O(m + n)
- Binary search on partition (preferred) → O(log (m + n))
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search
        # core concept: we dont need to sort everything so we compared the partion left right in both nums1 and nums2

        # partition smaller array
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2

        # track A parition
        l, r = 0, len(A) - 1
        total_len = len(A) + len(B)
        half = (total_len) // 2

        # loop through different partitions
        while True:
            # A partition index
            # if l = r = len(A) - 1, the whole A is at the left side of merged array
            # if l = r = 0, the whole A is at the right side of merged array
            A_p_idx = (l + r) // 2
            B_p_idx = half - A_p_idx - 2

            # edge case: the whole A is at the right side of merged array so we set it as -inf
            Aleft = float("-inf") if A_p_idx < 0 else A[A_p_idx]
            # edge case: the whole A is at the left side of merged array so we set it as inf
            Aright = float("inf") if (A_p_idx + 1) >= len(A) else A[A_p_idx + 1]
            Bleft = float("-inf") if B_p_idx < 0 else B[B_p_idx]
            Bright = float("inf") if (B_p_idx + 1) >= len(B) else B[B_p_idx + 1]

            # check successful partition
            if Aleft <= Bright and Bleft <= Aright:
                if total_len % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            # update A parition by updating l, r
            # A left parition should be smaller
            elif Aleft > Bright:
                r -= 1
            # a right partition should be larger
            elif Aright < Bleft:
                l += 1


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))  # 2.0
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))  # 2.5


