#!/usr/bin/env python3

import heapq
import math
import sys
import unittest

# number: 121
# section: array/string
# difficulty: easy
# tags: array, dynamic programming, top 150

# constraints
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

# solution: brute-force
# complexity
# run-time: O(n^2)
# space: O(1)
def max_profit1(prices):
    max_profit = -math.inf

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit if max_profit > 0 else 0

# solution: dp?
# complexity
# run-time: O(n)?
# space: O(1)?
def max_profit2(prices):
    max_profit = -math.inf
    min_idx = 0

    for i in range(1, len(prices)):
        profit = prices[i] - prices[min_idx]
        max_profit = max(max_profit, profit)

        if prices[i] < prices[min_idx]:
            min_idx = i

    return max_profit if max_profit > 0 else 0

# solution: heap
# complexity
# run-time: O(n*log n)
# space: O(n)
def max_profit3(prices):
    if not prices:
        return 0

    heap = [prices[0]]
    max_diff = -math.inf

    for i in range(1, len(prices)):
        # heap[0] is min element
        max_diff = max(max_diff, prices[i]-heap[0])
        heapq.heappush(heap, prices[i])
        #print(f"max_diff:{max_diff}")

    return max_diff if max_diff > 0 else 0

# TODO: solve using sliding window?

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
