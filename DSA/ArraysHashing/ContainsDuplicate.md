# Contains Duplicate

Given an integer array nums, return True if any value appears at least twice, and False if every element is distinct.

```
Input: nums = [1, 2, 3, 1]
Output: True
Input: nums = [1, 2, 3, 4]
Output: False
```

## Explanation

Add each number to a hash set and stop as soon as one is already there.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Output

Running `python ContainsDuplicate.py` executes these examples:

```python
print(contains_duplicate([1, 2, 3, 1]))                    # True
print(contains_duplicate([1, 2, 3, 4]))                    # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
```

Output:

```
True
False
True
```
