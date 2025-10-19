# Merge Sorted Array

- Tag: two-pointers, array, in-place
- Intuition: merge two sorted arrays by comparing current elements and advancing pointers.
- Approach: merge into a temporary list, then write back into `nums1` in-place for clarity.
- Complexity: O(m + n) time, O(m + n) extra space (this version). A classic alternative uses O(1) extra space by filling from the end.

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
- Output: nums1 becomes [1,2,2,3,5,6]

## Run
```bash
python3 solution.py
```


