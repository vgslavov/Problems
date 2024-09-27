#!/usr/bin/env python3

import sys
import unittest

# number: 19
# section: linked list
# difficulty: medium
# tags: linked list, two pointers, top 150

# constraints
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# solution: dummy node + fast & slow pointers
# complexity
# run-time: O(n)
# space: O(1)
def remove_nth(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # fast ptr n ahead of slow
    while fast.next and n:
        fast = fast.next
        n -= 1

    while fast.next:
        slow = slow.next
        fast = fast.next

    # skip nth node
    slow.next = slow.next.next

    return dummy.next

# TODO: add unit tests
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Input: head = [1], n = 1
# Output: []

# Input: head = [1,2], n = 1
# Output: [1]

# Input: head = [1,2], n = 2
# Output: [2]

if __name__ == '__main__':
    sys.exit(unittest.main())
