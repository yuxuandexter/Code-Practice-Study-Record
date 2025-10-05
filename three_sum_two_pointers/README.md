# Three Sum (Two Pointers)

- Tag: two pointers, sorting
- Intuition: sort first; fix one number and use two pointers to find pairs that sum to its opposite
- Approach: iterate i, skip duplicates; then two-pointer search on the remaining subarray
- Complexity: O(n^2) time, O(1) extra space (ignoring output)

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: nums = [-1,0,1,2,-1,-4]
- Output: [[-1,-1,2],[-1,0,1]]

## Run
```bash
python3 solution.py
```
