# Reverse Linked List

Given the head of a singly linked list, reverse the list and return the new head.

```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
```

## Explanation

Walk the list once, pointing each node's next back at the previous node. Save the next node first so the rest of the list is not lost.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Output

Running `python ReverseLinkedList.py` executes these examples:

```python
print(to_list(reverse_list(build_list([1, 2, 3, 4, 5]))))  # [5, 4, 3, 2, 1]
print(to_list(reverse_list(build_list([1, 2]))))           # [2, 1]
print(to_list(reverse_list(build_list([]))))               # []
```

Output:

```
[5, 4, 3, 2, 1]
[2, 1]
[]
```
