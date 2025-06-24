#!/usr/bin/env python3

import itertools
import sys
import unittest

# number: 46
# title: Permutations
# url: https://leetcode.com/problems/permutations/
# section: backtracking
# difficulty: medium
# tags: array, backtracking, top 150, meta

# constraints
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

# solution: itertools
# complexity
# run-time: O(n*n!)?
# space: O(n*n!)?
def permute(nums):
    return [list(v) for v in itertools.permutations(nums)]

# TODO: solve manually

class TestPermute(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = [[]]
        self.assertEqual(permute(nums), expected)

    def test1(self):
        nums = [1,2,3]
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(permute(nums), expected)

    def test2(self):
        nums = [0,1]
        expected = [[0,1],[1,0]]
        self.assertEqual(permute(nums), expected)

    def test3(self):
        nums = [1]
        expected = [[1]]
        self.assertEqual(permute(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
