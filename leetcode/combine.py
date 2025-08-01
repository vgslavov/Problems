#!/usr/bin/env python3

import itertools
import sys
import unittest

# number: 77
# title: Combinations
# url: https://leetcode.com/problems/combinations/
# section: backtracking
# difficulty: medium
# tags: backtracking, top 150

# constraints
# 1 <= n <= 20
# 1 <= k <= n

# solution: itertools
# complexity
# run-time: O(n choose k)
# space: O(k)
def combine(n: int, k: int) -> list[list[int]]:
    # range(start, stop): [start, stop)!
    return [list(v) for v in itertools.combinations(list(range(1, n+1)), k)]

# solution: LeetCode backtracking
# complexity
# run-time: O(n choose k) ~ O(n!/(k!(n-k)!))
# space: O(k)
# TODO: understand better
def combine2(n: int, k: int) -> list[list[int]]:
    def backtrack(curr, i):
        # base
        if len(curr) == k:
            # append a *copy* of the current combination to the answer
            ans.append(curr[:])
            return

        # iterate through input on each level of the tree 
        # loop over: [i, n] to avoid duplicates
        # compare to permutations loop:
        # for n in nums:
        for num in range(i, n+1):
            curr.append(num)
            backtrack(curr, num+1)
            curr.pop()

    ans = []
    # root of the backtracking tree is an empty list
    backtrack([], 1)
    return ans

class TestCombine(unittest.TestCase):
    def test_empty(self):
        n = 0
        k = 0
        expected = [[]]
        self.assertEqual(combine(n, k), expected)
        self.assertEqual(combine2(n, k), expected)

    def test_4c2(self):
        n = 4
        k = 2
        expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        self.assertEqual(combine(n, k), expected)
        self.assertEqual(combine2(n, k), expected)

    def test_1c1(self):
        n = 1
        k = 1
        expected = [[1]]
        self.assertEqual(combine(n, k), expected)
        self.assertEqual(combine2(n, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
