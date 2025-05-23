#!/usr/bin/env python3

import bisect
import sys
import unittest

# number: 34
# title: Find First and Last Position of Element in Sorted Array
# url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# section: binary search
# difficulty: medium
# tags: array, binary search, top 150, meta

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

# solution: manual binary search + two pointers
# complexity
# run-time: O(n) worst, O(log n) average
# space: O(1)
def search_range(nums, target):
    left = binary_search(nums, target)
    if left < 0 or left >= len(nums) or nums[left] != target:
        return [-1,-1]

    right = left
    # go both left & right
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

# complexity
# run-time: O(log n)
# space: O(1)
def binary_search_left(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right-left) // 2
        #print(f"left:{left},mid:{mid},right:{right}")

        if nums[mid] >= target:
            right = mid
        else:
            left = mid+1

    return left

# solution: manual binary search left
# complexity
# run-time: O(n) worst, O(log n) average
# space: O(1)
def search_range2(nums, target):
    left = binary_search_left(nums, target)
    #print(f"left:{left}")
    if left < 0 or left >= len(nums) or nums[left] != target:
        return [-1,-1]

    right = left

    while right < len(nums) and nums[right] == target:
        right += 1

    return [left,right-1]

# solution: Pythonic bisect
# complexity
# run-time: O(n) worst, O(log n) average
# space: O(1)
def search_range3(nums, target):
    left = bisect.bisect_left(nums, target)
    if left < 0 or left >= len(nums) or nums[left] != target:
        return [-1,-1]

    right = left

    while right < len(nums) and nums[right] == target:
        right += 1

    return [left,right-1]

class TestSearchRange(unittest.TestCase):
    def test_empty(self):
        nums = []
        target = 0
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        expected = [3,4]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test2(self):
        nums = [5,7,7,8,8,10]
        target = 6
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test3(self):
        nums = [5,7,7,8,8,10]
        target = 6
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test4(self):
        nums = [1]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test5(self):
        nums = [2,2]
        target = 2
        expected = [0,1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test6(self):
        nums = [1,3]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test7(self):
        nums = [1,2,3]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test8(self):
        nums = [1,2,2]
        target = 2
        expected = [1,2]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test9(self):
        nums = [3,3,3]
        target = 3
        expected = [0,2]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

    def test10(self):
        nums = [2,2]
        target = 3
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)
        self.assertEqual(search_range2(nums, target), expected)
        self.assertEqual(search_range3(nums, target), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
