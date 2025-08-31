# Container With Most Water

Given an array height of n vertical lines, find two lines that together with the x-axis form a container holding the most water. Return that maximum amount.

```
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49   (lines at index 1 and 8: min(8, 7) * 7)
Input: height = [1, 1]
Output: 1
```

## Explanation

Start with the widest container and move the shorter line inward. Moving the taller line can never help, because the width shrinks and the height is still limited by the shorter line.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Output

Running `python ContainerWithMostWater.py` executes these examples:

```python
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_area([1, 1]))                       # 1
```

Output:

```
49
1
```
