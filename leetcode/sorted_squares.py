#!/usr/bin/env python3

import sys
import unittest

# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

# O(n log n)
def sorted_squares(nums):
    for i in range(len(nums)):
        nums[i] = pow(nums[i], 2)

    nums.sort()

    return nums

# TODO: O(n) using two pointers?
def sorted_squares2(nums):
    pass

class TestSortedSquares(unittest.TestCase):
    def test_empty(self):
        nums = []
        self.assertFalse(sorted_squares(nums))

    def test_1(self):
        nums = [-4,-1,0,3,10]
        expected = [0,1,9,16,100]
        self.assertEqual(sorted_squares(nums), expected)

    def test_2(self):
        nums = [-7,-3,2,3,11]
        expected = [4,9,9,49,121]
        self.assertEqual(sorted_squares(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
