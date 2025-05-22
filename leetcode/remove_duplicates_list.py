#!/usr/bin/env python3

import sys
import unittest

# number: 83
# title: Remove Duplicates from Sorted List
# url: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# section: linked list
# difficulty: easy
# tags: linked list

# constraints
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
# keep 1 value from dupes!

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution: fast & slow pointers
# complexity
# run-time: O(n)
# space: O(1)
def remove_duplicates(head):
    slow = fast = head

    while slow and slow.next:
        # skip duplicates
        while slow.next and fast.val == slow.next.val:
            fast.next = slow.next.next
            
        # catch up fast & slow
        fast = fast.next
        slow = fast

    return head

# TODO: add unittest
# Input: head = [1,1,2]
# Output: [1,2]
 
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

if __name__ == '__main__':
    sys.exit(unittest.main())
