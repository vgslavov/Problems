#!/usr/bin/env python3

from functools import cache
import sys
import unittest

# number: 55
# title: Jump Game
# url: https://leetcode.com/problems/jump-game/
# section: array / string
# difficulty: medium
# tags: array, dp, greedy, top 150

# constraints:
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5

def can_jump_i(nums, i):
    # last one is always Good
    if i == len(nums)-1:
        return True

    # can't jump farther than end of array
    farthest = min(i + nums[i], len(nums)-1)

    # try all b/w next and farthest: range is [)
    for next_jump in range(i+1, farthest+1):
        if can_jump_i(nums, next_jump):
            return True

    # nothing was Good
    return False

# non-solution: LeetCode backtracking (recursion w/o memoization)
# complexity:
# run-time: O(2^n)
# space: O(n)
def can_jump(nums):
    return can_jump_i(nums, 0)

# solution: LeetCode top-down 1D recursive DP w/ functools for memoization
# complexity:
# run-time: O(n^2)
# space: O(n)
def can_jump2(nums) -> bool:
    @cache
    def dp(i):
        # last one is always Good
        if i == len(nums)-1:
            return True

        # can't jump farther than end of array
        farthest = min(i + nums[i], len(nums)-1)

        # try all b/w next and farthest: range is [)
        for next_jump in range(i+1, farthest+1):
            if dp(next_jump):
                return True

        # nothing was Good
        return False

    return dp(0)

# solution: LeetCode top-down recursive 1D DP w/ list for memoization
# complexity:
# run-time: O(n^2)
# space: O(n)
def can_jump3(nums) -> bool:
    def dp(i):          
        # check cache
        if memo[i] != -1:
            return memo[i] == 1

        # can't jump farther than end of array
        farthest = min(i + nums[i], len(nums)-1)

        # try all b/w next and farthest: range is [)
        for next_jump in range(i+1, farthest+1):
            if dp(next_jump):
                memo[i] = 1
                return True

        # nothing was Good
        memo[i] = 0
        return False

    # don't use a dict, use a list!
    memo = [-1] * len(nums)
    # last position always Good
    memo[-1] = 1
    return dp(0)

# solution: LeetCode bottom-up iterative 1D DP
# complexity:
# run-time: O(n^2)
# space: O(n)
def can_jump4(nums) -> bool:
    # -1: unknown
    # 0: bad (unused)
    # 1: good
    memo = [-1] * len(nums)
    # last position always Good
    memo[-1] = 1

    # start from right, but skip last
    for i in range(len(nums)-2,-1,-1):
        # can't jump farther than end of array
        farthest = min(i + nums[i], len(nums)-1)

        # try all b/w next and farthest: range is [)
        for j in range(i+1, farthest+1):
            # we can reach j from i
            if memo[j] == 1:
                memo[i] = 1
                # optimization: no need to check farther
                break

    # is first index Good (i.e. can reach next from it?)
    return memo[0] == 1

# TODO: solve using greedy
class TestCanJump(unittest.TestCase):
    def test_can_jump(self):
        self.assertEqual(can_jump([2,3,1,1,4]), True)
        self.assertEqual(can_jump2([2,3,1,1,4]), True)
        self.assertEqual(can_jump3([2,3,1,1,4]), True)
        self.assertEqual(can_jump4([2,3,1,1,4]), True)

        self.assertEqual(can_jump([3,2,1,0,4]), False)
        self.assertEqual(can_jump2([3,2,1,0,4]), False)
        self.assertEqual(can_jump3([3,2,1,0,4]), False)
        self.assertEqual(can_jump4([3,2,1,0,4]), False)

        self.assertEqual(can_jump([0]), True)
        self.assertEqual(can_jump2([0]), True)
        self.assertEqual(can_jump3([0]), True)
        self.assertEqual(can_jump4([0]), True)

        self.assertEqual(can_jump([2,0]), True)
        self.assertEqual(can_jump2([2,0]), True)
        self.assertEqual(can_jump3([2,0]), True)
        self.assertEqual(can_jump4([2,0]), True)

        self.assertEqual(can_jump([0,0]), False)
        self.assertEqual(can_jump2([0,0]), False)
        self.assertEqual(can_jump3([0,0]), False)
        self.assertEqual(can_jump4([0,0]), False)

        self.assertEqual(can_jump([1,0]), True)
        self.assertEqual(can_jump2([1,0]), True)
        self.assertEqual(can_jump3([1,0]), True)
        self.assertEqual(can_jump4([1,0]), True)

        self.assertEqual(can_jump([1,2]), True)
        self.assertEqual(can_jump2([1,2]), True)
        self.assertEqual(can_jump3([1,2]), True)
        self.assertEqual(can_jump4([1,2]), True)

        self.assertEqual(can_jump([2,1]), True)
        self.assertEqual(can_jump2([2,1]), True)
        self.assertEqual(can_jump3([2,1]), True)
        self.assertEqual(can_jump4([2,1]), True)

if __name__ == "__main__":
    sys.exit(unittest.main())