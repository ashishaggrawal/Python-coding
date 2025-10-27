# Binary Tree Level Order Traversal

Given the root of a binary tree, return the values of its nodes level by level, from left to right.

```
Input: [3, 9, 20, None, None, 15, 7]
Output: [[3], [9, 20], [15, 7]]
```

## Explanation

BFS with collections.deque. At the start of each level, the queue holds exactly that level's nodes, so process len(queue) nodes and collect their values.

## Complexity

- **Time:** O(n)
- **Space:** O(w) (w = maximum width of the tree)

## Output

Running `python BinaryTreeLevelOrderTraversal.py` executes these examples:

```python
print(level_order(build_tree([3, 9, 20, None, None, 15, 7])))  # [[3], [9, 20], [15, 7]]
print(level_order(build_tree([1])))                            # [[1]]
print(level_order(build_tree([])))                             # []
```

Output:

```
[[3], [9, 20], [15, 7]]
[[1]]
[]
```
