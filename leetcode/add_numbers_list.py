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

def list2vals(l):
    vals = []
    while l:
        vals.append(l.val)
        l = l.next
    return vals

def vals2list(vals):
    head = ListNode()
    curr = head
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return head.next

class TestAddNumbers(unittest.TestCase):
    def test_single_digits(self):
        # 2 + 3 = 5
        l1 = ListNode(2)
        l2 = ListNode(3)
        self.assertEqual(list2vals(add_numbers(l1, l2)), [5])

    def test_example1(self):
        # 342 + 465 = 807
        l1 = vals2list([2, 4, 3])
        l2 = vals2list([5, 6, 4])
        self.assertEqual(list2vals(add_numbers(l1, l2)), [7, 0, 8])

    def test_example2(self):
        # 0 + 0 = 0
        l1 = ListNode(0)
        l2 = ListNode(0)
        self.assertEqual(list2vals(add_numbers(l1, l2)), [0])

    def test_carry(self):
        # 99 + 1 = 100
        l1 = vals2list([9, 9])
        l2 = ListNode(1)
        self.assertEqual(list2vals(add_numbers(l1, l2)), [0, 0, 1])

    def test_different_lengths(self):
        # 99999 + 1 = 100000
        l1 = vals2list([9, 9, 9, 9, 9])
        l2 = ListNode(1)
        self.assertEqual(list2vals(add_numbers(l1, l2)), [0, 0, 0, 0, 0, 1])

class TestHelpers(unittest.TestCase):
    def test_list2int(self):
        # [2, 4, 3] represents 342
        l = vals2list([2, 4, 3])
        self.assertEqual(list2int(l), 342)

    def test_int2list2(self):
        self.assertEqual(list2vals(int2list2(342)), [2, 4, 3])

    def test_int2list2_zero(self):
        self.assertEqual(list2vals(int2list2(0)), [0])

    def test_reverse(self):
        l = vals2list([1, 2, 3])
        self.assertEqual(list2vals(reverse(l)), [3, 2, 1])

if __name__ == '__main__':
    sys.exit(unittest.main())
