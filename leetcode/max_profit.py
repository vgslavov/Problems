#!/usr/bin/env python3

import heapq
import math
import sys
import unittest

# number: 121
# title: Best Time to Buy and Sell Stock
# url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# section: array/string
# difficulty: easy
# tags: array, dynamic programming, top 150, citadel, grind 75

# constraints
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
# limit to 1 buy & 1 sell
# have to buy *before* you sell (can't short)

# solution: brute-force
# complexity
# run-time: O(n^2)
# space: O(1)
def max_profit1(prices):
    ans = -math.inf

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            ans = max(ans, profit)

    return ans if ans > 0 else 0

# solution: one pass to find biggest diff by finding cheapest price
# complexity
# run-time: O(n)
# space: O(1)
def max_profit2(prices):
    ans = -math.inf
    min_idx = 0

    for i in range(1, len(prices)):
        profit = prices[i] - prices[min_idx]
        ans = max(ans, profit)

        if prices[i] < prices[min_idx]:
            min_idx = i

    return ans if ans > 0 else 0

# solution: min heap
# complexity
# run-time: O(n*log n)
# space: O(n)
def max_profit3(prices):
    if not prices:
        return 0

    heap = [prices[0]]
    ans = -math.inf

    for i in range(1, len(prices)):
        # heap[0] is min element
        ans = max(ans, prices[i]-heap[0])
        heapq.heappush(heap, prices[i])
        #print(f"max_diff:{max_diff}")

    return ans if ans > 0 else 0

# TODO: solve using sliding window & DP

class TestMaxProfit(unittest.TestCase):

    def test_empty(self):
        prices = []
        expected = 0

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)
        self.assertEqual(max_profit3(prices), expected)

    def test_profit1(self):
        prices = [7,1,5,3,6,4]
        expected = 5

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)
        self.assertEqual(max_profit3(prices), expected)

    def test_profit2(self):
        prices = [7,6,4,3,1]
        expected = 0

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)
        self.assertEqual(max_profit3(prices), expected)

    def test_profit3(self):
        prices = [2,4,1]
        expected = 2

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)
        self.assertEqual(max_profit3(prices), expected)

    def test_profit4(self):
        prices = [2,1,2,1,0,1,2]
        expected = 2

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)
        self.assertEqual(max_profit3(prices), expected)

    def test_profit5(self):
        prices = [2,1,2,0,1]
        expected = 1

        self.assertEqual(max_profit1(prices), expected)
        self.assertEqual(max_profit2(prices), expected)
        self.assertEqual(max_profit3(prices), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
