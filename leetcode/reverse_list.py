#!/usr/bin/env python3

import sys
import unittest

# number: 206
# section: recursion
# difficulty: easy
# tags: linked list, recursion

# constraints
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_helper(head, prev):
    if not head.next:
        head.next = prev
        return head

    next_node = head.next
    head.next = prev
    prev = head
    head = next_node

    return reverse_helper(head, prev)

# solution: recursive
# complexity
# run-time: O(n)
# space: O(n)
def reverse_list(head):
    if not head or not head.next:
        return head

    return reverse_helper(head, None)

# solution: iterative
# complexity
# run-time: O(n)
# space: O(1)
def reverse_list(head):
    if not head or not head.next:
        return head

    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
