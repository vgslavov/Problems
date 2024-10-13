#!/usr/bin/env python3

import math
import sys
import unittest

# number: 26
# section: array/string
# difficulty: easy
# tags: array, two pointers, top 150, meta

# constraints
# remove in-place
# nums is sorted in non-decreasing order
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100

# solution: sort
# complexity
# run-time: O(n * log(n))
# space: O(1)
def remove_duplicates(nums):
    dupes = 0

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = math.inf
            dupes += 1

    nums.sort()

    return len(nums) - dupes, nums

# TODO: in O(n)

class TestRemoveDuplicates(unittest.TestCase):
    def test_empty(self):
        nums = []
        k = len(nums)
        self.assertEqual(remove_duplicates(nums), (k, nums))

    def test_no_dupes(self):
        nums = [1, 2, 3]
        k = len(nums)
        self.assertEqual(remove_duplicates(nums), (k, nums))

    def test_dupes1(self):
        nums = [1, 1, 2]
        expected = [1, 2]
        k = len(expected)
        self.assertEqual(remove_duplicates(nums)[1][:k], expected)

    def test_dupes2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected = [0,1,2,3,4]
        k = len(expected)
        self.assertEqual(remove_duplicates(nums)[1][:k], expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
