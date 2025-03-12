#!/usr/bin/env python3

import sys
import unittest

# number: 148
# section: divide & conquer
# difficulty: medium
# tags: linked list, two pointers, divide & conquer, sorting, merge sort,
# top 150

# constraints
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# run-time: O(n)
def merge(list1, list2):
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

    # append remaining
    tail.next = list1 if list1 else list2

    return head.next

# run-time: O(n)
def find_mid(head):
    if not head:
        return None

    prev = None
    mid = head

    while head and head.next:
        prev = mid
        mid = mid.next
        head = head.next.next

    # disconnect *before* mid
    prev.next = None

    return mid

# solution: LeetCode fast/slow ptrs + merge sort
# complexity:
# run-time: O(n*log n)
# space: O(log n)
def sort_list(head):
    # base case: return head!
    if not head or not head.next:
        return head

    # get middle
    mid = find_mid(head)

    # split
    left = sort_list(head)
    right = sort_list(mid)

    # merge
    return merge(left, right)

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
