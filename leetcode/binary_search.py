#!/usr/bin/env python3

from bisect import bisect_left
import sys
import unittest

# number: 704
# title: Binary Search
# url: https://leetcode.com/problems/binary-search/
# difficulty: easy
# tags: array, binary search, top 150, grind 75

# constraints:
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.

# solution: bisect_left
# time: O(log n)
# space: O(1)
def search(nums: list[int], target: int) -> int:
    i = bisect_left(nums, target)
    if i < len(nums) and nums[i] == target:
        return i

    return -1

# solution: manual
# time: O(log n)
# space: O(1)
def search2(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1

    if left < len(nums) and nums[left] == target:
        return left

    return -1

class TestBinarySearch(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([-1,0,3,5,9,12], 9), 4)
        self.assertEqual(search([-1,0,3,5,9,12], 2), -1)
        self.assertEqual(search([5], 5), 0)
        self.assertEqual(search([1], 0), -1)

    def test_search2(self):
        self.assertEqual(search2([-1,0,3,5,9,12], 9), 4)
        self.assertEqual(search2([-1,0,3,5,9,12], 2), -1)
        self.assertEqual(search2([5], 5), 0)
        self.assertEqual(search2([1], 0), -1)

if __name__ == "__main__":
    sys.exit(unittest.main())