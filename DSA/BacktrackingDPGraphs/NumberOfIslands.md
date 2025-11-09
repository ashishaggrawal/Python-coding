# Number of Islands

Given an m x n grid of "1" (land) and "0" (water), return the number of islands. An island is land connected horizontally or vertically.

```
Input: grid = [["1","1","0","0","0"],
               ["1","1","0","0","0"],
               ["0","0","1","0","0"],
               ["0","0","0","1","1"]]
Output: 3
```

## Explanation

Scan the grid. Each unvisited "1" starts a new island; flood-fill it (BFS here) to mark every connected land cell as visited so it is not counted again. BFS is used instead of recursive DFS to avoid hitting the recursion limit on large grids.

## Complexity

- **Time:** O(m * n)
- **Space:** O(min(m, n)) for the BFS queue

## Output

Running `python NumberOfIslands.py` executes these examples:

```python
print(num_islands([["1", "1", "1", "1", "0"],
                   ["1", "1", "0", "1", "0"],
                   ["1", "1", "0", "0", "0"],
                   ["0", "0", "0", "0", "0"]]))  # 1
print(num_islands([["1", "1", "0", "0", "0"],
                   ["1", "1", "0", "0", "0"],
                   ["0", "0", "1", "0", "0"],
                   ["0", "0", "0", "1", "1"]]))  # 3
```

Output:

```
1
3
```
