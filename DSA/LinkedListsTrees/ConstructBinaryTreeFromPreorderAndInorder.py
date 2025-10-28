# Given the preorder and inorder traversals of a binary tree with unique values,
# rebuild the tree and return its root.
# Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
# Output: [3, 9, 20, None, None, 15, 7]   (level order)

# Approach: the next preorder value is always the root of the current subtree. Its
# position in inorder splits that range into the left and right subtrees. A hash map of
# value -> inorder index makes that lookup O(1), and passing index bounds instead of
# slicing avoids copying subarrays.
# Time: O(n)  Space: O(n)

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    index_of = {val: i for i, val in enumerate(inorder)}
    pre_iter = iter(preorder)

    def build(lo, hi):
        if lo > hi:
            return None
        root_val = next(pre_iter)
        root = TreeNode(root_val)
        mid = index_of[root_val]
        root.left = build(lo, mid - 1)   # left subtree must be built first (preorder order)
        root.right = build(mid + 1, hi)
        return root

    return build(0, len(inorder) - 1)


def to_level_order(root):
    """Level-order list with None for missing children, trailing Nones removed."""
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    print(to_level_order(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))  # [3, 9, 20, None, None, 15, 7]
    print(to_level_order(build_tree([-1], [-1])))                            # [-1]
