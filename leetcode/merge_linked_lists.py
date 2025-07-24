#!/usr/bin/env python3

import sys
import unittest

# number: 21
# title: Merge Two Sorted Lists
# url: https://leetcode.com/problems/merge-two-sorted-lists/
# section: linked list
# difficulty: easy
# tags: link list, recursion, top 150, meta, grind 75

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# constraints
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# solution: two pointers
# complexity
# run-time: O(n+m)
# space: O(1)
def merge_linked_lists(list1, list2):
    head = ListNode()
    tail = head

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # append remaining list
    tail.next = list1 if list1 else list2

    return head.next

# TODO: unit test

if __name__ == '__main__':
    sys.exit(unittest.main())
