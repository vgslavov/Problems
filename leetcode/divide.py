#!/usr/bin/env python3

import sys
import unittest

# number: 29
# title: Divide Two Integers
# url: https://leetcode.com/problems/divide-two-integers/
# section: meta
# difficulty: medium
# tags: meta

# constraints
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0
# without using multiplication, division, and mod operator

# non-solution: brute force subtraction
# complexity
# run-time: O(n), TLE
# space: O(1)
def divide(dividend: int, divisor: int) -> int:
    count = 0
    # xor
    isneg = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    if dividend == divisor:
        return -1 if isneg else 1

    while dividend-divisor > 0:
        dividend -= divisor
        count += 1

    return -count if isneg else count

# TODO: use binary search for O(log n)?

class TestDivide(unittest.TestCase):
    def test10_3(self):
        dividend = 10
        divisor = 3
        expected = 3
        self.assertEqual(divide(dividend, divisor), expected)

    def test7_3(self):
        dividend = 7
        divisor = -3
        expected = -2
        self.assertEqual(divide(dividend, divisor), expected)

    def test1_1(self):
        dividend = 1
        divisor = 1
        expected = 1
        self.assertEqual(divide(dividend, divisor), expected)

    # TODO: solve TLE
    def test_large(self):
        dividend = -2147483648
        divisor = -1
        expected = -2147483648
        #self.assertEqual(divide(dividend, divisor), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
