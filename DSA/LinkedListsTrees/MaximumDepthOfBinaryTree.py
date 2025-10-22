# Given the root of a binary tree, return its maximum depth: the number of nodes on the
# longest path from the root down to a leaf.
# Input: [3, 9, 20, None, None, 15, 7]   (level order)
# Output: 3

# Approach 1 (DFS recursion): depth = 1 + the deeper of the two subtrees.
# Approach 2 (BFS queue): count how many levels are processed.
# Time: O(n)  Space: O(h) for DFS, O(w) for BFS

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_bfs(root):
    if root is None:
        return 0
    depth = 0
    queue = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


def build_tree(values):
    """Build a tree from a level-order list where None marks a missing node."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    print(max_depth(build_tree([3, 9, 20, None, None, 15, 7])))      # 3
    print(max_depth_bfs(build_tree([3, 9, 20, None, None, 15, 7])))  # 3
    print(max_depth(build_tree([1, None, 2])))                       # 2
