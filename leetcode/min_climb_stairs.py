#!/usr/bin/env python3

import sys
import unittest

# number: 746
# title: Min Cost Climbing Stairs
# url: https://leetcode.com/problems/min-cost-climbing-stairs/
# difficulty: easy
# tags: array, dp

# constraints
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

# solution: recursive top-down 1D DP using dict
# complexity
# run-time: O(n)
# space: O(n)
def min_cost_climb_stairs(cost) -> int:
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
def min_cost_climb_stairs2(cost) -> int:
    @cache
    def dp(i):
        # base case
        if i in (0,1):
            return 0

        # recurrence relation
        return min(dp(i-1)+cost[i-1], dp(i-2)+cost[i-2])

    return dp(len(cost))

# solution: iterative bottom-up 1D DP
# complexity
# run-time: O(n)
# space: O(n)
def min_cost_climb_stairs3(cost) -> int:
    # init + base cases
    dp = [0] * (len(cost)+1)

    # recurrence relation
    for i in range(2, len(cost)+1):
        # why not?
        #memo[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

    return dp[len(cost)]

if __name__ == '__main__':
    sys.exit(unittest.main())
