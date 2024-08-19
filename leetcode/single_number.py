#!/usr/bin/env python3

import sys
import unittest

# number: 136
# section: bit manipulation
# difficulty: easy
# tags: array, bit manipulation, top 150

# constraints
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears
# only once.

# complexity
# run-time: O(n)
# space: O(1)
def toggle_bit(value, index):
    return value ^ (1 << index)

def get_normalized_bit(value, index):
    return (value >> index) & 1

def single_number(nums):
    bitmask = 0

    for n in nums:
        bitmask = toggle_bit(bitmask, n)

    for n in nums:
        if get_normalized_bit(bitmask, n):
            return n

    return 0

class TestSingleNumber(unittest.TestCase):
    def test_1(self):
        nums = [2,2,1]
        expected = 1
        self.assertEqual(single_number(nums), expected)

    def test_4(self):
        nums = [4,1,2,1,2]
        expected = 4
        self.assertEqual(single_number(nums), expected)

    def test_single(self):
        nums = [1]
        expected = 1
        self.assertEqual(single_number(nums), expected)

    # TODO: support negative numbers
    def test_negative(self):
        nums = [-1]
        expected = -1
        self.assertEqual(single_number(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
