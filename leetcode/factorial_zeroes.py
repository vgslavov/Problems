#!/usr/bin/env python3

from functools import cache
import sys
import unittest

# number: 172
# section: math
# difficulty: medium
# tags: math, top 150

# constraints
# 0 <= n <= 10^4

# complexity
# run-time: O(n)
# space: O(n)
# uses a lot of mem
@cache
def factorial(n):
    if not n:
        return 1

    return n * factorial(n-1)

# solution: recursive
# complexity
# run-time: O(n)
# space: O(n)
def factorial_zeroes(n):
    ans = factorial(n)
    #print(f"factorial:{ans}")

    count = 0
    while ans:
        #print(f"ans:{ans}")
        if ans % 10 == 0:
            count += 1
        else:
            break

        # integer division: to avoid scientific notion w/ large numbers
        ans //= 10

    return count

# TODO: solve in O(log n)

class TestFactorialZeroes(unittest.TestCase):

    def test_0(self):
        n = 0
        expected = 0
        self.assertEqual(factorial_zeroes(n), expected)

    def test_3(self):
        n = 3
        expected = 0
        self.assertEqual(factorial_zeroes(n), expected)

    def test_5(self):
        n = 5
        expected = 1
        self.assertEqual(factorial_zeroes(n), expected)

    def test_30(self):
        n = 30
        expected = 7
        self.assertEqual(factorial_zeroes(n), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
