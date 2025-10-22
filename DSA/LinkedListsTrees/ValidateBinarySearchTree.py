# Given the root of a binary tree, return True if it is a valid binary search tree:
# every node in a left subtree is smaller than the node, and every node in a right
# subtree is larger.
# Input: [2, 1, 3]
# Output: True
# Input: [5, 1, 4, None, None, 3, 6]
# Output: False   (3 is in 5's right subtree but is smaller than 5)

# Approach: pass down the allowed (low, high) range. Going left tightens the upper bound
# and going right tightens the lower bound. Checking only a node against its direct
# children is not enough, as the second example shows.
# Time: O(n)  Space: O(h)

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root, low=float("-inf"), high=float("inf")):
    if root is None:
        return True
    if not (low < root.val < high):
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)


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
    print(is_valid_bst(build_tree([2, 1, 3])))                   # True
    print(is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])))  # False
    print(is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])))  # False
