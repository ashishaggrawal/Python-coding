# Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth: the number of nodes on the longest path from the root down to a leaf.

```
Input: [3, 9, 20, None, None, 15, 7]   (level order)
Output: 3
```

## Explanation

**Approach 1 (DFS recursion):** depth = 1 + the deeper of the two subtrees.

**Approach 2 (BFS queue):** count how many levels are processed.

## Complexity

- **Time:** O(n)
- **Space:** O(h) for DFS, O(w) for BFS

## Output

Running `python MaximumDepthOfBinaryTree.py` executes these examples:

```python
print(max_depth(build_tree([3, 9, 20, None, None, 15, 7])))      # 3
print(max_depth_bfs(build_tree([3, 9, 20, None, None, 15, 7])))  # 3
print(max_depth(build_tree([1, None, 2])))                       # 2
```

Output:

```
3
3
2
```
