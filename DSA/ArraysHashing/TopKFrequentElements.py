# Given an integer array nums and an integer k, return the k most frequent elements.
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
# Input: nums = [1], k = 1
# Output: [1]

# Approach 1 (bucket sort): a number can appear at most n times, so place each number
# in bucket[frequency] and read buckets from highest to lowest.
# Time: O(n)  Space: O(n)
#
# Approach 2 (heap): heapq.nlargest picks the k highest counts.
# Time: O(n log k)  Space: O(n)

import heapq
from collections import Counter


def top_k_frequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


def top_k_frequent_heap(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))       # [1, 2]
    print(top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(top_k_frequent([1], 1))                      # [1]
