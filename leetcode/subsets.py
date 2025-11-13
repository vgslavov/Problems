#!/usr/bin/env python3

import sys
import unittest

# number: 78
# title: Subsets
# url: https://leetcode.com/problems/subsets/
# section: backtracking
# difficulty: medium
# tags: backtracking, grind 75, neetcode 150

# constraints
# 0 <= nums.length <= 10
# -10 <= nums[i] <= 10

# solution: LeetCode backtracking
# complexity
# run-time: O(n*2^n)
# space: O(n)
# TODO: understand better
def subsets(nums: list[int]) -> list[list[int]]:
    def backtrack(curr, i):
        # subsets have variable length (unlike permutations)
        # make sure i doesn't get past end
        if i > len(nums):
            return

        for j in range(i, len(nums)):
            curr.append(nums[j])
            # recursive calls should not create duplicates
            backtrack(curr, j+1)
            curr.pop()

        ans.append(curr[:])

    ans = []
    # i: where to start iterating from
    # (to ensure no duplicate subsets)
    # 0: first call starts at first element of nums
    backtrack([], 0)

    # for unit tests
    ans.sort()
    return ans

# solution: Neetcode backtracking
# complexity:
# run-time: O(n*n^2)
# space: O(n)
def subsets2(nums: list[int]) -> list[list[int]]:
    def dfs(i):
        if i >= len(nums):
            ans.append(subset[:])
            return

        # left subtree: decision to include nums[i]
        subset.append(nums[i])
        # go to next element
        dfs(i+1)

        # right subtree: decision NOT to include nums[i]
        subset.pop()
        # go to next element
        dfs(i+1)

    ans = []
    subset = []
    dfs(0)
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
    sys.exit(unittest.main())