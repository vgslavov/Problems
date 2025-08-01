#!/usr/bin/env python3

import itertools
import sys
import unittest

# number: 46
# title: Permutations
# url: https://leetcode.com/problems/permutations/
# section: backtracking
# difficulty: medium
# tags: array, backtracking, top 150, meta, grind 75

# constraints
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

# solution: itertools
# complexity
# run-time: O(n*n!)?
# space: O(n*n!)?
def permute(nums: list[int]) -> list[list[int]]:
    return [list(v) for v in itertools.permutations(nums)]

# solution: LeetCode backtracking
# explanation:
# * dfs traversal of an imaginary tree
# * leaves of the tree are permutations
# * each node is a partial permutation
# * each level of the tree is a number in the permutation
# * each node has n children, where n is the number of elements in the input
# * each node has n-1 elements left to choose from
# complexity
# run-time: O(n^2*n!)
# space: O(n)
# TODO: understand better
def permute2(nums: list[int]) -> list[list[int]]:
    def backtrack(curr):
        # base case: permutation as long as input
        if len(curr) == len(nums):
            # append a *copy* of the current permutation to the answer
            ans.append(curr[:])
            return

        # iterate through input on each level of the tree
        for n in nums:
            # TODO: put in dict to optimize: O(n*n!)
            if n not in curr:
                curr.append(n)
                backtrack(curr)
                curr.pop()

    # root of the backtracking tree is an empty list
    # nodes are the leaves of the tree
    ans = []
    backtrack([])

    return ans

class TestPermute(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = [[]]
        self.assertEqual(permute(nums), expected)
        self.assertEqual(permute2(nums), expected)

    def test1(self):
        nums = [1,2,3]
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(permute(nums), expected)
        self.assertEqual(permute2(nums), expected)

    def test2(self):
        nums = [0,1]
        expected = [[0,1],[1,0]]
        self.assertEqual(permute(nums), expected)
        self.assertEqual(permute2(nums), expected)

    def test3(self):
        nums = [1]
        expected = [[1]]
        self.assertEqual(permute(nums), expected)
        self.assertEqual(permute2(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
