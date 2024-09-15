#!/usr/bin/env python3

import sys
import unittest

# number: 153
# section: binary search
# difficulty: medium
# tags: array, binary search, top 150

# constraints
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# complexity
# run-time: O(log n)
# space: O(1)
def find_min(nums):
    if not nums:
        return None
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return min(nums)

    left = 0
    right = len(nums)-1

    # no =
    while left < right:
        mid = left + (right-left) // 2

        if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
            return nums[mid]
        elif nums[mid] > nums[-1]:
            left = mid+1
        else:
            right = mid-1

    return nums[left]

class TestFindMin(unittest.TestCase):
    def test_empty(self):
        nums = []
        self.assertFalse(find_min(nums))

    def test1(self):
        nums = [3,4,5,1,2]
        expected = 1
        self.assertEqual(find_min(nums), expected)

    def test2(self):
        nums = [4,5,6,7,0,1,2]
        expected = 0
        self.assertEqual(find_min(nums), expected)

    def test3(self):
        nums = [11,13,15,17]
        expected = 11
        self.assertEqual(find_min(nums), expected)

    def test4(self):
        nums = [2,1]
        expected = 1
        self.assertEqual(find_min(nums), expected)

    def test5(self):
        nums = [2,3,1]
        expected = 1
        self.assertEqual(find_min(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
