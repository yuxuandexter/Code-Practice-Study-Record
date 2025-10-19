# Longest Palindromic Substring (Expand Around Center)

- Tag: two-pointers, expand-around-center
- Intuition: a palindrome mirrors around its center; try every center.
- Approach: expand from each index as the center for both odd and even lengths, updating the best window when characters match.
- Complexity: O(n^2) time, O(1) space

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: s = "babad"
- Output: "bab" ("aba" is also valid)

## Run
```bash
python3 solution.py
```


