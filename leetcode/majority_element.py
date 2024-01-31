#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
def majority_element1(nums):
    if not nums:
        return False

    counts = defaultdict(int)

    for v in nums:
        counts[v] += 1

    return max(zip(counts.values(), counts.keys()))[1]

# TODO: extra: O(n) time & O(1) space
# store in bitmap/int?
def majority_element2(nums):
    pass

class TestMajorityElement(unittest.TestCase):

    def test_empty(self):
        nums = []
        self.assertFalse(majority_element1(nums))

    def test_majority1(self):
        nums = [3,2,3]
        self.assertEqual(majority_element1(nums), 3)

    def test_majority2(self):
        nums = [2,2,1,1,1,2,2]
        self.assertEqual(majority_element1(nums), 2)

if __name__ == '__main__':
    sys.exit(unittest.main())
