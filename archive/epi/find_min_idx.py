#!/usr/bin/env python

import unittest

# find indices of 2 smallest elements (first 2 if dups)
# time: O(n)
def find_min_idx_2(nums):

    if not nums:
        return None, None

    if len(nums) == 1:
        return 0, None

    if min(nums[0], nums[1]) == nums[0]:
        min_idx1 = 0
        min_idx2 = 1
    else:
        min_idx1 = 1
        min_idx2 = 0

    for i in range(2, len(nums)):
        if nums[i] < nums[min_idx1]:
            min_idx2 = min_idx1
            min_idx1 = i
        elif nums[i] < nums[min_idx2]:
            min_idx2 = i

    return min_idx1, min_idx2

class TestFindMinIdx2(unittest.TestCase):

    def test_dups(self):
        nums = [15, 15, 15, 90, 30]
        self.assertEqual(find_min_idx_2(nums), (0, 1))

    def test_dups2(self):
        nums = [1, 1, 1, 1, 1, 1]
        self.assertEqual(find_min_idx_2(nums), (0, 1))

    def test_gt2(self):
        nums = [20, 15, 24, 1, 4, 90]
        self.assertEqual(find_min_idx_2(nums), (3, 4))

    def test_two(self):
        nums = [20, 15]
        self.assertEqual(find_min_idx_2(nums), (1, 0))

    def test_one(self):
        nums = [15]
        self.assertEqual(find_min_idx_2(nums), (0, None))

    def test_empty(self):
        nums = []
        self.assertEqual(find_min_idx_2(nums), (None, None))

    def test_none(self):
        self.assertEqual(find_min_idx_2(None), (None, None))

if __name__ == '__main__':
    unittest.main()
