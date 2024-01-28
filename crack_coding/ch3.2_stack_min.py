#!/usr/bin/env python3

import heapq
import sys
import unittest

# list of tuples
# time: O(1)
# space: O(N) x 2+
class StackMin1:
    def __init__(self):
        self._stack = []

    # O(1)
    def push(self, item):
        min_int = min(item, self._stack[-1][1]) if len(self._stack) else item
        self._stack.append((item, min_int))

    # O(1)
    def pop(self):
        return self._stack.pop()[0] if len(self._stack) else None

    # O(1)
    def min(self):
        return self._stack[-1][1] if len(self._stack) else None

    def empty(self):
        return not len(self._stack)

    def size(self):
        return len(self._stack)

# min count
# time: O(1)
# space: O(N) x 2
class StackMin2:
    def __init__(self):
        self._stack = []
        # order of mins & their count
        self._min2count = []

    # O(1)
    def push(self, item):
        # empty min stack or smaller new int
        if not self._min2count or \
           (self._min2count and item < self._min2count[-1][0]):
            self._min2count.append((item, 1))
        # existing min
        elif self._min2count and item == self._min2count[-1][0]:
            self._min2count[-1] = (self._min2count[-1][0],\
                                   self._min2count[-1][1] + 1)

        self._stack.append(item)

    # O(1)
    def pop(self):
        if self._stack[-1] == self._min2count[-1]:
            self._min2count[-1] = (self._min2count[-1][0], \
                                   self._min2count[-1][1] - 1)
            if not self._min2count[-1][1]:
                self._min2count.pop()

        return self._stack.pop() if len(self._stack) else None

    # O(1)
    def min(self):
        return self._min2count[-1][0] if len(self._min2count) else None

    def empty(self):
        return not len(self._stack)

    def size(self):
        return len(self._stack)

class TestStackMin(unittest.TestCase):

    def test_empty(self):
        s1 = StackMin1()
        s2 = StackMin2()
        self.assertTrue(s1.empty())
        self.assertTrue(s2.empty())
        self.assertFalse(s1.min())
        self.assertFalse(s2.min())

    def test_min(self):
        s1 = StackMin1()
        s1.push(5)
        s1.push(1)
        s1.push(10)
        s1.push(100)
        s1.push(19)
        s1.push(113)
        self.assertEqual(s1.size(), 6)
        self.assertEqual(s1.min(), 1)

        s2 = StackMin2()
        s2.push(5)
        s2.push(1)
        s2.push(10)
        s2.push(100)
        s2.push(19)
        s2.push(113)
        self.assertEqual(s2.size(), 6)
        self.assertEqual(s2.min(), 1)

    def test_min_dupe(self):
        s1 = StackMin1()
        s1.push(5)
        self.assertEqual(s1.min(), 5)
        s1.push(1)
        self.assertEqual(s1.min(), 1)
        s1.push(10)
        self.assertEqual(s1.min(), 1)
        s1.push(1)
        self.assertEqual(s1.min(), 1)
        s1.pop()
        self.assertEqual(s1.min(), 1)
        s1.push(19)
        self.assertEqual(s1.min(), 1)
        s1.push(113)
        self.assertEqual(s1.min(), 1)

        s2 = StackMin2()
        s2.push(5)
        self.assertEqual(s2.min(), 5)
        s2.push(1)
        self.assertEqual(s2.min(), 1)
        s2.push(10)
        self.assertEqual(s2.min(), 1)
        s2.push(1)
        self.assertEqual(s2.min(), 1)
        s2.pop()
        self.assertEqual(s2.min(), 1)
        s2.push(19)
        self.assertEqual(s2.min(), 1)
        s2.push(113)
        self.assertEqual(s2.min(), 1)
        s2.pop()
        s2.pop()

if __name__ == '__main__':
    sys.exit(unittest.main())
