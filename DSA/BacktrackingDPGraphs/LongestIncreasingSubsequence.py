# Given an integer array nums, return the length of the longest strictly increasing
# subsequence (elements in order, not necessarily next to each other).
# Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4   ([2, 3, 7, 101])
# Input: nums = [7, 7, 7, 7]
# Output: 1

# Approach 1 (DP): dp[i] = length of the longest increasing subsequence ending at i,
# built from every earlier j with nums[j] < nums[i].
# Time: O(n^2)  Space: O(n)
#
# Approach 2 (patience sorting): tails[k] is the smallest possible tail of an increasing
# subsequence of length k + 1. For each number, bisect finds the first tail >= it and
# replaces it (or appends if none). The length of tails is the answer.
# Time: O(n log n)  Space: O(n)

from bisect import bisect_left


def length_of_lis_dp(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def length_of_lis(nums):
    tails = []
    for num in nums:
        i = bisect_left(tails, num)
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num
    return len(tails)


if __name__ == "__main__":
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))     # 4
    print(length_of_lis_dp([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(length_of_lis([0, 1, 0, 3, 2, 3]))               # 4
    print(length_of_lis([7, 7, 7, 7]))                     # 1
