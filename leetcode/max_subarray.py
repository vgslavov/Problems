#!/usr/bin/env python3

import math
import sys
import unittest

# number: 53
# title: Maximum Subarray
# url: https://leetcode.com/problems/maximum-subarray/
# section: Kadane's algo
# difficulty: medium
# tags: array, divide & conquer, dp, grind 75

# constraints
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# complexity
# run-time: O(n)
# space: O(1)
# TODO: understand better
def max_subarray(nums) -> int:
    if not nums:
        return 0

    max_sum = -math.inf
    curr_sum = 0

    for n in nums:
        # discard sum so far: curr_sum+n
        # if smaller than current number: n
        curr_sum = max(n, curr_sum+n)

        # compare max sum to current sum
        max_sum = max(max_sum, curr_sum)

    return max_sum

class TestMaxSubarray(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = 0
        self.assertEqual(max_subarray(nums), expected)

    def test1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected = 6
        self.assertEqual(max_subarray(nums), expected)

    def test2(self):
        nums = [1]
        expected = 1
        self.assertEqual(max_subarray(nums), expected)

    def test3(self):
        nums = [5,4,-1,7,8]
        expected = 23
        self.assertEqual(max_subarray(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
