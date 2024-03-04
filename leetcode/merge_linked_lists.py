#!/usr/bin/env python3

import sys
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
def merge_linked_lists(list1, list2):
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1

    head = None
    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    merged = head

    while list1 and list2:
        if list1.val < list2.val:
            merged.next = list1
            list1 = list1.next
        else:
            merged.next = list2
            list2 = list2.next
        merged = merged.next

    while list1:
        merged.next = list1
        list1 = list1.next
        merged = merged.next

    while list2:
        merged.next = list2
        list2 = list2.next
        merged = merged.next

    return head

# TODO: unit test

if __name__ == '__main__':
    sys.exit(unittest.main())
