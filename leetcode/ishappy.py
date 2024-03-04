#!/usr/bin/env python3

import sys
import unittest

def pow_digits(n):
    s = str(n)

    sum = 0
    for i in range(len(s)):
        sum += pow(int(s[i]), 2)

    return sum

# 1 <= n <= 2^31 - 1
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
