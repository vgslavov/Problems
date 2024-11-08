#!/usr/bin/env python3

import sys
import unittest

# number: 232
# section: 
# difficulty: easy
# tags: stack, design, queue

# constraints
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.

# complexity
# run-time: see below
# space: O(n)
class MyQueue:

    def __init__(self):
        # front of queue
        self.__front = []

        # back of queue
        self.__back = []

    # run-time: O(1)
    def push(self, x: int) -> None:
        # always push to back stack
        self.__back.append(x)

    # run-time: O(1) amortized, O(n) worst-case
    def pop(self) -> int:
        if self.empty():
            raise ValueError("empty queue") 

        # if front is non-empty, pop from front
        if not self.__front and not self.__back2front():
            raise ValueError("failed moving from back to front")

        return self.__front.pop()

    # run-time: O(1) amortized, O(n) worst-case
    def peek(self) -> int:
        if self.empty():
            raise ValueError("empty queue")

        if not self.__front and not self.__back2front():
            raise ValueError("failed moving from back to front")

        return self.__front[-1]

    # run-time: O(n)
    def __back2front(self) -> bool:
        if self.empty():
            return False

        while self.__back:
            self.__front.append(self.__back[-1])
            self.__back.pop()

        return True

    # run-time: O(1)
    def empty(self) -> bool:
        return not len(self.__front) and not len(self.__back)

# TODO: worst-case O(1)?

class TestMyQueue(unittest.TestCase):
    def test(self):
        q = MyQueue()
        q.push(1)                       # [1]
        q.push(2)                       # [1,2]
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)    # [2]
        self.assertFalse(q.empty())

if __name__ == '__main__':
    sys.exit(unittest.main())
