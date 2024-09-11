#!/usr/bin/env python3

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
def search_range(nums, target):
    ans = [-1,-1]

    # TODO: refactor
    if not nums:
        return ans
    elif len(nums) == 1:
        if nums[0] == target:
            return [0,0]
        else:
            return ans
    elif len(nums) == 2:
        if nums[0] == target:
            ans[0] = 0
        elif nums[1] == target:
            ans[0] = 1

        if nums[1] == target:
            ans[1] = 1
        elif nums[0] == target:
            ans[1] = 0

        return ans

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right-left) // 2
        print(f"left:{left},mid:{mid},right:{right}")

        if nums[mid] == target:
            if nums[mid-1] < target:
                ans[0] = mid
                left = mid+1
            elif nums[mid+1] > target:
                ans[1] = mid
                right = mid-1
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    # TODO: refactor
    if ans[0] == -1 and nums[left] == target:
        ans[0] = left
    if ans[1] == -1 and nums[right] == target:
        ans[1] = right

    return ans

class TestSearchRange(unittest.TestCase):
    def test_empty(self):
        nums = []
        target = 0
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)

    def test1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        expected = [3,4]
        self.assertEqual(search_range(nums, target), expected)

    def test2(self):
        nums = [5,7,7,8,8,10]
        target = 6
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)

    def test3(self):
        nums = [5,7,7,8,8,10]
        target = 6
        expected = [-1,-1]
        self.assertEqual(search_range(nums, target), expected)

    def test4(self):
        nums = [1]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)

    def test5(self):
        nums = [2,2]
        target = 2
        expected = [0,1]
        self.assertEqual(search_range(nums, target), expected)

    def test6(self):
        nums = [1,3]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)

    def test7(self):
        nums = [1,2,3]
        target = 1
        expected = [0,0]
        self.assertEqual(search_range(nums, target), expected)

    # TODO: fix
    def test8(self):
        nums = [1,2,2]
        target = 2
        expected = [0,1]
        self.assertEqual(search_range(nums, target), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
