# Lowest Common Ancestor of a BST

Given a binary search tree and two nodes p and q in it, return their lowest common ancestor: the deepest node that has both p and q as descendants (a node counts as a descendant of itself).

```
Input: root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 8
Output: 6
Input: root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 4
Output: 2
```

## Explanation

Use the BST ordering. If both values are smaller than the current node, the answer is on the left; if both are larger, it is on the right. Otherwise they split here (or one of them is this node), so this node is the answer.

## Complexity

- **Time:** O(h)
- **Space:** O(1)

## Output

Running `python LowestCommonAncestorOfBST.py` executes these examples:

```python
root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
print(lowest_common_ancestor(root, find(root, 2), find(root, 8)).val)  # 6
print(lowest_common_ancestor(root, find(root, 2), find(root, 4)).val)  # 2
print(lowest_common_ancestor(root, find(root, 3), find(root, 5)).val)  # 4
```

Output:

```
6
2
4
```
