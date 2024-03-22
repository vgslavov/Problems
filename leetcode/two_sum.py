#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

# O(n^2): slow!
def two_sum1(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return [-1,-1]

# extra: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
# O(n)
def two_sum2(nums, target):
    # value to list indices
    d = defaultdict(list)

    for i in range(len(nums)):
        d[nums[i]].append(i)

    for i in range(len(nums)):
        sub = target - nums[i]
        if sub not in d:
            continue

        for idx in d[sub]:
            if idx != i:
                return [i, idx]

    return [-1,-1]

# O(n): smaller const
def two_sum3(nums, target):
    # value to index
    d = {}
    for i in range(len(nums)):
        sub = target - nums[i]

        if sub in d:
            return [d[sub], i]

        d[nums[i]] = i

    return [-1,-1]

class TestTwoSum(unittest.TestCase):
    def test_empty(self):
        nums = []
        target = 0
        expected = [-1, -1]
        self.assertEqual(two_sum1(nums, target), expected)
        self.assertEqual(two_sum2(nums, target), expected)
        self.assertEqual(two_sum3(nums, target), expected)

    def test1(self):
        nums = [2,7,11,15]
        target = 9
        expected = [0,1]
        self.assertEqual(two_sum1(nums, target), expected)
        self.assertEqual(two_sum2(nums, target), expected)
        self.assertEqual(two_sum3(nums, target), expected)

    def test2(self):
        nums = [3,2,4]
        target = 6
        expected = [1,2]
        self.assertEqual(two_sum1(nums, target), expected)
        self.assertEqual(two_sum2(nums, target), expected)
        self.assertEqual(two_sum3(nums, target), expected)

    def test3(self):
        nums = [3,3]
        target = 6
        expected = [0,1]
        self.assertEqual(two_sum1(nums, target), expected)
        self.assertEqual(two_sum2(nums, target), expected)
        self.assertEqual(two_sum3(nums, target), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
