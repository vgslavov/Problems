#!/usr/bin/env python3

import math
import sys
import unittest

# number: 322
# title: Coin Change
# url: https://leetcode.com/problems/coin-change/
# difficulty: medium
# tags: array, dp, bfs, top 150, grind 75

# constraints
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4

# solution: recursive top-down 1D DP using dict
# complexity
# run-time: O(n*m)
# space: O(n)
def coin_change(coins: list[int], amount: int) -> int:
    def dp(a):
        if a == 0:
            return 0

        if a in memo:
            return memo[a]

        ans = math.inf

        for c in coins:
            if a - c >= 0:
                ans = min(ans, 1+dp(a-c))

        memo[a] = ans
        return ans

    memo = {}
    ans = dp(amount)
    return ans if ans < math.inf else -1

# TODO: solve bottom-up 1D DP

class TestCoinChange(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(coin_change([2], 3), -1)
        self.assertEqual(coin_change([1], 0), 0)
        self.assertEqual(coin_change([1], 1), 1)
        self.assertEqual(coin_change([1], 2), 2)
        self.assertEqual(coin_change([1], 3), 3)
        self.assertEqual(coin_change([1], 4), 4)

if __name__ == "__main__":
    sys.exit(unittest.main())