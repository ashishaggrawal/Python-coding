# Valid Palindrome

Given a string s, return True if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

```
Input: s = "A man, a plan, a canal: Panama"
Output: True
Input: s = "race a car"
Output: False
```

## Explanation

Two pointers move inward from both ends, skipping characters that are not letters or digits, and compare the rest case-insensitively. No cleaned copy is built.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Output

Running `python ValidPalindrome.py` executes these examples:

```python
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
print(is_palindrome(" "))                               # True
```

Output:

```
True
False
True
```
