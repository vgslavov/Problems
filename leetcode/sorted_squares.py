#!/usr/bin/env python3

import sys
import unittest

# number: 977
# title: Squares of a Sorted Array
# url: https://leetcode.com/problems/squares-of-a-sorted-array/
# section: assessments
# difficulty: easy
# tags: array, two pointers, sorting, meta

# constraints
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

# solution: sort
# complexity
# run-time: O(n log n)
# space: O(1)
def sorted_squares(nums):
    for i in range(len(nums)):
        nums[i] = pow(nums[i], 2)

    nums.sort()

    return nums

# binary search: with dupes
# complexity: O(log n)
# space: O(1)
# TODO: fix dupes issue
def find_min_idx(self, nums):
    if len(nums) == 1:
        return 0
    elif len(nums) == 2:
        return min(range(len(nums)), key=nums.__getitem__)

    left = 0
    right = len(nums)-1

    while left < right:
        mid = left + (right-left)//2
        print(f"left:{left},mid:{mid},right:{right}")

        if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
            return mid
        elif nums[mid-1] >= nums[mid] and nums[mid] >= nums[mid+1]:
            left = mid+1
        else:
            right = mid

    return right

# solution: min() + merge
# complexity
# run-time: O(n)
# space: O(n)
def sorted_squares2(nums):
    if not nums:
        return nums

    has_neg = False
    if nums[0] < 0:
        has_neg = True

    # square: O(n)
    for i in range(len(nums)):
        nums[i] = pow(nums[i], 2)

    print(f"squared:{nums}")

    # there were no negative numbers
    if not has_neg:
        return nums

    # find min idx: (log n)
    #min_idx = self.find_min_idx(nums)
    #if min_idx >= len(nums):
    #    print(f"can't find mid")
    #    return []

    # find min index: O(n)
    min_idx = min(range(len(nums)), key=nums.__getitem__)
    print(f"min_idx:{min_idx}")

    # split array in 2 & reverse 1st: O(n)
    nums1 = list(reversed(nums[:min_idx]))
    nums2 = nums[min_idx:]

    print(f"nums1:{nums1},nums2:{nums2}")

    # merge 2 arrays
    i = j = 0
    ans = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            ans.append(nums1[i])
            i += 1
        else:
            ans.append(nums2[j])
            j += 1

    if i < len(nums1):
        ans.extend(nums1[i:])
    elif j < len(nums2):
        ans.extend(nums2[j:])

    return ans

# solution: two pointers
# complexity
# run-time: O(n)
# space: O(n)
def sorted_squares3(nums):
    left = 0
    right = len(nums)-1
    ans = []

    while left <= right:
        # read positive & negative numbers independently
        # sort descending
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1

        ans.append(pow(square, 2))

    return list(reversed(ans))

class TestSortedSquares(unittest.TestCase):
    def test_empty(self):
        nums = []
        self.assertFalse(sorted_squares(nums))
        self.assertFalse(sorted_squares2(nums))

    def test_1_1(self):
        nums = [-4,-1,0,3,10]
        expected = [0,1,9,16,100]
        self.assertEqual(sorted_squares(nums), expected)

    def test_1_2(self):
        nums = [-4,-1,0,3,10]
        expected = [0,1,9,16,100]
        self.assertEqual(sorted_squares2(nums), expected)

    def test_1_3(self):
        nums = [-4,-1,0,3,10]
        expected = [0,1,9,16,100]
        self.assertEqual(sorted_squares3(nums), expected)

    def test_2_1(self):
        nums = [-7,-3,2,3,11]
        expected = [4,9,9,49,121]
        self.assertEqual(sorted_squares(nums), expected)

    def test_2_2(self):
        nums = [-7,-3,2,3,11]
        expected = [4,9,9,49,121]
        self.assertEqual(sorted_squares2(nums), expected)

    def test_2_3(self):
        nums = [-7,-3,2,3,11]
        expected = [4,9,9,49,121]
        self.assertEqual(sorted_squares3(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
