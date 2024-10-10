#!/usr/bin/env python3

import itertools
import sys
import unittest

# number: 77
# section: backtracking
# difficulty: medium
# tags: backtracking, top 150

# constraints
# 1 <= n <= 20
# 1 <= k <= n

# solution: itertools
# complexity
# run-time: O(n choose k)
# space: O(n choose k)
def combine(n: int, k: int):
    # range(start, stop): [start, stop)!
    return [list(v) for v in itertools.combinations(list(range(1, n+1)), k)]

# TODO: calc combinations manually

class TestCombine(unittest.TestCase):
    def test_empty(self):
        n = 0
        k = 0
        expected = [[]]
        self.assertEqual(combine(n, k), expected)

    def test_4c2(self):
        n = 4
        k = 2
        expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        self.assertEqual(combine(n, k), expected)

    def test_1c1(self):
        n = 1
        k = 1
        expected = [[1]]
        self.assertEqual(combine(n, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
