# Longest Substring Without Repeating Characters

- Tag: string, brute force
- Intuition: expand a substring starting at each index until a repeat is seen
- Approaches:
  - Brute force expand-and-check: O(n^2) time, O(n) space (current window)
  - Sliding window with set/map (preferred): O(n) time, O(min(n, alphabet)) space

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: s = "abcabcbb"
- Output: 3 (substring "abc")

## Run
```bash
python3 solution.py
```
