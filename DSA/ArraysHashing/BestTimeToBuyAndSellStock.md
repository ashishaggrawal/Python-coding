# Best Time to Buy and Sell Stock

Given an array prices where prices[i] is the price of a stock on day i, return the maximum profit from buying on one day and selling on a later day. Return 0 if no profit is possible.

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5   (buy at 1, sell at 6)
Input: prices = [7, 6, 4, 3, 1]
Output: 0
```

## Explanation

In one pass, track the lowest price seen so far and the best profit from selling today at the current price.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Output

Running `python BestTimeToBuyAndSellStock.py` executes these examples:

```python
print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))     # 0
```

Output:

```
5
0
```
