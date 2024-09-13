#!/usr/bin/env python3

import bisect
import sys
import unittest

# number: 34
# section: binary search
# difficulty: medium
# tags: array, binary search, top 150

# constraints
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9

# complexity
# run-time: O(log n)
# space: O(1)
def binary_search(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right-left) // 2
        #print(f"left:{left},mid:{mid},right:{right}")

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return left

# solution: binary search + two pointers
# complexity
# run-time: O(log n)
# space: O(1)
def search_range(nums, target):
    idx = binary_search(nums, target)
    if idx < 0 or idx >= len(nums) or nums[idx] != target:
        return [-1,-1]

    #print(f"idx:{idx},val:{nums[idx]}")
    left = right = idx
    while 0 < left and right < len(nums)-1:
        if nums[left-1] == target:
            left -= 1

        if nums[right+1] == target:
            right += 1
        else:
            break

    while 0 < left:
        if nums[left-1] != target:
            break

        left -= 1

    while right < len(nums)-1:
        if nums[right+1] != target:
            break

        right += 1

    return [left,right]

# solution: Pythonic bisect + two pointers
# complexity
# run-time: O(log n)
# space: O(1)
def search_range2(nums, target):
    idx = bisect.bisect_left(nums, target)
    if idx < 0 or idx >= len(nums) or nums[idx] != target:
        return [-1,-1]

    #print(f"idx:{idx},val:{nums[idx]}")
    left = right = idx
    while 0 < left and right < len(nums)-1:
        if nums[left-1] == target:
            left -= 1

        if nums[right+1] == target:
            right += 1
        else:
            break

    while 0 < left:
        if nums[left-1] != target:
            break

        left -= 1

    while right < len(nums)-1:
        if nums[right+1] != target:
            break

        right += 1

    return [left,right]

class TestSearchRange(unittest.TestCase):
    def test_empty(self):
        nums = []
        target = 0
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        expected = [3,4]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test2(self):
        nums = [5,7,7,8,8,10]
        target = 6
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test3(self):
        nums = [5,7,7,8,8,10]
        target = 6
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test4(self):
        nums = [1]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test5(self):
        nums = [2,2]
        target = 2
        expected = [0,1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test6(self):
        nums = [1,3]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test7(self):
        nums = [1,2,3]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test8(self):
        nums = [1,2,2]
        target = 2
        expected = [1,2]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test9(self):
        nums = [3,3,3]
        target = 3
        expected = [0,2]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

    def test10(self):
        nums = [2,2]
        target = 3
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
