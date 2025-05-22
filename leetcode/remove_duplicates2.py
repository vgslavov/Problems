#!/usr/bin/env python3

import math
import sys
import unittest

# number: 80
# title: Remove Duplicates from Sorted Array II
# url: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# section: array/string
# difficulty: medium
# tags: array, two pointers, top 150

# constraints
# remove in-place w/ O(1) memory!
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order
# stable
# unique elements appear at most twice

# solution: sort
# complexity
# run-time: O(n*log n)
# space: O(1)
def remove_duplicates2(nums):
    dupes = 0

    for i in range(len(nums) - 2):
        # TODO: make more generic?
        if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
            nums[i] = math.inf
            dupes += 1

    nums.sort()
    return len(nums) - dupes, nums

# TODO: O(n) using two pointers

class TestRemoveDuplicates2(unittest.TestCase):

    def test_empty(self):
        nums = []
        k = len(nums)
        self.assertEqual(remove_duplicates2(nums), (k, nums))

    def test_no_dupes(self):
        nums = [1,2,3]
        k =  len(nums)
        self.assertEqual(remove_duplicates2(nums), (k, nums))

    def test_dupes1(self):
        nums = [1,1,1,2,2,3]
        expected = [1,1,2,2,3]
        k = len(expected)
        self.assertEqual(remove_duplicates2(nums)[1][:k], expected)

    def test_dupes2(self):
        nums = [0,0,1,1,1,1,2,3,3]
        expected = [0,0,1,1,2,3,3]
        k = len(expected)
        self.assertEqual(remove_duplicates2(nums)[1][:k], expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
