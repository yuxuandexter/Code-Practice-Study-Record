# Median of Two Sorted Arrays (Binary Search)

- Tag: binary search
- Intuition: we don't need to fully merge; we only need the median. Partition the two arrays so left parts contain half the elements and all left values <= right values.
- Approaches:
  - Brute force two-pointers merge: O(m + n) time, O(m + n) space
  - Binary search on partition (preferred): O(log(m + n)) time, O(1) space

## Binary Search Partition Details
- Goal: choose partitions so left side has half the total elements and every left element ≤ every right element.
- Let `A` be the shorter array and `B` the other.
- Define indices and boundary values:
  - `A_p_idx = (l + r) // 2`
  - `B_p_idx = half - A_p_idx - 2`
  - `Aleft = A[A_p_idx]` if `A_p_idx >= 0` else `-inf`
  - `Aright = A[A_p_idx + 1]` if `A_p_idx + 1 < len(A)` else `+inf`
  - `Bleft = B[B_p_idx]` if `B_p_idx >= 0` else `-inf`
  - `Bright = B[B_p_idx + 1]` if `B_p_idx + 1 < len(B)` else `+inf`
- Partition intent:
  - `Aleft` and `Bleft` belong to the left partition of the merged order
  - `Aright` and `Bright` belong to the right partition
- Correct partition condition: `Aleft ≤ Bright` and `Bleft ≤ Aright`.
- Adjust search on `A`:
  - If `Aleft > Bright`, move left: `r = A_p_idx - 1`.
  - Else if `Aright < Bleft`, move right: `l = A_p_idx + 1`.
- Compute median once partition is correct:
  - If total length is even: `(max(Aleft, Bleft) + min(Aright, Bright)) / 2`.
  - If odd: `min(Aright, Bright)`.

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: nums1 = [1,3], nums2 = [2]
- Output: 2.0

## Run
```bash
python3 solution.py
```
