#!/usr/bin/env python3

import sys
import unittest

# number: 143
# title: Reorder List
# url: https://leetcode.com/problems/reorder-list/
# section: meta
# difficulty: medium
# tags: linked list, two pointers, stack, recursion

# constraints:
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# number: 876
# solution: fast/slow pointer
# complexity:
# run-time: O(n)
# space: O(1)
def find_middle_prev(head: ListNode) -> ListNode:
    prev = ListNode(0, head)
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        prev = prev.next
        fast = fast.next.next

    return prev

# number: 206
# solution: prev pointer
# complexity:
# run-time: O(n)
# space: O(1)
def reverse(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev

# number: 21
# solution: head/tail pointer
# complexity:
# run-time: O(n)
# space: O(1)
def merge(list1: ListNode, list2: ListNode) -> ListNode:
    head = ListNode()
    tail = head

    while list1 and list2:
        tail.next = list1
        list1 = list1.next
        tail = tail.next

        tail.next = list2
        list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return head.next

# solution: find middle, reverse second half, merge two halves
# complexity:
# run-time: O(n)
# space: O(1)
def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    # pointer to middle
    prev = find_middle_prev(head)

    # disconnect the first half
    middle = prev.next
    prev.next = None

    # list of 1
    if head == middle:
        return head

    merge(head, reverse(middle))

class TestReorderList(unittest.TestCase):
    def test_reorder_list(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        reorderList(head)

        # Check the order: 1 -> 4 -> 2 -> 3
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 4)
        self.assertEqual(head.next.next.val, 2)
        self.assertEqual(head.next.next.next.val, 3)
        self.assertIsNone(head.next.next.next.next)

        # Create a linked list: 1 -> 2 -> 3
        head = ListNode(1, ListNode(2, ListNode(3)))
        reorderList(head)
        # Check the order: 1 -> 3 -> 2
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 3)
        self.assertEqual(head.next.next.val, 2)

        # Create a linked list: 1 -> 2
        head = ListNode(1, ListNode(2))
        reorderList(head)
        # Check the order: 1 -> 2
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)

        # Create a linked list: 1
        head = ListNode(1)
        reorderList(head)
        # Check the order: 1
        self.assertEqual(head.val, 1)
        self.assertIsNone(head.next)

        # Create an empty linked list
        head = None
        reorderList(head)
        # Check the order: None
        self.assertIsNone(head)

if __name__ == '__main__':
    sys.exit(unittest.main())