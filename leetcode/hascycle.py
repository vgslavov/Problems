#!/usr/bin/env python3

import sys
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
# O(1) memory
def hascycle(head):
    fast = slow = head

    while fast and fast.next:
        # True for identical Node values
        # head: [1, 1, 1, 1], pos = -1
        #if slow.val == fast.next.val:
        if slow == fast.next:
            return True

        slow = slow.next
        fast = fast.next.next

    return False

# TODO: unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
