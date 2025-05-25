#!/usr/bin/env python3

import sys
import unittest

# number: 2
# title: Add Two Numbers
# url: https://leetcode.com/problems/add-two-numbers/
# section: linked list
# difficulty: medium
# tags: linked list, math, recursion, top 150, meta

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

# solution: requires reverse
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

# solution: doesn't require reverse
# complexity
# run-time: O(n)
# space: O(1)
def int2list2(n):
    l = head = ListNode()

    if n == 0:
        return ListNode(0)

    while n:
        l.next = ListNode(n % 10)
        n //= 10
        l = l.next

    return head.next

# solution: list 2 int 2 list + reverse
# complexity
# run-time: O(n)
# space: O(1)
def add_numbers(l1, l2):
    #return reverse(int2list(list2int(l1) + list2int(l2)))
    # no need to reverse!
    return int2list2(list2int(l1) + list2int(l2))

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
