#!/usr/bin/env python3

import sys
import unittest

#1 <= nums.length <= 1000
#-10^6 <= nums[i] <= 10^6
def running_sum(nums):
    if not nums:
        return []

    run_sum = [nums[0]]

    for i in range(1, len(nums)):
        run_sum.append(nums[i] + run_sum[-1])

    return run_sum

class TestRunningSum(unittest.TestCase):
    def test_empty(self):
        nums = []
        self.assertFalse(running_sum(nums))

    def test_1(self):
        nums = [1,2,3,4]
        expected = [1,3,6,10]
        self.assertEqual(running_sum(nums), expected)

    def test_2(self):
        nums = [1,1,1,1,1]
        expected = [1,2,3,4,5]
        self.assertEqual(running_sum(nums), expected)

    def test_3(self):
        nums = [3,1,2,10,1]
        expected = [3,4,6,16,17]
        self.assertEqual(running_sum(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
