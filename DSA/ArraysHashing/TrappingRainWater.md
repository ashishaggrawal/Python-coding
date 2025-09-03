# Trapping Rain Water

Given n non-negative integers representing an elevation map where each bar has width 1, compute how much water it can trap after raining.

```
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Input: height = [4, 2, 0, 3, 2, 5]
Output: 9
```

## Explanation

Water above a bar = min(tallest bar on its left, tallest on its right) - its height. Two pointers track the max from each side; whichever side has the smaller max is the limiting wall, so that side's water can be settled and its pointer moved.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Output

Running `python TrappingRainWater.py` executes these examples:

```python
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap([4, 2, 0, 3, 2, 5]))                    # 9
```

Output:

```
6
9
```
