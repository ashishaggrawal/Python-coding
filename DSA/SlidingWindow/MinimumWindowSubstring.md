# Minimum Window Substring

Given strings s and t, return the shortest substring of s that contains every character of t (including duplicates). Return "" if there is no such substring.

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Input: s = "a", t = "aa"
Output: ""
```

## Explanation

Keep one map of the counts t needs and one of the counts in the window. `formed` tracks how many distinct characters currently meet their required count. Expand right until the window is valid, then shrink from the left while it stays valid, recording the smallest window seen.

## Complexity

- **Time:** O(len(s) + len(t))
- **Space:** O(len(s) + len(t))

## Output

Running `python MinimumWindowSubstring.py` executes these examples:

```python
print(min_window("ADOBECODEBANC", "ABC"))  # BANC
print(min_window("a", "a"))                # a
print(repr(min_window("a", "aa")))         # ''
```

Output:

```
BANC
a
''
```
