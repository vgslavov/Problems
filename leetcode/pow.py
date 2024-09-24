#!/usr/bin/env python3

import sys
import unittest

# number: 50
# section: math
# tags: math, recursion, top 150

# constraints
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= x^n <= 10^4

# solution: brute-force iterative
# complexity
# run-time: O(n), slow!
# space: O(1)
def pow(x, n):
    isneg = False
    if not n:
        return 1
    elif n < 0:
        n *= -1
        isneg = True

    ans = x
    n -= 1

    while n:
        ans *= x
        n -= 1

    return 1/ans if isneg else ans

# solution: brute-force recursive
# complexity
# run-time: O(n), slow!
# space: O(1)
def pow2(x, n):
    if not n:
        return 1
    elif n < 0:
        return 1 / pow(x, -n)

    return x * pow2(x, n-1)

class TestPow(unittest.TestCase):
    def test_0(self):
        x = 0.44528
        n = 0
        expected = 1
        self.assertEqual(pow(x, n), expected)
        self.assertEqual(pow2(x, n), expected)

    def test1(self):
        x = 2.00000
        n = 10
        expected = 1024.0
        self.assertEqual(pow(x, n), expected)
        self.assertEqual(pow2(x, n), expected)

    def test2(self):
        x = 2.10000
        n = 3
        expected = 9.26100
        self.assertEqual(round(pow(x, n), 5), expected)
        self.assertEqual(round(pow2(x, n), 5), expected)

    def test_large(self):
        x = 0.00001
        n = 2147483647
        expected = 0
        # TODO: too slow
        #self.assertEqual(pow(x, n), expected)
        #self.assertEqual(pow2(x, n), expected)

    def test_neg(self):
        x = 2.00000
        n = -2
        expected = 0.25000
        self.assertEqual(round(pow(x, n), 5), expected)
        self.assertEqual(round(pow2(x, n), 5), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())