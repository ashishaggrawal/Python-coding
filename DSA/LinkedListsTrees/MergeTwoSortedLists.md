# Merge Two Sorted Lists

Given the heads of two sorted linked lists, merge them into one sorted list by splicing their nodes together, and return its head.

```
Input: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

## Explanation

A dummy head removes the special case for the first node. Repeatedly attach the smaller front node, then attach whatever remains of the other list.

## Complexity

- **Time:** O(n + m)
- **Space:** O(1) (existing nodes are reused, not copied)

## Output

Running `python MergeTwoSortedLists.py` executes these examples:

```python
print(to_list(merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))))  # [1, 1, 2, 3, 4, 4]
print(to_list(merge_two_lists(build_list([]), build_list([0]))))              # [0]
```

Output:

```
[1, 1, 2, 3, 4, 4]
[0]
```
