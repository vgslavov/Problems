#!/usr/bin/env python3

import sys
import unittest

# number: 86
# section: linked list
# difficulty: medium
# tags: linked list, two pointers, top 150

# constraints
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution: LeetCode using 2 pointers
# complexity
# run-time: O(n)
# space: O(1)
def partition_list(head, x):
    before_head = before = ListNode(0)
    after_head = after = ListNode(0)

    while head:
        #print(f"head:{head}")
        #print(f"before_head:{before}")
        #print(f"after_head:{after}")

        # add to before
        if head.val < x:
            # add node
            before.next = head
            # go fwd in before
            before = before.next
            # go fwd in org
            head = head.next
            # disconnect node from org
            before.next = None
        # add to after (>= x)
        else:
            after.next = head
            after = after.next
            head = head.next
            after.next = None

    # join end of before & beginning of after
    before.next = after_head.next

    return before_head.next

# TODO: add unit tests
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Input: head = [2,1], x = 2
# Output: [1,2]

if __name__ == '__main__':
    sys.exit(unittest.main())
