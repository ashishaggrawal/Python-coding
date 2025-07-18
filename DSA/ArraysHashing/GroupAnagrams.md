# Group Anagrams

Given an array of strings, group the anagrams together. An anagram uses exactly the same letters as another word, in a different order.

```
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

## Explanation

Anagrams share the same letter counts, so a tuple of 26 counts works as a dictionary key. This avoids sorting each word (O(k log k)) and costs O(k) per word.

## Complexity

- **Time:** O(n * k)
- **Space:** O(n * k)   (n words, k = longest word length)

## Output

Running `python GroupAnagrams.py` executes these examples:

```python
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams([""]))   # [['']]
print(group_anagrams(["a"]))  # [['a']]
```

Output:

```
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
[['']]
[['a']]
```
