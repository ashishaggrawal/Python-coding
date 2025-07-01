# Two Sum

Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. Each input has exactly one solution, and the same element may not be used twice.

```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

## Explanation

For each number, check whether its complement (target - num) has already been seen. A hash map from value to index makes each lookup O(1).

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Output

Running `python TwoSum.py` executes these examples:

```python
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([3, 3], 6))          # [0, 1]
```

Output:

```
[0, 1]
[1, 2]
[0, 1]
```
