#!/usr/bin/env python3

from functools import cache
import sys
import unittest

# number: 70
# section: 1D DP
# difficulty: easy
# tags: math, dp, memoization, top 150

# constraints
# 1 <= n <= 45

# solution: recursive top-down 1D DP using dict
# complexity
# run-time: O(n)
# space: O(n)
def climb_stairs(n: int) -> int:
    def dp(i):
        # base case
        if i in (1,2):
            return i

        # check cache
        if i in memo:
            return memo[i]

        # calc recurrence relation
        memo[i] = dp(i-1) + dp(i-2)
        #print(f"memo[{i}]:{memo[i]}")

        # return recurrence relation
        return memo[i]

    # cache or use @functools.cache
    memo = {}
    return dp(n)

# solution: recursive top-down 1D DP using functools
# complexity
# run-time: O(n)
# space: O(n)
def climb_stairs2(n: int) -> int:
    @cache
    def dp(i):
        # base case
        if i in (1,2):
            return i

        # recurrence relation
        return dp(i-1) + dp(i-2)

    return dp(n)

# solution: iterative bottom-up 1D DP
# complexity
# run-time: O(n)
# space: O(n)
def climb_stairs3(n: int) -> int:
    # init
    dp = [0] * (n+1)

    if n == 1:
        return n

    # base cases
    dp[1] = 1
    dp[2] = 2

    # recurrence relation
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

if __name__ == '__main__':
    sys.exit(unittest.main())
