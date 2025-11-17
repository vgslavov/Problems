#! /usr/bin/env python3

import argparse
import sys
import unittest

# tags: backtracking, dfs
# leetcode number: 39

# solution: backtracking using dfs
# complexity:
# run-time: O(n^(t/min(candidates)))
# where n is number of candidates, t is target value
# space: O(t/min(candidates))
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    def dfs(i, total, cur):
        # base case
        if total == target:
            ans.append(cur.copy())
            return
        elif total > target or i >= len(candidates):
            return

        # recursion
        for j in range(i, len(candidates)):
            if total > target:
                return
                
            cur.append(candidates[j])
            dfs(j, total+candidates[j], cur)
            cur.pop()

    ans = []
    dfs(0, 0, [])
    return ans

# solution: Algomonster backtracking using dfs+sort
# complexity:
# run-time: O(n^(t/min(candidates)))
# where n is number of candidates, t is target value
# space: O(t/min(candidates))
def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    def dfs(i, remaining, cur):
        if remaining == 0:
            ans.append(cur.copy())
            return

        for j in range(i, len(candidates)):
            if remaining - candidates[j] < 0:
                continue

            cur.append(candidates[j])
            dfs(j, remaining-candidates[j], cur)
            cur.pop()

    ans = []
    candidates.sort()
    dfs(0, target, [])
    return ans

class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.funcs = [combination_sum, combination_sum2]

    def assertCombos(self, func, candidates, target, expected):
        # pass a copy to avoid in-place mutation by implementations
        got = func(list(candidates), target)
        self.assertEqual(
            sorted(map(tuple, map(sorted, got))),
            sorted(map(tuple, map(sorted, expected)))
        )
    
    def test_examples(self):
        cases = [
            ([2, 3, 6, 7], 7, [[7], [2, 2, 3]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2], 1, []),
        ]
        for func in self.funcs:
            for candidates, target, expected in cases:
                with self.subTest(func=func.__name__, candidates=candidates, target=target):
                    self.assertCombos(func, candidates, target, expected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    candidates = [int(x) for x in input().split()]
    target = int(input())
    res = combination_sum(candidates, target)
    for row in sorted(map(sorted, res)):
        print(" ".join(map(str, row)))