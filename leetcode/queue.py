#!/usr/bin/env python3

import sys
import unittest

# constraints
# don't use Python list/deque's append(), etc.

class MyQueue:
    def __init__(self, capacity=100):
        self.__capacity = capacity
        self.__queue = [None] * capacity
        self.__front = -1
        self.__back = -1

    def __increase_capacity(self, factor=2):
        print(f"before increase_capacity, q:{self.__queue}")
        self.__capacity *= factor
        self.__queue[:] = self.__queue[:self.__capacity] + \
                [None for _ in range(self.__capacity - len(self.__queue))]

        print(f"after increase_capacity, q:{self.__queue}")

    def push(self, value):
        print(f"before push, q:{self.__queue}")
        if (self.__back - self.__front + 1) == self.__capacity:
            self.__increase_capacity()

        self.__back += 1
        self.__queue[self.__back] = value
        if self.__front < 0:
            self.__front = 0
        print(f"after push, q:{self.__queue}")

    def pop(self):
        print(f"before pop, q:{self.__queue}")
        if self.empty():
            return None

        value = self.__queue[self.__front]
        self.__queue[self.__front] = None
        self.__front += 1
        print(f"after pop, q:{self.__queue}")

        return value

    def peek(self):
        if self.empty():
            return None

        return self.__queue[self.__front]

    def empty(self):
        print(f"empty, front:{self.__front},back:{self.__back}")
        if self.__front != self.__back:
            return False

        # brand new
        if self.__front == -1:
            return True
        # point to None
        elif not self.__queue[self.__front]:
            return True

        return False

class TestMyQueue(unittest.TestCase):
    def test(self):
        q = MyQueue(1)                  # [None]
        self.assertTrue(q.empty())
        self.assertFalse(q.pop())
        q.push(1)                       # [1]
        q.push(2)                       # [1,2]
        q.push(3)                       # [1,2,3]
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)    # [2]
        self.assertFalse(q.empty())

if __name__ == '__main__':
    sys.exit(unittest.main())
