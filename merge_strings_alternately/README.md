# Merge Strings Alternately

- Tag: two-pointers, string
- Intuition: iterate with two pointers, appending from each string alternately.
- Approach: move pointers along `word1` and `word2`, appending characters when in bounds.
- Complexity: O(n + m) time, O(1) extra space

## Files
- `solution.py`: Python implementation with problem description in comments

## Example
- Input: word1 = "ab", word2 = "pqrs"
- Output: "apbqrs"

## Run
```bash
python3 solution.py
```


