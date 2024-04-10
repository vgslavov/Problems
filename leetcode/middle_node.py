#!/usr/bin/env python3

import sys
import unittest

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
def middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# TODO: add unittest

if __name__ == '__main__':
    sys.exit(unittest.main())
