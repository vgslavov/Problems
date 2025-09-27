#!/usr/bin/env python3

import argparse
import sys
import unittest


# tags: hash table

# solution: Python dict
# complexity:
# run-time: O(1) for both put/get
# space: O(capacity)
class LRUCache:
    def __init__(self, capacity):
        self.__cache = dict()
        if capacity <= 0:
            raise ValueError("Invalid capacity")
        self.__capacity = capacity

    def put(self, key, val):
        # overwriting existing key doesn't change capacity
        if key in self.__cache:
            del self.__cache[key]
            self.__cache[key] = val
            return None

        # delete oldest
        if len(self.__cache) == self.__capacity:
            del self.__cache[next(iter(self.__cache))]

        self.__cache[key] = val

        return None

    def get(self, key):
        if key not in self.__cache:
            return -1

        # re-adding inserts it at bottom of dict
        val = self.__cache[key]
        del self.__cache[key]
        self.__cache[key] = val

        return val
        
def execute(operations: list[list[str]]) -> list[int]:
    cache = None
    ans = []

    try:
        for op in operations:
            if op[0] == 'LRUCache':
                cache = LRUCache(int(op[1]))
            elif op[0] == 'get':
                ans.append(cache.get(int(op[1])))
            elif op[0] == 'put':
                cache.put(int(op[1]), int(op[2]))
            else:
                print(f"unsupported op: {op}")
    except Exception as e:
        print(f"{e}")

    return ans

class TestLRUCache(unittest.TestCase):
    
    def test_0_capacity(self):
        capacity = 0
        self.assertRaises(ValueError, LRUCache, capacity)

    def test_neg_capacity(self):
        capacity = -5
        self.assertRaises(ValueError, LRUCache, capacity)

    def test_lrucache(self):
        capacity = 2
        obj = LRUCache(capacity)
        obj.put(1, 1)
        obj.put(2, 2)
        self.assertEqual(obj.get(1), 1)       # returns 1
        obj.put(3, 3)                         # evicts key 2
        self.assertEqual(obj.get(2), -1)      # returns -1 (not found)
        obj.put(4, 4)                         # evicts key 1
        self.assertEqual(obj.get(1), -1)      # returns -1 (not found)
        self.assertEqual(obj.get(3), 3)       # returns 3
        self.assertEqual(obj.get(4), 4)       # returns 4

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    operations = [input().split() for _ in range(int(input()))]
    res = execute(operations)
    print(" ".join(map(str, res)))