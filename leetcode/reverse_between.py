#!/usr/bin/env python3

import sys
import unittest

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def traverse(head, n):
    count = 1
    curr = prev = head

    while curr and count < n:
        next_node = curr.next
        prev = curr
        curr = next_node
        count += 1

    return prev

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
def reverseBetween(head, left, right):
    pre_start = head
    pre_end = traverse(pre_start, left)

    rev_start = pre_end.next
    pre_end.next = None
    print("pre_start:{}".format(pre_start))
    print("pre_end:{}".format(pre_end))

    rev_end = traverse(rev_start, right)

    post_start = rev_end.next
    rev_end.next = None
    print("rev_start:{}".format(rev_start))
    print("rev_end:{}".format(rev_end))

    reversed = reverse(rev_start)
    print("reversed:{}".format(reversed))

    # reconnect
    pre_end.next = reversed
    rev_start.next = post_start

    return head

if __name__ == '__main__':
    sys.exit(unittest.main())
