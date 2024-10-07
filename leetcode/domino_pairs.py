#!/usr/bin/env python3

from collections import defaultdict
import math
import sys
import unittest

# number: 1128
# section: assessments
# difficulty: easy
# tags: amazon

# constraints
# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9

# solution: dict + comb
# complexity
# run-time: O(n)
# space: O(n)
def domino_pairs(dominoes) -> int:
    ans = 0
    counts = defaultdict(int)

    for i in range(len(dominoes)):
        counts[tuple(sorted(dominoes[i]))] += 1

    return sum([math.comb(v,2) for v in counts.values()])

class TestDominoPairs(unittest.TestCase):
    def test_empty(self):
        dominoes = []
        expected = 0
        self.assertEqual(domino_pairs(dominoes), expected)

    def test1(self):
        dominoes = [[1,2],[2,1],[3,4],[5,6]]
        expected = 1
        self.assertEqual(domino_pairs(dominoes), expected)

    def test2(self):
        dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
        expected = 3
        self.assertEqual(domino_pairs(dominoes), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
