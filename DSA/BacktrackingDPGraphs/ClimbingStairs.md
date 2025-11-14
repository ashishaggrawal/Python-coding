# Climbing Stairs

You are climbing a staircase with n steps and can climb 1 or 2 steps at a time. Return the number of distinct ways to reach the top.

```
Input: n = 2
Output: 2   (1+1, 2)
Input: n = 3
Output: 3   (1+1+1, 1+2, 2+1)
```

## Explanation

The last move is either 1 or 2 steps, so ways(n) = ways(n-1) + ways(n-2), the Fibonacci recurrence. Each state needs only the previous two, so two variables replace the full DP table.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Output

Running `python ClimbingStairs.py` executes these examples:

```python
print(climb_stairs(2))   # 2
print(climb_stairs(3))   # 3
print(climb_stairs(10))  # 89
```

Output:

```
2
3
89
```
