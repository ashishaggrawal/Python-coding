# Construct Binary Tree from Preorder and Inorder Traversal

Given the preorder and inorder traversals of a binary tree with unique values, rebuild the tree and return its root.

```
Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, None, None, 15, 7]   (level order)
```

## Explanation

The next preorder value is always the root of the current subtree. Its position in inorder splits that range into the left and right subtrees. A hash map of value -> inorder index makes that lookup O(1), and passing index bounds instead of slicing avoids copying subarrays.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Output

Running `python ConstructBinaryTreeFromPreorderAndInorder.py` executes these examples:

```python
print(to_level_order(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))  # [3, 9, 20, None, None, 15, 7]
print(to_level_order(build_tree([-1], [-1])))                            # [-1]
```

Output:

```
[3, 9, 20, None, None, 15, 7]
[-1]
```
