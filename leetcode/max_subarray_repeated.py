#!/usr/bin/env python3

from functools import cache
import sys
import unittest

# number: 718
# section: citadel
# difficulty: medium
# tags: array, binary search, dp, sliding window, rolling hash, hash function

# constraints
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100

# solution: top-down recursive 2DP using functools, like LCS
# complexity
# run-time:
# space:
# TODO: Fix
def max_subarray_repeated(nums1, nums2) -> int:
    @cache
    def dp(i, j):
        # base case
        if i == len(nums1) or j == len(nums2):
            return 0

        # recurrence relation
        if nums1[i] == nums2[j]:
            return 1 + dp(i+1, j+1)

        return max(dp(i, j+1), dp(i+1, j))

    return dp(0, 0)

# solution: bottom-up iterative 2DP
# complexity
# run-time:
# space:
# TODO: Fix
def max_subarray_repeated2(nums1, nums2) -> int:
    pass

class TestMaxSubarrayRepeated(unittest.TestCase):
    def test_empty(self):
        nums1 = []
        nums2 = []
        expected = 0
        self.assertEqual(max_subarray_repeated(nums1, nums2), expected)

    def test1(self):
        nums1 = [1,2,3,2,1]
        nums2 = [3,2,1,4,7]
        expected = 3
        self.assertEqual(max_subarray_repeated(nums1, nums2), expected)

    def test2(self):
        nums1 = [0,0,0,0,0]
        nums2 = [0,0,0,0,0]
        expected = 5
        self.assertEqual(max_subarray_repeated(nums1, nums2), expected)

    # TODO: fix
    def test3(self):
        nums1 = [0,1,1,1,1]
        nums2 = [1,0,1,0,1]
        expected = 2
        self.assertEqual(max_subarray_repeated(nums1, nums2), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
