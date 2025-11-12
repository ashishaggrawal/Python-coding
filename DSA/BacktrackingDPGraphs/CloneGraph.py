# Given a node in a connected undirected graph, return a deep copy of the graph.
# Each node has a value and a list of neighbours.
# Input: adjacency list [[2, 4], [1, 3], [2, 4], [1, 3]]   (node i+1's neighbours)
# Output: an identical graph made of new node objects

# Approach: traverse the graph (DFS) and keep a hash map from each original node to its
# copy. The map serves as the visited set and also lets cycles link to copies that
# already exist instead of recursing forever.
# Time: O(V + E)  Space: O(V)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    if node is None:
        return None
    copies = {}  # original node -> its clone

    def dfs(original):
        if original in copies:
            return copies[original]
        copy = Node(original.val)
        copies[original] = copy
        for neighbor in original.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)


def build_graph(adjacency):
    nodes = [Node(i + 1) for i in range(len(adjacency))]
    for i, neighbors in enumerate(adjacency):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0] if nodes else None


def to_adjacency(node):
    """Collect every node reachable from node and return the adjacency list by value."""
    seen, stack = {}, [node]
    while stack:
        n = stack.pop()
        if n.val in seen:
            continue
        seen[n.val] = n
        stack.extend(n.neighbors)
    return [[nb.val for nb in seen[v].neighbors] for v in sorted(seen)], list(seen.values())


if __name__ == "__main__":
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = clone_graph(original)
    adj, cloned_nodes = to_adjacency(cloned)
    _, original_nodes = to_adjacency(original)
    print(adj)  # [[2, 4], [1, 3], [2, 4], [1, 3]]
    print("no shared nodes:", not set(map(id, cloned_nodes)) & set(map(id, original_nodes)))  # True
