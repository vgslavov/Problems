#!/usr/bin/env python3

from functools import cache
import sys
import unittest

# number: 198
# section: 1D DP
# difficulty: medium
# tags: array, dp, top 150

# constraints
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# solution: recursive top-down 1D DP using dict
# complexity
# run-time: O(n)
# space: O(n)
def rob(nums) -> int:
    def dp(i):
        # base case
        if i == 0:
            return nums[0]
        elif i == 1:
            return max(nums[0], nums[1])

        # cache
        if i in memo:
            return memo[i]

        # recurrence relation
        memo[i] = max(dp(i-1), dp(i-2)+nums[i])

        return memo[i]

    memo = {}
    return dp(len(nums)-1)

# solution: recursive top-down 1D DP using functools
# complexity
# run-time: O(n)
# space: O(n)
def rob2(nums) -> int:
    @cache
    def dp(i):
        # base case
        if i == 0:
            return nums[0]
        elif i == 1:
            return max(nums[0], nums[1])

        # recurrence relation
        return max(dp(i-1), dp(i-2)+nums[i])

    return dp(len(nums)-1)

# solution: iterative bottom-up 1D DP
# complexity
# run-time: O(n)
# space: O(n)
def rob3(nums) -> int:
    # init
    dp = [0] * len(nums)

    if len(nums) == 1:
        return nums[0]

    # base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # recurrence relation
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    return dp[len(nums)-1]

if __name__ == '__main__':
    sys.exit(unittest.main())
