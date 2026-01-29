#!/usr/bin/env python3

import sys
import unittest

# number: 739
# title: Daily Temperatures
# url: https://leetcode.com/problems/daily-temperatures/
# difficulty: medium
# tags: stack, array, monotonic stack, grind 75

# constraints
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100

# solution: monotonic stack
# complexity
# run-time: O(n)
# space: O(n)
def daily_temperatures(temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures) 
    # uncalc-ed indices
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_i = stack.pop()
            ans[prev_i] = i-prev_i

        stack.append(i)

    return ans

class TestDailyTemperatures(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(daily_temperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])

    def test_example2(self):
        self.assertEqual(daily_temperatures([30,40,50,60]), [1,1,1,0])

    def test_example3(self):
        self.assertEqual(daily_temperatures([30,60,90]), [1,1,0])

if __name__ == "__main__":
    sys.exit(unittest.main())