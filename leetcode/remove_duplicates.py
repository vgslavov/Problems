#!/usr/bin/env python3

import sys
import unittest

# remove in-place
# nums is sorted in non-decreasing order
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
def remove_duplicates(nums):
    dupes = 0

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            #print("dupe:{} at i:{}".format(nums[i], i))
            nums[i] = 999
            dupes += 1

    nums.sort()

    return len(nums) - dupes, nums

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
