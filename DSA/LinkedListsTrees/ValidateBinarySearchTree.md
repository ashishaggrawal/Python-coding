# Validate Binary Search Tree

Given the root of a binary tree, return True if it is a valid binary search tree: every node in a left subtree is smaller than the node, and every node in a right subtree is larger.

```
Input: [2, 1, 3]
Output: True
Input: [5, 1, 4, None, None, 3, 6]
Output: False   (3 is in 5's right subtree but is smaller than 5)
```

## Explanation

Pass down the allowed (low, high) range. Going left tightens the upper bound and going right tightens the lower bound. Checking only a node against its direct children is not enough, as the second example shows.

## Complexity

- **Time:** O(n)
- **Space:** O(h)

## Output

Running `python ValidateBinarySearchTree.py` executes these examples:

```python
print(is_valid_bst(build_tree([2, 1, 3])))                   # True
print(is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])))  # False
print(is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])))  # False
```

Output:

```
True
False
False
```
