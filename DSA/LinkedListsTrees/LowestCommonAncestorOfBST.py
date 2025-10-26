# Given a binary search tree and two nodes p and q in it, return their lowest common
# ancestor: the deepest node that has both p and q as descendants (a node counts as a
# descendant of itself).
# Input: root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 8
# Output: 6
# Input: root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 4
# Output: 2

# Approach: use the BST ordering. If both values are smaller than the current node, the
# answer is on the left; if both are larger, it is on the right. Otherwise they split
# here (or one of them is this node), so this node is the answer.
# Time: O(h)  Space: O(1)

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
    return None


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


def find(root, val):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root


if __name__ == "__main__":
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(lowest_common_ancestor(root, find(root, 2), find(root, 8)).val)  # 6
    print(lowest_common_ancestor(root, find(root, 2), find(root, 4)).val)  # 2
    print(lowest_common_ancestor(root, find(root, 3), find(root, 5)).val)  # 4
