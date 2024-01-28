#!/usr/bin/env python3

import sys
import unittest

# list
class Queue1:
    def __init__(self):
        self._stack = []

    # O(1)
    def push_back(self, elem):
        self._stack.append(elem)

    # O(N)?
    def pop_front(self):
        return self._stack.pop(0) if not self.empty() else None

    def empty(self):
        return not len(self._stack)

    def size(self):
        return len(self._stack)

# 2 lists
class Queue2:
    def __init__(self):
        # reverse queue order
        self._stack1 = []
        # temporary
        self._stack2 = []

    # O(1)
    def push_back(self, elem):
        self._stack1.append(elem)

    # O(N)
    def pop_front(self):
        while len(self._stack1):
            self._stack2.append(self._stack1.pop())

        front = self._stack2.pop() if len(self._stack2) else None

        while len(self._stack2):
            self._stack1.append(self._stack2.pop())

        return front

    def empty(self):
        return not len(self._stack1)

    def size(self):
        return len(self._stack1)


class TestQueueStack(unittest.TestCase):

    def test_empty(self):
        q1 = Queue1()
        self.assertFalse(q1.pop_front())

        q2 = Queue2()
        self.assertFalse(q2.pop_front())

    def test_all(self):
        q1 = Queue1()
        q1.push_back(5)
        q1.push_back(15)
        q1.push_back(9)
        self.assertEqual(q1.pop_front(), 5)
        self.assertFalse(q1.empty())
        self.assertEqual(q1.size(), 2)

        q2 = Queue2()
        q2.push_back(5)
        q2.push_back(15)
        q2.push_back(9)
        self.assertEqual(q2.pop_front(), 5)
        self.assertFalse(q2.empty())
        self.assertEqual(q2.size(), 2)

if __name__ == '__main__':
    sys.exit(unittest.main())
