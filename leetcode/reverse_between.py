#!/usr/bin/env python3

import sys
import unittest

# number: 92
# section: linked list
# difficulty: medium
# tags: linked list, top 150

# constraints
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# complexity
# run-time: O(n)
# space: O(1)
def reverse(head):
    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# complexity
# run-time: O(n)
# space: O(1)
def traverse(head, n):
    curr = head
    prev = None

    while curr and n:
        prev = curr
        curr = curr.next
        n -= 1

    return prev

# solution: traverse x2 + reverse
# complexity
# run-time: O(n)
# space: O(1)
# TODO: refactor
def reverse_between(head, left, right):
    if left == right and left == 1:
        return head

    pre_start = rev_start = new_head = head

    # range doesn't start with 1st node
    if left > 1:
        # don't include left: it's a part of reversed range!
        pre_end = traverse(pre_start, left-1)

        # disconnect pre from rev ranges
        rev_start = pre_end.next
        pre_end.next = None

        #print(f"pre_start:{pre_start},pre_end:{pre_end}")

    rev_end = traverse(rev_start, right-left+1)

    # disconnect: before reversal
    post_start = rev_end.next
    rev_end.next = None

    #print(f"pre-reverse: rev_start:{rev_start},rev_end:{rev_end},head:{head}")

    reversed = reverse(rev_start)
    #print(f"reversed:{reversed}")

    #print(f"post-reverse: rev_start:{rev_start},rev_end:{rev_end},head:{head}")
    #print(f"post_start:{post_start}")

    # reconnect: after reversal
    if left > 1:
        pre_end.next = reversed
    elif not post_start:
        return reversed
    else:
        new_head = rev_end

    # start is end after reversing
    rev_start.next = post_start

    return new_head

# TODO: add unit tests
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Input: head = [5], left = 1, right = 1
# Output: [5]

# Input: head = [3,5], left = 1, right = 2
# Output: [5,3]

# Input: head = [1,2,3], left = 1, right = 2
# Output: [2,1,3]

if __name__ == '__main__':
    sys.exit(unittest.main())
