# Combination Sum

Given an array of distinct integers candidates and a target, return all unique combinations of candidates that sum to target. The same number may be used any number of times.

```
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]
Input: candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

## Explanation

Backtracking. At each step choose a candidate at index >= start, so every combination is built in non-decreasing order and is never repeated. After exploring a choice, pop it to restore the state. Sorting lets the loop stop early once a candidate is too large.

## Complexity

- **Time:** O(n^(t/m)) in the worst case (t = target, m = smallest candidate)
- **Space:** O(t/m)

## Output

Running `python CombinationSum.py` executes these examples:

```python
print(combination_sum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]
print(combination_sum([2, 3, 5], 8))     # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(combination_sum([2], 1))           # []
```

Output:

```
[[2, 2, 3], [7]]
[[2, 2, 2, 2], [2, 3, 3], [3, 5]]
[]
```
