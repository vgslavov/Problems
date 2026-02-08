#!/usr/bin/env python3

import sys
import unittest

# number: 134
# title: Gas Station
# url: https://leetcode.com/problems/gas-station/
# section: array / string
# difficulty: medium
# tags: array, greedy, top 150, grind 75

# constraints
# n == gas.length == cost.length
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4
# The input is generated such that the answer is unique.

# solution: Neetcode greedy
# complexity
# run-time: O(n)
# space: O(1)
def can_complete_circuit(gas, cost):
    # don't have enough gas to cover cost
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0

    for i in range(len(gas)-1):
        # calc diff array: what gas is left after driving to i+1
        diff = gas[i] - cost[i]
        total += diff

        # ran out of gas, start on next station
        if total < 0:
            total = 0
            start = i+1

    return start

# TODO: solve using two pointers

class TestCanCompleteCircuit(unittest.TestCase):

    def test_example1(self):
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        expected = 3
        self.assertEqual(can_complete_circuit(gas, cost), expected)

    def test_example2(self):
        gas = [2,3,4]
        cost = [3,4,3]
        expected = -1
        self.assertEqual(can_complete_circuit(gas, cost), expected)

    def test_example3(self):
        gas = [3,1,1]
        cost = [1,2,2]
        expected = 0
        self.assertEqual(can_complete_circuit(gas, cost), expected)

    def test_example4(self):
        gas = [5,1,2,3,4]
        cost = [4,4,1,5,1]
        expected = 4
        self.assertEqual(can_complete_circuit(gas, cost), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())