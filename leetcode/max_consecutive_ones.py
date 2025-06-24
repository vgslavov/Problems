#!/usr/bin/env python3

import sys
import unittest

# number: 1004
# title: Max Consecutive Ones III
# url: https://leetcode.com/problems/max-consecutive-ones-iii/
# section: sliding window
# difficulty: medium
# tags: array, binary search, sliding window, prefix sum, leetcode 75, meta

# constraints
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
# k: how many 0s to flip

# complexity
# run-time: O(n)
# space: O(1)
def max_consecutive_ones(nums, k):
    left = curr = ans = 0

    for right in range(len(nums)):
        # count 0s
        if nums[right] == 0:
            curr += 1

        # too many 0s
        while curr > k:
            # remove 0s
            if nums[left] == 0:
                curr -= 1
            # shrink window
            left += 1

        # update answer
        ans = max(ans, right - left + 1)

    return ans

class TestMaxConsecutiveOnes(unittest.TestCase):
    def test_empty(self):
        nums = []
        k = 1
        expected = 0
        self.assertEqual(max_consecutive_ones(nums, k), expected)

    def test_1(self):
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        k = 2
        expected = 6
        self.assertEqual(max_consecutive_ones(nums, k), expected)

    def test_2(self):
        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        k = 3
        expected = 10
        self.assertEqual(max_consecutive_ones(nums, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
