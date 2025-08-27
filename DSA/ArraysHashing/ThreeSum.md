# 3Sum

Given an integer array nums, return all unique triplets [a, b, c] such that a + b + c == 0. The result must not contain duplicate triplets.

```
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Input: nums = [0, 0, 0]
Output: [[0, 0, 0]]
```

## Explanation

Sort, then fix each number as the first element and use two pointers on the rest to find pairs summing to its negative. Skip equal neighbours to avoid duplicates.

## Complexity

- **Time:** O(n^2)
- **Space:** O(1) extra (ignoring the sort and output)

## Output

Running `python ThreeSum.py` executes these examples:

```python
print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 1, 1]))              # []
print(three_sum([0, 0, 0]))              # [[0, 0, 0]]
```

Output:

```
[[-1, -1, 2], [-1, 0, 1]]
[]
[[0, 0, 0]]
```
