# Linked List Cycle

Given the head of a linked list, return True if the list contains a cycle.

```
Input: 3 -> 2 -> 0 -> -4, where -4 points back to 2
Output: True
Input: 1 -> 2
Output: False
```

## Explanation

Floyd's Tortoise and Hare. A slow pointer moves 1 step and a fast pointer moves 2. If there is a cycle the fast pointer laps the slow one and they meet; otherwise the fast pointer reaches the end.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Output

Running `python LinkedListCycle.py` executes these examples:

```python
print(has_cycle(build_list_with_cycle([3, 2, 0, -4], 1)))  # True
print(has_cycle(build_list_with_cycle([1, 2], 0)))         # True
print(has_cycle(build_list_with_cycle([1, 2], -1)))        # False
```

Output:

```
True
True
False
```
