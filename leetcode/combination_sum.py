#!/usr/bin/env python3

import sys
import unittest

# number: 39
# title: Combination Sum
# url: https://leetcode.com/problems/combination-sum/
# difficulty: medium
# tags: array, backtracking, neetcode 150, grind 75

# constraints
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# all elements of candidates are distinct.
# 1 <= target <= 40

# solution: Neetcode backtracking using dfs
# complexity:
# run-time: O(n^(t/min(candidates)))
# where n is number of candidates, t is target, m is minimum value in candidates
# space: O(t/min(candidates))
# TODO: understand better
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    def dfs(i, total, cur):
        # base cases
        if total == target:
            ans.append(cur.copy())
            return
        elif total > target or i >= len(candidates):
            return

        # go left: same number, more of it
        cur.append(candidates[i])
        dfs(i, total+candidates[i], cur)

        # go right: next number
        cur.pop()
        dfs(i+1, total, cur)

    ans = []
    dfs(0, 0, [])
    return ans

# solution: backtracking using dfs+sort, template
# complexity:
# run-time: O(n^(t/min(candidates)))
# where n is number of candidates, t is target, m is minimum value in candidates
# space: O(t/min(candidates))
def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    def dfs(i, total, cur):
        # base cases
        if total == target:
            ans.append(cur.copy())
            return
        
        for j in range(i, len(candidates)):
            # optimization: sorted
            if total + candidates[j] > target:
                return

            cur.append(candidates[j])
            dfs(j, total+candidates[j], cur)
            cur.pop()

    candidates.sort()
    ans = []
    dfs(0, 0, [])
    return ans

class TestCombinationSum(unittest.TestCase):
    def test_example1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[7], [2, 2, 3]]
        self.assertCountEqual(combination_sum(candidates, target), expected)
        self.assertCountEqual(combination_sum2(candidates, target), expected)

    def test_example2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertCountEqual(combination_sum(candidates, target), expected)
        self.assertCountEqual(combination_sum2(candidates, target), expected)

    def test_example3(self):
        candidates = [2]
        target = 1
        expected = []
        self.assertCountEqual(combination_sum(candidates, target), expected)
        self.assertCountEqual(combination_sum2(candidates, target), expected)

    def test_empty_candidates(self):
        candidates = []
        target = 7
        expected = []
        self.assertCountEqual(combination_sum(candidates, target), expected)
        self.assertCountEqual(combination_sum2(candidates, target), expected)

    def test_no_combination(self):
        candidates = [5, 10]
        target = 3
        expected = []
        self.assertCountEqual(combination_sum(candidates, target), expected)
        self.assertCountEqual(combination_sum2(candidates, target), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())