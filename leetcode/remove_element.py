#!/usr/bin/env python3

import sys
import unittest

# remove in-place
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100
def remove_element(nums, val):
    matches = 0

    for i, v in enumerate(nums):
        if v == val:
            nums[i] = 999
            matches += 1

    nums.sort()

    return len(nums) - matches, nums

class TestRemoveElement(unittest.TestCase):

    def test_empty(self):
        nums = []
        val = 5
        k = len(nums)
        self.assertEqual(remove_element(nums, val), (k, nums))

    def test_nomatch(self):
        nums = [1,2,3,4]
        val = 5
        k = len(nums)
        self.assertEqual(remove_element(nums, val), (k, nums))

    def test_match1(self):
        nums = [3,2,2,3]
        val = 3
        expected = [2,2]
        k = len(expected)
        self.assertEqual(remove_element(nums, val)[1][:k], expected)

    def test_match2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        expected = [0,0,1,3,4]
        k = len(expected)
        self.assertEqual(remove_element(nums, val)[1][:k], expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
