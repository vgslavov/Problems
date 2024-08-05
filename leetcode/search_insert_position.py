#!/usr/bin/env python3

import sys
import unittest

# number: 35
# section: binary search
# difficulty: easy
# tags: array, binary search, top 150

# constraints
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4

# complexity
# run-time: O(log n)
# space: O(1)
def search_insert(nums, target):
    start = 0
    end = len(nums) - 1

    # outside given range
    if not nums or target <= nums[start]:
        return 0
    elif target > nums[end]:
        return len(nums)

    # inclusive!
    while start <= end:
        # don't overflow
        mid = start + (end - start) // 2
        print('start:{}, mid:{}, end:{}'.format(start, mid, end))

        # found
        if target == nums[mid]:
            return mid
        # go right
        elif nums[mid] < target:
            start = mid + 1
        # go left
        else:
            end = mid - 1

    # why?
    return start

class TestSearchInsert(unittest.TestCase):
    def test_empty(self):
        nums = []
        target = 0
        expected = 0
        self.assertEqual(search_insert(nums, target), expected)

    def test_found_even(self):
        nums = [1,3,5,6]
        target = 5
        expected = 2
        self.assertEqual(search_insert(nums, target), expected)

    def test_notfound_inside(self):
        nums = [1,3,5,6]
        target = 2
        expected = 1
        self.assertEqual(search_insert(nums, target), expected)

    def test_notfound_outside(self):
        nums = [1,3,5,6]
        target = 7
        expected = 4
        self.assertEqual(search_insert(nums, target), expected)

    def test_found_single(self):
        nums = [1]
        target = 1
        expected = 0
        self.assertEqual(search_insert(nums, target), expected)

    def test_notfound_2(self):
        nums = [1,3]
        target = 2
        expected = 1
        self.assertEqual(search_insert(nums, target), expected)

    def test_notfound_odd(self):
        nums = [1,2,4,6,7]
        target = 3
        expected = 2
        self.assertEqual(search_insert(nums, target), expected)

    def test_found_even2(self):
        nums = [3,4,5,6,7,8]
        target = 6
        expected = 3
        self.assertEqual(search_insert(nums, target), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
