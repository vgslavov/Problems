#!/usr/bin/env python3

import sys
import unittest

# number: 82
# section: linked list
# difficulty: medium
# tags: linked list, two pointers, top 150

# constraints
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# complexity
# run-time: O(n)
# space: O(1)
# TODO: refactor, ugly
def remove_duplicates(head):
    if not head:
        return None

    prev = None
    curr = head
    dupe = False

    while curr.next:
        # dupes, keep walking
        if curr.val == curr.next.val:
            curr = curr.next
            dupe = True
            continue

        # last dupe
        if dupe:
            if prev:
                # skip all dupes
                prev.next = curr.next
                # last dupe
                curr = curr.next
            else:
                # if starting with dupes
                head = curr.next
                curr.next = None
                curr = head
            dupe = False
            continue

        # iterate
        prev = curr
        curr = curr.next

    # ending in dupes
    if prev and prev.next != curr:
        prev.next = None
    # only dupes
    elif dupe:
        return None

    return head

if __name__ == '__main__':
    sys.exit(unittest.main())
