#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: backtracking, dfs
# leetcode number: 78

# solution: backtracking using dfs
# complexity:
# run-time: O(n*2^n), for each element in n, 2^n subsets
# space: O(n)
def subsets(nums: list[int]) -> list[list[int]]:
    def dfs(i, cur):
        if i >= len(nums):
            ans.append(cur[:])
            return

        # left subtree: decision to include nums[i]
        cur.append(nums[i])
        dfs(i+1, cur)

        # right subtree: decision NOT to include nums[i]
        cur.pop()
        dfs(i+1, cur)

    ans = []
    dfs(0, [])

    # for unit tests
    ans.sort()
    return ans

class TestSubsets(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = [[]]
        self.assertEqual(subsets(nums), expected)

    def test_single_element(self):
        nums = [1]
        expected = [[], [1]]
        self.assertEqual(subsets(nums), expected)


    def test_two_elements(self):
        nums = [1, 2]
        expected = [[], [1], [1, 2], [2]]
        self.assertEqual(subsets(nums), expected)

    def test_three_elements(self):
        nums = [1, 2, 3]
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertEqual(subsets(nums), expected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    res = subsets(nums)
    for row in sorted(map(sorted, res)):
        print(" ".join(map(str, row)))