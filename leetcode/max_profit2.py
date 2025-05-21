#!/usr/bin/env python3

import sys
import unittest

# number: 122
# title: Best Time to Buy and Sell Stock II
# url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# section: array/string
# difficulty: medium
# tags: array, dp, greedy, top 150

# constraints
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4
# multiple buys & sells
# but hold at most one share of stock at a time

# solution: Leetcode greedy
# complexity
# run-time: O(n)
# space: O(1)
def max_profit2(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

# TODO: solve using peak valley & DP?

class TestMaxProfit(unittest.TestCase):
    def test_empty(self):
        prices = []
        expected = 0
        self.assertEqual(max_profit2(prices), expected)

    def test1(self):
        prices = [7,1,5,3,6,4]
        expected = 7
        self.assertEqual(max_profit2(prices), expected)

    def test2(self):
        prices = [1,2,3,4,5]
        expected = 4
        self.assertEqual(max_profit2(prices), expected)

    def test3(self):
        prices = [7,6,4,3,1]
        expected = 0
        self.assertEqual(max_profit2(prices), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
