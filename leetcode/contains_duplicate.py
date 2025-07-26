#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 217
# title: Contains Duplicate
# url: https://leetcode.com/problems/contains-duplicate/
# difficulty: easy
# tags: array, hash table, sliding window, grind 75

# constraints
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5

# solution: defaultdict
# complexity
# run-time: O(n)
# space: O(n)
def contains_duplicate(nums: list[int]) -> bool:
    d = defaultdict(int)

    for n in nums:
        d[n] += 1

    # max value
    #return max(d.values(), default=0) > 1 if d else False
    # key with max value
    return d[max(d, key=d.get)] > 1 if d else False

class TestContainsDuplicate(unittest.TestCase):
    def test_empty(self):
        nums = []
        self.assertFalse(contains_duplicate(nums))

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        self.assertFalse(contains_duplicate(nums))

    def test_with_duplicates(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(contains_duplicate(nums))

    def test_large_input(self):
        nums = list(range(100000)) + [99999]
        self.assertTrue(contains_duplicate(nums))

if __name__ == '__main__':
    sys.exit(unittest.main())