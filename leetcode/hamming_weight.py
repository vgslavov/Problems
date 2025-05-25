#!/usr/bin/env python3

import sys
import unittest

# number: 191
# title: Number of 1 Bits
# url: https://leetcode.com/problems/number-of-1-bits/
# section: bit manipulation
# difficulty: easy
# tags: divide & conquer, bit manipulation, top 150

# constraints
# 1 <= n <= 2^31 - 1

# solution: compare to 1 & halve
# complexity
# run-time: O(log n)
# space: O(1)
def hamming_weight(n):
    count = 0

    while n:
        count += (n & 1)
        n >>= 1

    return count

# solution: no division
# complexity
# run-time: O(n)?
# space: O(1)
def hamming_weight2(n):
    count = 0

    while n:
        n &= n - 1
        count += 1

    return count

class TestHammingWeight(unittest.TestCase):

    def test_0(self):
        n = 0
        expected = 0
        self.assertEqual(hamming_weight(n), expected)
        self.assertEqual(hamming_weight2(n), expected)

    def test_11(self):
        n = 11
        expected = 3
        self.assertEqual(hamming_weight(n), expected)
        self.assertEqual(hamming_weight2(n), expected)

    def test_128(self):
        n = 128
        expected = 1
        self.assertEqual(hamming_weight(n), expected)
        self.assertEqual(hamming_weight2(n), expected)

    def test_2147483645(self):
        n = 2147483645
        expected = 30
        self.assertEqual(hamming_weight(n), expected)
        self.assertEqual(hamming_weight2(n), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
