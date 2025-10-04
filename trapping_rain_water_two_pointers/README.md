# Trapping Rain Water (Two Pointers)

- Tag: two pointers
- Intuition: water trapped at a bar depends on the shorter side between left_max and right_max
- Approach: use two pointers from both ends; move the side with the smaller height, update max, and accumulate water
- Complexity: O(n) time, O(1) extra space

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
- Output: 6

## Run
```bash
python3 solution.py
```
