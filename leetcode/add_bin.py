#!/usr/bin/env python3

import sys
import unittest

# number: 67
# section: bit manipulation
# difficulty: easy
# tags: math, string, bit manipulation, simulation, top 150

# constraints
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# solution: Pythonic
# run-time: O(1)
# space: O(1)
def add_bin(a, b):
    # convert binary string to int
    # add
    # convert int to binary string
    # slice
    return bin(int(a, 2) + int(b, 2))[2:]

# TODO: add unit tests, solve using bin arithmetic

if __name__ == '__main__':
    sys.exit(unittest.main())
