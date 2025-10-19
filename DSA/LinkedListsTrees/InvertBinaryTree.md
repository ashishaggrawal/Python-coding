# Invert Binary Tree

Given the root of a binary tree, invert it (mirror it left to right) and return its root.

```
Input: [4, 2, 7, 1, 3, 6, 9]   (level order)
Output: [4, 7, 2, 9, 6, 3, 1]
```

## Explanation

**Approach 1 (recursive):** swap the children of each node, then invert both subtrees.

**Approach 2 (iterative):** visit nodes with a queue and swap each node's children.

## Complexity

- **Time:** O(n)
- **Space:** O(h) recursive (h = tree height), O(w) iterative (w = max width)

## Output

Running `python InvertBinaryTree.py` executes these examples:

```python
print(to_level_order(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))))            # [4, 7, 2, 9, 6, 3, 1]
print(to_level_order(invert_tree_iterative(build_tree([4, 2, 7, 1, 3, 6, 9]))))  # [4, 7, 2, 9, 6, 3, 1]
print(to_level_order(invert_tree(build_tree([2, 1, 3]))))                        # [2, 3, 1]
```

Output:

```
[4, 7, 2, 9, 6, 3, 1]
[4, 7, 2, 9, 6, 3, 1]
[2, 3, 1]
```
