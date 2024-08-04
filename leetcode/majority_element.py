#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 169
# section: array/string
# difficulty: easy
# tags: array, hash table, divide & conquer, sorting, counting, top 150

# constraints
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# solution: dictionary
# complexity
# run-time: O(n)
# space: O(n)
def majority_element(nums):
    if not nums:
        return False

    counts = defaultdict(int)

    for v in nums:
        counts[v] += 1

    return max(zip(counts.values(), counts.keys()))[1]

# TODO: O(n) time & O(1) space using bitmap/int?

class TestMajorityElement(unittest.TestCase):

    def test_empty(self):
        nums = []
        self.assertFalse(majority_element(nums))

    def test_majority1(self):
        nums = [3,2,3]
        self.assertEqual(majority_element(nums), 3)

    def test_majority2(self):
        nums = [2,2,1,1,1,2,2]
        self.assertEqual(majority_element(nums), 2)

if __name__ == '__main__':
    sys.exit(unittest.main())
