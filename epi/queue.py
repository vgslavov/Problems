#!/usr/bin/env python3

import sys
import unittest

# section: interview
# difficulty: easy
# tags: optiver

# constraints
# don't use Python list/deque's append(), etc.

class MyQueue:
    def __init__(self, capacity=MAX_SIZE) -> None:
        self.__capacity = capacity
        self.__queue = [None] * capacity
        self.__size = self.__front = self.__back = 0

    def __increase_capacity(self, factor=2) -> None:
        self.__capacity *= factor
        self.__queue[:] = self.__queue[:self.__capacity] + \
                [None for _ in range(self.__capacity - len(self.__queue))]

    def push(self, value: int) -> None:
        if self.__size == self.__capacity:
            self.__increase_capacity()

        self.__queue[self.__back] = value
        self.__back += 1
        self.__size += 1

    def pop(self) -> int:
        if self.empty():
            return None

        value = self.__queue[self.__front]
        self.__queue[self.__front] = None
        self.__front += 1
        self.__size -= 1

        return value

    def front(self):
        if self.empty():
            return None

        return self.__queue[self.__front]

    def empty(self):
        return not self.__size

class TestMyQueue(unittest.TestCase):
    def test(self):
        q = MyQueue(1)                  # [None]
        self.assertTrue(q.empty())
        self.assertFalse(q.pop())
        q.push(1)                       # [1]
        q.push(2)                       # [1,2]
        q.push(3)                       # [1,2,3]
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.pop(), 1)    # [2]
        self.assertFalse(q.empty())

if __name__ == '__main__':
    sys.exit(unittest.main())
