#!/usr/bin/env python3

import sys
import unittest

# number: 24
# section: recursion
# difficulty: medium
# tags: linked list, recursion

# constraints
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

def swap_helper(head):
    if not head or not head.next:
        return

    head.val, head.next.val = head.next.val, head.val

    swap_helper(head.next.next)

# solution: swap values
# complexity
# run-time: O(n)
# space: O(n)
def swap_pairs(head):
    if not head or not head.next:
        return head

    org_head = head
    swap_helper(head)

    return org_head

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
