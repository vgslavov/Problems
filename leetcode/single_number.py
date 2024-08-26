#!/usr/bin/env python3

import sys
import unittest

# number: 136
# section: bit manipulation
# difficulty: easy
# tags: array, bit manipulation, top 150, leetcode 75

# constraints
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears
# only once.

# solution: xor 2 bitmasks
# complexity
# run-time: O(n), slow
# space: O(1)
def toggle_bit(value, offset):
    return value ^ (1 << offset)

def get_normalized_bit(value, offset):
    return (value >> offset) & 1

def single_number(nums):
    # negative bitmask
    bitmask1 = 0
    # positive bitmask
    bitmask2 = 0

    for n in nums:
        if n < 0:
            n = abs(n)
            bitmask1 = toggle_bit(bitmask1, n)
        else:
            bitmask2 = toggle_bit(bitmask2, n)

    for n in nums:
        if n < 0:
            n = abs(n)
            if get_normalized_bit(bitmask1, n):
                return -n
        elif get_normalized_bit(bitmask2, n):
            return n

    return 0

# solution: xor 1 bitmask
# complexity
# run-time: O(n)
# space: O(1)
def single_number2(nums):
    mask = 0

    # x ^ x = 0
    # 0 ^ y = y
    # x ^ x ^ y = y
    for n in nums:
        mask ^= n

    return mask

class TestSingleNumber(unittest.TestCase):
    def test_1(self):
        nums = [2,2,1]
        expected = 1
        self.assertEqual(single_number(nums), expected)
        self.assertEqual(single_number2(nums), expected)

    def test_4(self):
        nums = [4,1,2,1,2]
        expected = 4
        self.assertEqual(single_number(nums), expected)
        self.assertEqual(single_number2(nums), expected)

    def test_single(self):
        nums = [1]
        expected = 1
        self.assertEqual(single_number(nums), expected)
        self.assertEqual(single_number2(nums), expected)

    def test_negative(self):
        nums = [-1]
        expected = -1
        self.assertEqual(single_number(nums), expected)
        self.assertEqual(single_number2(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
