#!/usr/bin/env python3

import math
import sys
import unittest

# number: 309
# section: optiver
# difficulty: medium
# tags: array, dp, optiver

# constraints
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

# solution: Leetcode state machine
# complexity
# run-time: O(n)
# space: O(1)
def max_profit_cooldown(prices):
    # states

    # initial and transient b/w sold and held (for cooldown)
    reset = 0

    # just sold
    sold = -math.inf

    # just bought or rest
    held = -math.inf

    # transitions
    # reset -buy-> held -sell-> sold -rest-> reset
    # \rest/      \rest/                    \rest/

    for p in prices:
        # save state for later
        pre_sold = sold

        # prev state: held (sell) + proceeds of sale
        sold = held + p

        # prev state: held (rest)
        # or reset (buy) - cost of purchase (just bought)
        held = max(held, reset-p)

        # prev state: reset (rest)
        # or sold (rest), just sold
        reset = max(reset, pre_sold)

    # can't hold, have to sell!
    return max(reset, sold)

class TestMaxProfitCooldown(unittest.TestCase):
    def test_empty(self):
        prices = []
        expected = 0
        self.assertEqual(max_profit_cooldown(prices), expected)

    def test1(self):
        prices = [1,2,3,0,2]
        expected = 3
        self.assertEqual(max_profit_cooldown(prices), expected)

    def test2(self):
        prices = [1]
        expected = 0
        self.assertEqual(max_profit_cooldown(prices), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
