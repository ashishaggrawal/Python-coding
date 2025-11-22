# Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence (elements in order, not necessarily next to each other).

```
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4   ([2, 3, 7, 101])
Input: nums = [7, 7, 7, 7]
Output: 1
```

## Explanation

**Approach 1 (DP):** dp[i] = length of the longest increasing subsequence ending at i, built from every earlier j with nums[j] < nums[i].

**Approach 2 (patience sorting):** tails[k] is the smallest possible tail of an increasing subsequence of length k + 1. For each number, bisect finds the first tail >= it and replaces it (or appends if none). The length of tails is the answer.

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| DP | O(n^2) | O(n) |
| Patience sorting | O(n log n) | O(n) |

## Output

Running `python LongestIncreasingSubsequence.py` executes these examples:

```python
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))     # 4
print(length_of_lis_dp([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(length_of_lis([0, 1, 0, 3, 2, 3]))               # 4
print(length_of_lis([7, 7, 7, 7]))                     # 1
```

Output:

```
4
4
4
1
```
