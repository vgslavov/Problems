#!/usr/bin/env python3

import bisect
import sys
import unittest

# number: 33
# title: Search in Rotated Sorted Array
# url: https://leetcode.com/problems/search-in-rotated-sorted-array/
# section: binary search
# difficulty: medium
# tags: array, binary search, top 150, meta, grind 75

# constraints
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4

# complexity
# run-time: O(log n)
# space: O(1)
def find_max(nums):
    if len(nums) == 1:
        return 0
    elif len(nums) == 2:
        # returns index of max num
        return max(range(len(nums)), key=nums.__getitem__)

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right - left) // 2
        #print("left:{}, mid:{}, right:{}".format(left,mid,right))

        if mid >= len(nums)-1:
            break
        # found max num
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        # go right: rotation is there
        # compare to last!
        elif nums[mid] > nums[-1]:
            left = mid+1
        # go left
        else:
            right = mid-1

    return 0

# complexity
# run-time: O(log n)
# space: O(1)
def binary_search(nums, target, left, right):
    if right-left == 1:
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right

    while left <= right:
        mid = left + (right - left) // 2
        #print("left:{}, mid:{}, right:{}".format(left,mid,right))

        # found
        if nums[mid] == target:
            return mid
        # go left
        elif nums[mid] > target:
            right = mid-1
        # go right
        else:
            left = mid+1

    return left

# solution: manual binary search x2
# complexity
# run-time: O(log n)
# space: O(1)
def search_rotate(nums, target):
    if not nums:
        return -1

    end_idx = find_max(nums)
    #print("max_idx:{}".format(max_idx))
    if end_idx == -1:
        print("no end_idx")
        return -1

    left = binary_search(nums, target, 0, end_idx)
    if left < len(nums) and nums[left] == target:
        return left

    right = binary_search(nums, target, end_idx+1, len(nums)-1)
    if right < len(nums) and nums[right] == target:
        return right

    return -1

# solution: manual binary search + Pythonic bisect
# complexity
# run-time: O(log n)
# space: O(1)
def search_rotate2(nums, target):
    if not nums:
        return -1

    end_idx = find_max(nums)
    #print("max_idx:{}".format(max_idx))
    if end_idx == -1:
        print("no end_idx")
        return -1

    left = bisect.bisect_left(nums, target, 0, end_idx)
    if left < len(nums) and nums[left] == target:
        return left

    right = bisect.bisect_left(nums, target, end_idx+1, len(nums)-1)
    if right < len(nums) and nums[right] == target:
        return right

    return -1

class TestSearchRotate(unittest.TestCase):

    def test_empty(self):
        nums = []
        target = -1
        expected = target
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        expected = 4
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        expected = -1
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_3(self):
        nums = [1]
        target = 0
        expected = -1
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_4(self):
        nums = [1]
        target = 1
        expected = 0
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_5(self):
        nums = [1,3]
        target = 0
        expected = -1
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_6(self):
        nums = [1,3,5]
        target = 0
        expected = -1
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_7(self):
        nums = [1,3,5]
        target = 1
        expected = 0
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_8(self):
        nums = [1,3,5]
        target = 5
        expected = 2
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_9(self):
        nums = [5,1,3]
        target = 0
        expected = -1
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_10(self):
        nums = [5,1,2,3,4]
        target = 1
        expected = 1
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_11(self):
        nums = [57,58,59,62,63,66,68,72,73,74,75,76,77,78,80,81,86,95,96,97,98,100,101,102,103,110,119,120,121,123,125,126,127,132,136,144,145,148,149,151,152,160,161,163,166,168,169,170,173,174,175,178,182,188,189,192,193,196,198,199,200,201,202,212,218,219,220,224,225,229,231,232,234,237,238,242,248,249,250,252,253,254,255,257,260,266,268,270,273,276,280,281,283,288,290,291,292,294,295,298,299,4,10,13,15,16,17,18,20,22,25,26,27,30,31,34,38,39,40,47,53,54]
        target = 30
        expected = 113
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)

    def test_12(self):
        nums = [4,5,1,2,3]
        target = 1
        expected = 2
        self.assertEqual(search_rotate(nums, target), expected)
        self.assertEqual(search_rotate2(nums, target), expected)


if __name__ == '__main__':
    sys.exit(unittest.main())
