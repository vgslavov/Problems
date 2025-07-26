#!/usr/bin/env python3

import sys
import unittest

# number: 876
# title: Middle of the Linked List
# url: https://leetcode.com/problems/middle-of-the-linked-list/
# section:
# difficulty: easy
# tags: linked list, two pointers, grind 75

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# solution: fast/slow pointer
# complexity:
# run-time: O(n)
# space: O(1)
def middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# TODO: add unittest

if __name__ == '__main__':
    sys.exit(unittest.main())
