# Given the head of a linked list, return True if the list contains a cycle.
# Input: 3 -> 2 -> 0 -> -4, where -4 points back to 2
# Output: True
# Input: 1 -> 2
# Output: False

# Approach: Floyd's Tortoise and Hare. A slow pointer moves 1 step and a fast pointer
# moves 2. If there is a cycle the fast pointer laps the slow one and they meet;
# otherwise the fast pointer reaches the end.
# Time: O(n)  Space: O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def build_list_with_cycle(values, pos):
    """Build a list and link the tail back to index pos (-1 means no cycle)."""
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if pos >= 0 and nodes:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    print(has_cycle(build_list_with_cycle([3, 2, 0, -4], 1)))  # True
    print(has_cycle(build_list_with_cycle([1, 2], 0)))         # True
    print(has_cycle(build_list_with_cycle([1, 2], -1)))        # False
