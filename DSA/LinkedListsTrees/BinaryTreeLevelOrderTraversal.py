# Given the root of a binary tree, return the values of its nodes level by level,
# from left to right.
# Input: [3, 9, 20, None, None, 15, 7]
# Output: [[3], [9, 20], [15, 7]]

# Approach: BFS with collections.deque. At the start of each level, the queue holds
# exactly that level's nodes, so process len(queue) nodes and collect their values.
# Time: O(n)  Space: O(w) (w = maximum width of the tree)

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


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
    print(level_order(build_tree([3, 9, 20, None, None, 15, 7])))  # [[3], [9, 20], [15, 7]]
    print(level_order(build_tree([1])))                            # [[1]]
    print(level_order(build_tree([])))                             # []
