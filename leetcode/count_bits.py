#!/usr/bin/env python3

import sys
import unittest

# number: 338
# title: Counting Bits
# url: https://leetcode.com/problems/counting-bits/
# difficulty: easy
# tags: dynamic programming, bit manipulation, grind 75

# constraints:
# 0 <= n <= 10^5

# complexity:
# run-time: O(log n)
def count(n):
    ones = 0

    while n:
        ones += (n & 1)
        n >>= 1

    return ones

# solution: brute force
# complexity:
# run-time: O(n*log n)
# space: O(1)
def count_bits(n: int) -> list[int]:
    ans = []

    for i in range(n+1):
        ans.append(count(i))

    return ans

# TODO: solve in linear time

class TestCountBits(unittest.TestCase):
    def test_2(self):
        n = 2
        expected = [0,1,1]
        self.assertEqual(count_bits(n), expected)

    def test_5(self):
        n = 5
        expected = [0,1,1,2,1,2]
        self.assertEqual(count_bits(n), expected)

    def test_10(self):
        n = 10
        expected = [0,1,1,2,1,2,2,3,1,2,2]
        self.assertEqual(count_bits(n), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())