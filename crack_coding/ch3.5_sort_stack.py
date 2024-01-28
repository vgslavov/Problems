#!/usr/bin/env python3

import sys
import unittest

# list
class SortedStack():
    def __init__(self):
        # min on top
        self._stack = []

    # O(N)
    def push(self, elem):
        tmp = []
        while not self.empty() and elem > self.peek():
            tmp.append(self._stack.pop())

        self._stack.append(elem)

        while len(tmp):
            self._stack.append(tmp.pop())

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1] if not self.empty() else None

    def empty(self):
        return not len(self._stack)

    def size(self):
        return len(self._stack)

class TestSortedStack(unittest.TestCase):

    def test_empty(self):
        s = SortedStack()
        self.assertTrue(s.empty())

    def test_all(self):
        s = SortedStack()
        s.push(5)
        self.assertEqual(s.peek(), 5)
        s.push(15)
        self.assertEqual(s.peek(), 5)
        s.push(3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.size(), 3)

if __name__== '__main__':
    sys.exit(unittest.main())
