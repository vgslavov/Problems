#!/usr/bin/env python3

import math
import sys
import unittest

# number: 643
# title: Maximum Average Subarray I
# url: https://leetcode.com/problems/maximum-average-subarray-i/
# section: sliding window
# difficulty: easy
# tags: array, sliding window, leetcode 75

# constraints
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4

# solution: sliding window
# complexity
# run-time: O(n)
# space: O(1)
def find_max_avg(nums, k):
    if not nums:
        return 0

    sum = 0
    # nums can be -ve!
    ans = -math.inf

    # 1st window
    # k <= n!
    for i in range(k):
        sum += nums[i]

    # 1st avg
    ans = sum / k

    for i in range(k, len(nums)):
        # add current & remove first!
        sum += nums[i] - nums[i-k]
        ans = max(ans, sum / k)

    return ans

class TestFindMaxAvg(unittest.TestCase):
    def test_empty(self):
        nums = []
        k = 1
        expected = 0
        self.assertEqual(find_max_avg(nums, k), expected)

    def test_1(self):
        nums = [1,12,-5,-6,50,3]
        k = 4
        expected = 12.75
        self.assertEqual(find_max_avg(nums, k), expected)

    def test_2(self):
        nums = [5]
        k = 1
        expected = 5
        self.assertEqual(find_max_avg(nums, k), expected)

    def test_3(self):
        nums = [-1]
        k = 1
        expected = -1
        self.assertEqual(find_max_avg(nums, k), expected)

    def test_4(self):
        nums = [4,0,4,3,3]
        k = 5
        expected = 2.8
        self.assertEqual(find_max_avg(nums, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
