# Given the head of a singly linked list, reverse the list and return the new head.
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1

# Approach: walk the list once, pointing each node's next back at the previous node.
# Save the next node first so the rest of the list is not lost.
# Time: O(n)  Space: O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    print(to_list(reverse_list(build_list([1, 2, 3, 4, 5]))))  # [5, 4, 3, 2, 1]
    print(to_list(reverse_list(build_list([1, 2]))))           # [2, 1]
    print(to_list(reverse_list(build_list([]))))               # []
