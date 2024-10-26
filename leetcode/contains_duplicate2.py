#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 219
# section: hashmap
# difficulty: easy
# tags: array, hash table, sliding window, top 150

# description
# return true if there are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k

# constraints
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5

# solution: brute-force
# complexity
# run-time: O(n^2), slow!
# space: O(k)
def contains_nearby_duplicate(nums, k):
    d = defaultdict(list)

    for i in range(len(nums)):
        d[nums[i]].append(i)

    for key,val in d.items():
        for i in range(1, len(val)):
            if abs(val[i] - val[i-1]) <= k:
                return True

    return False

# TODO: solve using sliding window

class TestContainsDupes(unittest.TestCase):
    def test_empty(self):
        nums = []
        k = 0
        self.assertFalse(contains_nearby_duplicate(nums, k))

    def test_true(self):
        nums = [1,2,3,1]
        k = 3
        self.assertTrue(contains_nearby_duplicate(nums, k))

    def test_true2(self):
        nums = [1,0,1,1]
        k = 1
        self.assertTrue(contains_nearby_duplicate(nums, k))

    def test_false(self):
        nums = [1,2,3,1,2,3]
        k = 2
        self.assertFalse(contains_nearby_duplicate(nums, k))

if __name__ == '__main__':
    sys.exit(unittest.main())
