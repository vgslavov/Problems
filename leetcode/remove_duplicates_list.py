#!/usr/bin/env python3

import sys
import unittest

# keep 1 value from dupes!

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
def remove_duplicates(head):
    slow = fast = head

    while fast and fast.next:
        while fast.next and slow.val == fast.next.val:
            slow.next = fast.next.next

        slow = slow.next
        fast = slow

    return head

# TODO: add unittest
# Input: head = [1,1,2]
# Output: [1,2]
 
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

if __name__ == '__main__':
    sys.exit(unittest.main())
