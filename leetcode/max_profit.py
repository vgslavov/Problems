#!/usr/bin/env python3

import math
import sys
import unittest

# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

# O(n^2)
def max_profit1(prices):
    max_profit = -math.inf

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit if max_profit > 0 else 0

# O(n)
def max_profit2(prices):
    max_profit = -math.inf
    min_idx = 0

    for i in range(1, len(prices)):
        profit = prices[i] - prices[min_idx]
        if profit > max_profit:
            max_profit = profit

        if prices[i] < prices[min_idx]:
            min_idx = i

    return max_profit if max_profit > 0 else 0

class TestMaxProfit(unittest.TestCase):

    def test_empty(self):
        prices = []
        expected = 0

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)

    def test_profit1(self):
        prices = [7,1,5,3,6,4]
        expected = 5

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)

    def test_profit2(self):
        prices = [7,6,4,3,1]
        expected = 0

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)

    def test_profit3(self):
        prices = [2,4,1]
        expected = 2

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)

    def test_profit4(self):
        prices = [2,1,2,1,0,1,2]
        expected = 2

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)

    def test_profit5(self):
        prices = [2,1,2,0,1]
        expected = 1

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
