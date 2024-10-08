#!/usr/bin/env python3

import sys
import unittest

# number: 746
# difficulty: easy
# tags: array, dynamic programming

# constraints

# solution: recursive top-down 1D DP using dict
# complexity
# run-time: O(n)
# space: O(n)
def min_cost_clim_stairs(cost) -> int:
    def dp(i):
        # base case
        if i in (0,1):
            return 0

        # check cache
        if i in memo:
            return memo[i]

        # recurrence relation
        memo[i] = min(dp(i-1)+cost[i-1], dp(i-2)+cost[i-2])

        return memo[i]

    memo = {}
    return dp(len(cost))

# solution: recursive top-down 1D DP using functools
# complexity
# run-time: O(n)
# space: O(n)
def min_cost_clim_stairs(cost) -> int:
    @cache
    def dp(i):
        # base case
        if i in (0,1):
            return 0

        # recurrence relation
        return min(dp(i-1)+cost[i-1], dp(i-2)+cost[i-2])

    return dp(len(cost))


if __name__ == '__main__':
    sys.exit(unittest.main())
