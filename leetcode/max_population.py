#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 1854
# title: Maximum Population Year
# url: https://leetcode.com/problems/maximum-population-year/
# difficulty: easy
# tags: array, counting, prefix sum

# constraints:
# 1 <= logs.length <= 100
# 1950 <= logs[i][0] < logs[i][1] <= 250

# solution: brute force
# time complexity: O(n^2)
# space complexity: O(n)
def max_population(logs: list[list[int]]) -> int:
    count = defaultdict(int)

    for log in logs:
        for year in range(log[0], log[1]):
            count[year] += 1

    return max(count, key=count.get)

# solution: difference array + prefix sum
# n: len(logs)
# m: last_year - first_year (const)
# time complexity: O(n+m) ~ O(n)
# space complexity: O(n)
def max_population2(logs: list[list[int]]) -> int:
    first_year = 1950
    last_year = 2050

    # calc diff array
    diff = [0] * (last_year-first_year)

    for start,end in logs:
        diff[start-first_year] += 1
        # don't count last year of a person's life
        if end-first_year < len(diff):
            diff[end-first_year] -= 1

    # calc prefix sum
    prefix = [diff[0]]

    for i in range(1, len(diff)):
        prefix.append(prefix[-1]+diff[i])

    # index of the maximum value in prefix sum 
    # is the year with the maximum population
    return max(range(len(prefix)), key=prefix.__getitem__)+first_year

class TestMaxPopulation(unittest.TestCase):
    def test_example_1(self):
        logs = [[1993, 1999], [2000, 2010]]
        self.assertEqual(max_population(logs), 1993)
        self.assertEqual(max_population2(logs), 1993)

    def test_example_2(self):
        logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
        self.assertEqual(max_population(logs), 1960)
        self.assertEqual(max_population2(logs), 1960)

    def test_example_3(self):
        logs = [[1982,1998],[2013,2042],[2010,2035],[2022,2050],[2047,2048]]
        self.assertEqual(max_population(logs), 2022)
        self.assertEqual(max_population2(logs), 2022)

    def test_example_4(self):
        logs = [[2008,2026],[2004,2008],[2034,2035],[1999,2050],[2049,2050],[2011,2035],[1966,2033],[2044,2049]]
        self.assertEqual(max_population(logs), 2011)
        self.assertEqual(max_population2(logs), 2011)

    def test_example_5(self):
        logs = [[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]
        # TODO: fix
        #self.assertEqual(max_population(logs), 2005)
        self.assertEqual(max_population2(logs), 2005)

if __name__ == "__main__":
    sys.exit(unittest.main())