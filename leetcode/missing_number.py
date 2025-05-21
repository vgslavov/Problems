#!/usr/bin/env python3

import sys
import unittest

# number: 268
# title: Missing Number
# url: https://leetcode.com/problems/missing-number/
# section: array
# difficulty: easy
# tags: array, bit manipulation, math, top 150

# constraints
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

# solution: sort + linear scan
# complexity
# run-time: O(n*log n)
# space: O(1)
def missing_number1(nums):
    nums.sort()

    if nums and nums[0] != 0:
        return 0

    for i in range(len(nums)-1):
        if nums[i] + 1 != nums[i+1]:
            return nums[i] + 1

    return nums[-1] + 1 if nums else False

# solution: dict
# run-time: O(n)
# space: O(n)
def missing_number2(nums):
    if not nums:
        return False

    max_num = max(nums)
    d = { n: 0 for n in range(max_num+1) }

    for i in range(len(nums)):
        d[nums[i]] += 1

    for k,v in d.items():
        if not v:
            return k

    return max_num + 1

# solution: math
# run-time: O(n)
# space: O(1)
def missing_number3(nums):
    if not nums:
        return False

    max_num = max(nums)
    min_num = min(nums)

    if min_num != 0:
        return 0

    # formula: n * (n+1) / 2
    real_sum = max_num * (max_num+1) // 2
    actual_sum = sum(nums)

    if real_sum == actual_sum:
        return max_num + 1

    return real_sum - actual_sum

class TestMissingNumber(unittest.TestCase):
    def test_empty(self):
        nums = []
        self.assertFalse(missing_number1(nums))
        self.assertFalse(missing_number2(nums))
        self.assertFalse(missing_number3(nums))

    def test_0(self):
        nums = [1]
        expected = 0
        self.assertEqual(missing_number1(nums), expected)
        self.assertEqual(missing_number2(nums), expected)
        self.assertEqual(missing_number3(nums), expected)

    def test_1(self):
        nums = [1,0]
        expected = 2
        self.assertEqual(missing_number1(nums), expected)
        self.assertEqual(missing_number2(nums), expected)
        self.assertEqual(missing_number3(nums), expected)

    def test_2(self):
        nums = [3,0,1]
        expected = 2
        self.assertEqual(missing_number1(nums), expected)
        self.assertEqual(missing_number2(nums), expected)
        self.assertEqual(missing_number3(nums), expected)

    def test_3(self):
        nums = [0,1]
        expected = 2
        self.assertEqual(missing_number1(nums), expected)
        self.assertEqual(missing_number2(nums), expected)
        self.assertEqual(missing_number3(nums), expected)

    def test_4(self):
        nums = [9,6,4,2,3,5,7,0,1]
        expected = 8
        self.assertEqual(missing_number1(nums), expected)
        self.assertEqual(missing_number2(nums), expected)
        self.assertEqual(missing_number3(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
