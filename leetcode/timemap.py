#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 981
# title: Time Based Key-Value Store
# url: https://leetcode.com/problems/time-based-key-value-store/
# section: design
# difficulty: medium
# tags: hash table, string, binary search, design, grind 75

# constraints
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 10^7
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.

# solution: dict + list
# complexity
# run-time: O(1) for set, O(log n) for get
# space: O(n)
class TimeMap:

    def __init__(self):
        # key: key
        # value: vector of tuples, (timestamp, value)
        self.__cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.__cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.__cache:
            return ""

        return self._binary_search(self.__cache[key], timestamp)

    def _binary_search(self, nums: list, k: int) -> str:
        if not nums:
            return ""

        left = 0
        right = len(nums)-1
        last = -1

        while left <= right:
            mid = left + (right-left)//2

            # keep searching right to find the last timestamp <= k
            if nums[mid][0] <= k:
                last = mid
                left = mid+1
            else:
                right = mid-1

        return nums[last][1] if last != -1 else ""

class TestTimeMap(unittest.TestCase):
    def test_example1(self):
        timemap = TimeMap()
        timemap.set("foo", "bar", 1)
        result = timemap.get("foo", 1)
        self.assertEqual(result, "bar")
        result = timemap.get("foo", 3)
        self.assertEqual(result, "bar")
        timemap.set("foo", "bar2", 4)
        result = timemap.get("foo", 4)
        self.assertEqual(result, "bar2")
        result = timemap.get("foo", 5)
        self.assertEqual(result, "bar2")

    def test_example2(self):
        timemap = TimeMap()
        timemap.set("love", "high", 10)
        timemap.set("love", "low", 20)
        result = timemap.get("love", 5)
        self.assertEqual(result, "")
        result = timemap.get("love", 10)
        self.assertEqual(result, "high")
        result = timemap.get("love", 15)
        self.assertEqual(result, "high")
        result = timemap.get("love", 20)
        self.assertEqual(result, "low")
        result = timemap.get("love", 25)
        self.assertEqual(result, "low")

if __name__ == "__main__":
    sys.exit(unittest.main())