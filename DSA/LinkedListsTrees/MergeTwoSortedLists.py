# Given the heads of two sorted linked lists, merge them into one sorted list by
# splicing their nodes together, and return its head.
# Input: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Approach: a dummy head removes the special case for the first node. Repeatedly attach
# the smaller front node, then attach whatever remains of the other list.
# Time: O(n + m)  Space: O(1) (existing nodes are reused, not copied)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next


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
    print(to_list(merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))))  # [1, 1, 2, 3, 4, 4]
    print(to_list(merge_two_lists(build_list([]), build_list([0]))))              # [0]
