# Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.

```
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
Input: nums = [1], k = 1
Output: [1]
```

## Explanation

**Approach 1 (bucket sort):** a number can appear at most n times, so place each number in bucket[frequency] and read buckets from highest to lowest.

**Approach 2 (heap):** heapq.nlargest picks the k highest counts.

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Bucket sort | O(n) | O(n) |
| Heap | O(n log k) | O(n) |

## Output

Running `python TopKFrequentElements.py` executes these examples:

```python
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))       # [1, 2]
print(top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(top_k_frequent([1], 1))                      # [1]
```

Output:

```
[1, 2]
[1, 2]
[1]
```
