# Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

```
Input: s = "abcabcbb"
Output: 3   ("abc")
Input: s = "pwwkew"
Output: 3   ("wke")
```

## Explanation

Slide a window [left, right] and remember the last index of each character. When a character repeats inside the window, jump left to just past its previous index instead of shrinking one step at a time.

## Complexity

- **Time:** O(n)
- **Space:** O(min(n, alphabet size))

## Output

Running `python LongestSubstringWithoutRepeatingCharacters.py` executes these examples:

```python
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3
print(length_of_longest_substring(""))          # 0
```

Output:

```
3
1
3
0
```
