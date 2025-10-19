# Longest Common Prefix

- Tag: string, prefix
- Intuition: shrink a candidate prefix until all strings start with it.
- Approach: initialize prefix as the first string, then iteratively shorten while others don't start with it.
- Complexity: O(sum of string lengths)

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: ["flower","flow","flight"]
- Output: "fl"

## Run
```bash
python3 solution.py
```


