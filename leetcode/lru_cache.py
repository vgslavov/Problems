#!/usr/bin/env python3

from collections import OrderedDict
import sys
import unittest

# number: 146
# section: linked list
# difficulty: medium
# tags: hash table, linked list, design, doubly-linked list, top 150

# constraints
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.

class LRUCache:

    def __init__(self, capacity: int):
        self.__cache = OrderedDict()

        if not capacity:
            raise ValueError("Invalid capacity")

        self.__capacity = capacity

    def get(self, key: int) -> int:
        #print(f"get cache:{self.__cache} for key:{key}")

        if key not in self.__cache:
            return -1

        # mark as recent by moving to end of queue
        self.__cache.move_to_end(key)

        return self.__cache[key]

    def put(self, key: int, value: int) -> None:
        #print(f"put cache:{self.__cache} for key:{key}")

        # existing key
        if key in self.__cache:
            self.__cache[key] = value
            # end of queue: like deque.append()
            self.__cache.move_to_end(key)
            return

        # at capacity, free up
        if len(self.__cache) == self.__capacity:
            # from beginning of queue: like deque.popleft()
            self.__cache.popitem(last=False)

        # new key
        self.__cache[key] = value

class TestLRUCache(unittest.TestCase):

    def test_empty(self):
        self.assertRaises(ValueError, LRUCache, 0)

    def test_lrucache(self):
        capacity = 2
        obj = LRUCache(capacity)
        obj.put(1, 1); # cache is {1=1}
        obj.put(2, 2); # cache is {1=1, 2=2}
        self.assertEqual(obj.get(1), 1)
        obj.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(obj.get(2), -1)
        obj.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(obj.get(1), -1)
        self.assertEqual(obj.get(3), 3)
        self.assertEqual(obj.get(4), 4)

if __name__ == '__main__':
    sys.exit(unittest.main())
