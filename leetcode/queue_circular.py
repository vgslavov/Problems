#!/usr/bin/env python3

import sys
import unittest

# number: 622
# section: citadel
# difficulty: medium
# tags: array, linked list, design, queue, citadel

# constraints
# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 3000 calls will be made to enqueue, dequeue, front, rear, isempty, and
# isfull.

# solution: 2 lists
# complexity
# run-time: O(1) per op
# space: O(k)
class MyCircularQueue:

    def __init__(self, k: int):
        self.__front = []
        self.__rear = []
        self.__capacity = k

    def enqueue(self, value: int) -> bool:
        if self.isfull():
            return False

        self.__rear.append(value)

        return True

    def dequeue(self) -> bool:
        if self.__front:
            del self.__front[0]
            return True
        elif self.__rear:
            del self.__rear[0]
            return True
        else:
            return False

    def front(self) -> int:
        # first check front!
        if self.__front:
            return self.__front[0]
        elif self.__rear:
            return self.__rear[0]
        else:
            return -1

    def rear(self) -> int:
        # first check rear!
        if self.__rear:
            return self.__rear[-1]
        elif self.__front:
            return self.__front[-1]
        else:
            return -1

    def isempty(self) -> bool:
        if self.__front or self.__rear:
            return False

        return True

    def isfull(self) -> bool:
        if len(self.__front) + len(self.__rear) == self.__capacity:
            return True

        return False

# TODO: solve using linked list

class TestMyCirciularQueue(unittest.TestCase):
    def test(self):
        k = 3
        obj = MyCircularQueue(k)
        self.assertTrue(obj.enqueue(1))
        self.assertTrue(obj.enqueue(2))
        self.assertTrue(obj.enqueue(3))
        self.assertFalse(obj.enqueue(4))
        self.assertEqual(obj.rear(), 3)
        self.assertTrue(obj.isfull())
        self.assertTrue(obj.dequeue())
        self.assertTrue(obj.enqueue(4))
        self.assertEqual(obj.rear(), 4)
        self.assertFalse(obj.isempty())
        self.assertEqual(obj.front(), 2)

if __name__ == '__main__':
    sys.exit(unittest.main())
