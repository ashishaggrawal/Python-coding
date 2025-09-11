# Longest Repeating Character Replacement

Given a string s of uppercase letters and an integer k, you may change at most k characters to any other uppercase letter. Return the length of the longest substring that can be made of a single repeated letter.

```
Input: s = "ABAB", k = 2
Output: 4
Input: s = "AABABBA", k = 1
Output: 4
```

## Explanation

A window is valid if (window length - count of its most frequent letter) <= k, since that many letters need replacing. Grow the window to the right and shift left by one whenever it becomes invalid. max_freq never needs to decrease: only a higher max_freq can produce a longer answer.

## Complexity

- **Time:** O(n)
- **Space:** O(26)

## Output

Running `python LongestRepeatingCharacterReplacement.py` executes these examples:

```python
print(character_replacement("ABAB", 2))     # 4
print(character_replacement("AABABBA", 1))  # 4
```

Output:

```
4
4
```
