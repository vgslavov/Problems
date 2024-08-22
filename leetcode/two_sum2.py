#!/usr/bin/env python3

import sys
import unittest

# number: 167
# section: two pointers
# difficulty: medium
# tags: array, two pointers, binary search, top 150

# constraints
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

# complexity
# run-time: O(log n)
# space: O(1)

def binary_search(nums, target):
    start = 0
    end = len(nums)-1

    while start < end:
        mid = start + (end-start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= target:
            end = mid
        else:
            start = mid+1

    # duplicates: left-most insertion point
    return start

def two_sum2(nums, target):
    for i in range(len(nums)):
        sub = target - nums[i]
        j = binary_search(nums, sub)

        # duplicates
        if i == j:
            continue

        if nums[i] + nums[j] == target:
            # duplicates
            return sorted([i+1, j+1])

    return None

# TODO: solve linearly

class TestTwoSum2(unittest.TestCase):
    def test_empty(self):
        nums = []
        target = None
        self.assertFalse(two_sum2(nums, target))

    def test_1(self):
        nums = [2,7,11,15]
        target = 9
        expected = [1,2]
        self.assertEqual(two_sum2(nums, target), expected)

    def test_2(self):
        nums = [2,3,4]
        target = 6
        expected = [1,3]
        self.assertEqual(two_sum2(nums, target), expected)

    def test_3(self):
        nums = [-1,0]
        target = -1
        expected = [1,2]
        self.assertEqual(two_sum2(nums, target), expected)

    def test_4(self):
        nums = [5,25,75]
        target = 100
        expected = [2,3]
        self.assertEqual(two_sum2(nums, target), expected)

    def test_5(self):
        nums = [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
        target = 542
        expected = [24,32]
        self.assertEqual(two_sum2(nums, target), expected)

    def test_6(self):
        nums = [0,0,3,4]
        target = 0
        expected = [1,2]
        self.assertEqual(two_sum2(nums, target), expected)

    def test_7(self):
        nums = [1,2,3,4,4,9,56,90]
        target = 8
        expected = [4,5]
        self.assertEqual(two_sum2(nums, target), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
