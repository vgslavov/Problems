#!/usr/bin/env python3

import sys
import unittest

# number: 202
# section: hashmap
# difficulty: easy
# tags: hash table, math, two pointers, top 150

# description
# A happy number is a number defined by the following process:
# * Starting with any positive integer, replace the number by the sum of the
#   squares of its digits.
# * Repeat the process until the number equals 1 (where it will stay), or it
#   loops endlessly in a cycle which does not include 1.
# * Those numbers for which this process ends in 1 are happy.

def pow_digits(n):
    s = str(n)

    sum = 0
    for i in range(len(s)):
        sum += pow(int(s[i]), 2)

    return sum

# constraints
# 1 <= n <= 2^31 - 1

# complexity
# run-time: O(log n)
# space: O(1)
def ishappy(n):
    if not n:
        return False

    n = pow_digits(n)
    # TODO: figure out a max
    max = 10
    count = 0
    while n != 1 and count < max:
        n = pow_digits(n)
        count += 1

    return n == 1

class TestIsHappy(unittest.TestCase):
    def test_empty(self):
        n = None
        self.assertFalse(ishappy(n))

    def test_true(self):
        n = 19
        self.assertTrue(ishappy(n))

    def test_false(self):
        n = 2
        self.assertFalse(ishappy(n))

if __name__ == '__main__':
    sys.exit(unittest.main())
