# Coin Change

Given coin denominations and an amount, return the fewest coins needed to make that amount, or -1 if it cannot be made. Each coin may be used any number of times.

```
Input: coins = [1, 2, 5], amount = 11
Output: 3   (5 + 5 + 1)
Input: coins = [2], amount = 3
Output: -1
```

## Explanation

Unbounded-knapsack DP. dp[a] = fewest coins to make amount a. For every amount, try each coin as the last one used: dp[a] = min(dp[a - coin] + 1). Greedy (always taking the largest coin) fails for coins like [1, 3, 4] and amount 6.

## Complexity

- **Time:** O(amount * len(coins))
- **Space:** O(amount)

## Output

Running `python CoinChange.py` executes these examples:

```python
print(coin_change([1, 2, 5], 11))  # 3
print(coin_change([2], 3))         # -1
print(coin_change([1], 0))         # 0
print(coin_change([1, 3, 4], 6))   # 2   (3 + 3; greedy would give 4 + 1 + 1)
```

Output:

```
3
-1
0
2
```
