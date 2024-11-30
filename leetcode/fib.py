#!/usr/bin/env python3

from functools import cache
import sys
import unittest

# number: 509
# section: assessments
# difficulty: easy
# tags: math, dp, recursion, memoization, microsoft

# constraints
# 0 <= n <= 30

# solution: top-down recursive DP using functools for memoization
# complexity
# run-time: O(n)
# space: O(n)
@cache
def fib(n: int) -> int:
    if n in (0,1):
        return n

    return fib(n-1) + fib(n-2)

# solution: top-down recursive DP using dict for memoization
# complexity
# run-time: O(n)
# space: O(n)
def fib2(n: int) -> int:
    def dp(i):
        # base case
        if i == 1:
            return 1
        elif i == 0:
            return 0

        # check cache
        if i in memo:
            return memo[i]

        # recurrence relation
        memo[i] = dp(i-1) + dp(i-2)
        return memo[i]

    memo = {}
    return dp(n)

# solution: bottom up iterative DP
# complexity
# run-time: O(n)
# space: O(n)
def fib3(n: int) -> int:
    # init
    d = [0] * (n+1)

    # base cases
    if not n:
        return 0

    d[1] = 1

    # recurrence relation
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]

class TestFib(unittest.TestCase):
    def test0(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib2(0), 0)
        self.assertEqual(fib3(0), 0)

    def test2(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib2(2), 1)
        self.assertEqual(fib3(2), 1)

    def test3(self):
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib2(3), 2)
        self.assertEqual(fib3(3), 2)

    def test4(self):
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib2(4), 3)
        self.assertEqual(fib3(4), 3)

if __name__ == '__main__':
    sys.exit(unittest.main())
