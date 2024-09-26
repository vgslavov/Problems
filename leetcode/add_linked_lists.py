#!/usr/bin/env python3

import sys
import unittest

# number: 2
# section: linked list
# difficulty: medium
# tags: linked list, math, recursion, top 150

# constraints
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# complexity
# run-time: O(n)
# space: O(1)
def reverse(l):
    prev = None

    while l:
        curr = l
        l = l.next
        curr.next = prev
        prev = curr

    return prev

# complexity
# run-time: O(n)
# space: O(1)
def list2int(l):
    ans = 0
    digit = 1
    while l:
        ans += l.val * digit
        digit *= 10
        l = l.next

    return ans

# complexity
# run-time: O(n)
# space: O(1)
def int2list(n):
    prev = None
    l = ListNode()

    while n:
        l = ListNode()
        l.val = n % 10
        l.next = prev
        prev = l
        n //= 10

    return l

# solution: list 2 int 2 list + reverse
# complexity
# run-time: O(n)
# space: O(1)
def add_linked_lists(l1, l2):
    return reverse(int2list(list2int(l1) + list2int(l2)))

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
