#!/usr/bin/env python3

import sys
import unittest

# number: 67
# title: Add Binary
# url: https://leetcode.com/problems/add-binary/
# section: bit manipulation
# difficulty: easy
# tags: math, string, bit manipulation, simulation, top 150, meta, grind 75

# constraints
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# solution: Pythonic int/bin & addition
# run-time: O(n+m)
# space: O(max(n,m))
def add_bin(a, b):
    # convert binary string to int
    # add
    # convert int to binary string
    # slice: drop "0b" prefix
    return bin(int(a, 2) + int(b, 2))[2:]

# solution: Leetcode Pythonic int/bin & bitwise operators
# run-time: O(n+m)
# space: O(max(n,m))
# TODO: understand better
def add_bin2(a, b):
    # convert binary to int
    x, y = int(a, 2), int(b, 2)

    # while carry is non-0
    while y:
        # w/o carry
        answer = x ^ y
        # add carry
        carry = (x & y) << 1

        # store answer in x, carry in y
        x, y = answer, carry

        # one-liner
        #x, y = x ^ y, (x & y) << 1

    # drop "0b" prefix
    return bin(x)[2:]

class TestAddBin(unittest.TestCase):
    def test1(self):
        a = "11"
        b = "1"
        expected = "100"
        self.assertEqual(add_bin(a, b), expected)

    def test2(self):
        a = "1010"
        b = "1011"
        expected = "10101"
        self.assertEqual(add_bin(a, b), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
