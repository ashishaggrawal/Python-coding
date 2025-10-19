# Given the root of a binary tree, invert it (mirror it left to right) and return its root.
# Input: [4, 2, 7, 1, 3, 6, 9]   (level order)
# Output: [4, 7, 2, 9, 6, 3, 1]

# Approach 1 (recursive): swap the children of each node, then invert both subtrees.
# Approach 2 (iterative): visit nodes with a queue and swap each node's children.
# Time: O(n)  Space: O(h) recursive (h = tree height), O(w) iterative (w = max width)

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def invert_tree_iterative(root):
    queue = deque([root] if root else [])
    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root


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


def to_level_order(root):
    result, queue = [], deque([root] if root else [])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == "__main__":
    print(to_level_order(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))))            # [4, 7, 2, 9, 6, 3, 1]
    print(to_level_order(invert_tree_iterative(build_tree([4, 2, 7, 1, 3, 6, 9]))))  # [4, 7, 2, 9, 6, 3, 1]
    print(to_level_order(invert_tree(build_tree([2, 1, 3]))))                        # [2, 3, 1]
