#!/usr/bin/env python3

import sys
import unittest

# number: 190
# title: Reverse Bits
# url: https://leetcode.com/problems/reverse-bits/
# section: bit manipulation
# difficulty: easy
# tags: divide & conquer, bit manipulation, top 150

# constraints
# The input must be a binary string of length 32

# solution: Pythonic, format string + slicing
# by: nneonneo on stackoverflow
# complexity
# run-time: O(n), slow!
# space: O(1)
def reverse_bits(n):
    # format() f-string:
    # 0: fill with 0s
    # width: of string
    # b: binary type
    # [::-1]: reverse string
    # int(): convert to binary
    width = 32
    b = '{:0{width}b}'.format(n, width=width)
    return int(b[::-1], 2)

# solution: loop & shift bits
# by: bit twiddling hacks
# run-time: O(1), slow!
# space: O(1)
def reverse_bits2(n):
    width = 32
    r = 0

    for _ in range(width):
        # multiply by 2
        r <<= 1
        r |= n & 1
        # or
        #r = (r << 1) + (n & 1)

        # divide by 2
        n >>= 1

    return r

# TODO: solve using lookup table

class TestReverseBits(unittest.TestCase):
    def test1(self):
        n = 43261596
        r = 964176192
        self.assertEqual(reverse_bits(n), r)
        self.assertEqual(reverse_bits2(n), r)

    def test2(self):
        n = 4294967293
        r = 3221225471
        self.assertEqual(reverse_bits(n), r)
        self.assertEqual(reverse_bits2(n), r)

if __name__ == '__main__':
    sys.exit(unittest.main())
