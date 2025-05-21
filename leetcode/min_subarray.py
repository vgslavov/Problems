#!/usr/bin/env python3

import math
import sys
import unittest

# number: 209
# title: Minimum Size Subarray Sum
# url: https://leetcode.com/problems/minimum-size-subarray-sum/
# section: sliding window
# difficulty: medium
# tags: array, binary search, sliding window, prefix sum, top 150

# constraints
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4

# solution: sliding window
# complexity
# run-time: O(n)
# space: O(1)
# TODO: refactor
def min_subarray(target, nums):
    left = curr = 0
    ans = math.inf

    for right in range(len(nums)):
        curr += nums[right]

        while curr >= target:
            # in case you go below target
            ans = min(ans, right - left+1)
            # don't go below target
            if curr - nums[left] < target:
                break

            curr -= nums[left]
            left += 1
            ans = min(ans, right - left+1)

    return ans if ans < math.inf else 0

# TODO: solve O(n*log n), sort?

class TestMinSubarray(unittest.TestCase):

    def test_empty(self):
        target = 0
        nums = []
        expected = 0
        self.assertEqual(min_subarray(target, nums), expected)

    def test_same(self):
        target = 11
        nums = [1,1,1,1,1,1,1,1]
        expected = 0
        self.assertEqual(min_subarray(target, nums), expected)

    def test_7(self):
        target = 7
        nums = [2,3,1,2,4,3]
        expected = 2
        self.assertEqual(min_subarray(target, nums), expected)

    def test_4(self):
        target = 4
        nums = [1,4,4]
        expected = 1
        self.assertEqual(min_subarray(target, nums), expected)

    def test_11(self):
        target = 11
        nums = [1,2,3,4,5]
        expected = 3
        self.assertEqual(min_subarray(target, nums), expected)

    def test_15(self):
        target = 15
        nums = [1,2,3,4,5]
        expected = 5
        self.assertEqual(min_subarray(target, nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
