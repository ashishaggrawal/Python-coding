# Clone Graph

Given a node in a connected undirected graph, return a deep copy of the graph. Each node has a value and a list of neighbours.

```
Input: adjacency list [[2, 4], [1, 3], [2, 4], [1, 3]]   (node i+1's neighbours)
Output: an identical graph made of new node objects
```

## Explanation

Traverse the graph (DFS) and keep a hash map from each original node to its copy. The map serves as the visited set and also lets cycles link to copies that already exist instead of recursing forever.

## Complexity

- **Time:** O(V + E)
- **Space:** O(V)

## Output

Running `python CloneGraph.py` executes these examples:

```python
original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
cloned = clone_graph(original)
adj, cloned_nodes = to_adjacency(cloned)
_, original_nodes = to_adjacency(original)
print(adj)  # [[2, 4], [1, 3], [2, 4], [1, 3]]
print("no shared nodes:", not set(map(id, cloned_nodes)) & set(map(id, original_nodes)))  # True
```

Output:

```
[[2, 4], [1, 3], [2, 4], [1, 3]]
no shared nodes: True
```
