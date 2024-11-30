#!/usr/bin/env python3

from collections import defaultdict
from functools import cache
import math
import sys
import unittest

# number: 1128
# section: assessments
# difficulty: easy
# tags: array, hash table, counting, amazon

# constraints
# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9

# solution: dict + math.comb
# complexity
# run-time: O(n)
# space: O(n)
def domino_pairs(dominoes) -> int:
    ans = 0
    counts = defaultdict(int)

    for i in range(len(dominoes)):
        counts[tuple(sorted(dominoes[i]))] += 1

    return sum([math.comb(v,2) for v in counts.values()])

# complexity
# run-time: O(n)
# space: O(n)
def combinations(n, k):
    #print(f"n:{n},k:{k}")

    #@cache
    def dp(i):
        # base case
        if i <= 1:
            return 1

        # check cache
        if i in memo:
            return memo[i]

        # recurrence relation
        memo[i] = dp(i-1)*i
        return memo[i]

        # if cache
        #return dp(i-1)*i

    memo = {}

    # integer division: when k > n, combinations are 0!
    return dp(n) // (dp(n-k)*dp(k))

# solution: dict + dp comb
# complexity
# run-time: O(n)
# space: O(n)
def domino_pairs2(dominoes) -> int:
    counts = defaultdict(int)

    for i in range(len(dominoes)):
        counts[tuple(sorted(dominoes[i]))] += 1

    return sum([combinations(v,2) for v in counts.values()])

class TestDominoPairs(unittest.TestCase):
    def test_combinations1(self):
        n = 6
        k = 2
        expected = 15
        self.assertEqual(combinations(n, k), expected)

    def test_combinations2(self):
        n = 2
        k = 2
        expected = 1
        self.assertEqual(combinations(n, k), expected)

    def test_combinations3(self):
        n = 3
        k = 2
        expected = 3
        self.assertEqual(combinations(n, k), expected)

    def test_combinations4(self):
        n = 1
        k = 2
        expected = 0
        self.assertEqual(combinations(n, k), expected)

    def test_empty(self):
        dominoes = []
        expected = 0
        self.assertEqual(domino_pairs(dominoes), expected)
        self.assertEqual(domino_pairs2(dominoes), expected)

    def test1(self):
        dominoes = [[1,2],[2,1],[3,4],[5,6]]
        expected = 1
        self.assertEqual(domino_pairs(dominoes), expected)
        self.assertEqual(domino_pairs2(dominoes), expected)

    def test2(self):
        dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
        expected = 3
        self.assertEqual(domino_pairs(dominoes), expected)
        self.assertEqual(domino_pairs2(dominoes), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
