# Given an array prices where prices[i] is the price of a stock on day i, return the
# maximum profit from buying on one day and selling on a later day. Return 0 if no
# profit is possible.
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5   (buy at 1, sell at 6)
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0

# Approach: in one pass, track the lowest price seen so far and the best profit from
# selling today at the current price.
# Time: O(n)  Space: O(1)


def max_profit(prices):
    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))     # 0
