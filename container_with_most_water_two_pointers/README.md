# Container With Most Water (Two Pointers)

- Tag: two pointers
- Intuition: the area is width × min(height_left, height_right); the shorter side limits the area.
- Approach: start two pointers at the ends, compute area each step, move the shorter side inward to search for a taller boundary while width shrinks.
- Complexity: O(n) time, O(1) extra space

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: height = [1,8,6,2,5,4,8,3,7]
- Output: 49

## Run
```bash
python3 solution.py
```


