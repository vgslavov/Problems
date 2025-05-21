#!/usr/bin/env python3

import sys
import unittest

# number: 283
# title: Move Zeroes
# url: https://leetcode.com/problems/move-zeroes/
# section: meta
# difficulty: easy
# tags: array, two pointers, meta

# constraints
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# in-place

# solution: sliding window
# complexity
# run-time: O(n)
# space: O(1)
def move_zeroes(nums):
    left = right = 0

    for right in range(len(nums)):
        #print(f"left:{left},right:{right}")

        # find next non-zero on right
        if nums[right] == 0:
            continue

        # keep swapping if 0 on left
        if nums[left] == 0:
            nums[left],nums[right] = nums[right],nums[left]

        left += 1

class TestMoveZeroes(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = []
        move_zeroes(nums)
        self.assertEqual(nums, expected)

    def test1(self):
        nums = [0,1,0,3,12]
        expected = [1,3,12,0,0]
        move_zeroes(nums)
        self.assertEqual(nums, expected)

    def test2(self):
        nums = [0]
        expected = [0]
        move_zeroes(nums)
        self.assertEqual(nums, expected)

    def test3(self):
        nums = [1,0,1]
        expected = [1,1,0]
        move_zeroes(nums)
        self.assertEqual(nums, expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
