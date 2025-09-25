#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: stack, monotonic stack

# solution: AlgoMonster stack
# complexity:
# run-time: O(n)
# space: O(n)
# TODO: understand better
def daily_temperatures(t: list[int]) -> list[int]:
    # store visited indices of t w/o solution
    stack = []
    # pre-fill with 0s
    ans = [0] * len(t)

    for i in range(len(t)):
        # current temp > last uncalc-ed temp
        while stack and t[i] > t[stack[-1]]:
            prev_i = stack.pop()
            # index difference is days difference
            ans[prev_i] = i-prev_i

        # lower temps: t[i] <= t[stack[-1]]
        stack.append(i)
        
    return ans

class TestDailyTemperatures(unittest.TestCase):
    
    def test_daily_temperatures(self):
        self.assertEqual(daily_temperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
        self.assertEqual(daily_temperatures([30,40,50,60]), [1,1,1,0])
        self.assertEqual(daily_temperatures([30,60,90]), [1,1,0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    t = [int(x) for x in input().split()]
    res = daily_temperatures(t)
    print(" ".join(map(str, res)))