#!/usr/bin/env python3

import sys
import unittest

# number: 303
# title: Range Sum Query - Immutable
# url: https://leetcode.com/problems/range-sum-query-immutable/
# section: assessments
# difficulty: easy
# tags: array, design, prefix sum, meta

# constraints
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= left <= right < nums.length
# At most 10^4 calls will be made to sum_range.

# solution: prefix sum
# complexity
# run-time: O(n)
# space: O(n)
class NumArray:
    def __init__(self, nums):
        self.__nums = nums
        self.__prefix_sums = []
        self.calc_prefix_sum(nums)

    def sum_range(self, left: int, right: int) -> int:
        return self.__prefix_sums[right]-self.__prefix_sums[left]+self.__nums[left]

    def calc_prefix_sum(self, nums):
        if not nums:
            return

        self.__prefix_sums.append(nums[0])

        for i in range(1, len(nums)):
            self.__prefix_sums.append(self.__prefix_sums[-1] + nums[i])

class TestRangeSum(unittest.TestCase):
    def test1(self):
        num_array = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(num_array.sum_range(0, 2), 1)
        self.assertEqual(num_array.sum_range(2, 5), -1)
        self.assertEqual(num_array.sum_range(0, 5), -3)

if __name__ == '__main__':
    sys.exit(unittest.main())
