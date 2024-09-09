#!/usr/bin/env python3

import sys
import unittest

# number: 162
# section: binary search
# difficulty: medium
# tags: array, binary search, top 150

# constraints
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.

# solution: binary search
# complexity
# run-time: O(log n)
# space: O(1)
def find_peak(nums):
    if not nums:
        return None
    elif len(nums) == 1:
        return 0
    elif len(nums) == 2:
        # returns index of max num
        return max(range(len(nums)), key=nums.__getitem__)

    left = 0
    right = len(nums)-1

    while left < right:
        mid = left + (right-left) // 2
        print(f'left:{left},mid:{mid},right:{right}')

        # peak
        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        # ascending
        elif nums[mid-1] > nums[mid] and nums[mid] > nums[mid+1]:
            if mid-1 < 0:
                break
            right = mid-1
        # descending
        else:
            if mid+1 >= len(nums):
                break
            left = mid+1

    print(f'left:{left},mid:{mid},right:{right}')

    # cmp to 1st & last
    if nums[0] > nums[right] and nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[right] and nums[-1] > nums[-2]:
        return len(nums)-1

    return right

class TestFindPeak(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = None
        self.assertEqual(find_peak(nums), expected)

    def test1(self):
        nums = [1,2,3,1]
        expected = 2
        self.assertEqual(find_peak(nums), expected)

    def test2(self):
        nums = [1,2,1,3,5,6,4]
        expected = 5
        self.assertEqual(find_peak(nums), expected)

    def test3(self):
        nums = [1]
        expected = 0
        self.assertEqual(find_peak(nums), expected)

    def test4(self):
        nums = [1,2]
        expected = 1
        self.assertEqual(find_peak(nums), expected)

    def test5(self):
        nums = [1,2,3]
        expected = 2
        self.assertEqual(find_peak(nums), expected)

    def test6(self):
        nums = [1,2,1,2,1]
        expected = 3
        self.assertEqual(find_peak(nums), expected)

    def test7(self):
        nums = [1,2,3,4]
        expected = 3
        self.assertEqual(find_peak(nums), expected)

    def test8(self):
        nums = [5,4,3,4,5]
        expected = 4
        self.assertEqual(find_peak(nums), expected)

    def test9(self):
        nums = [4, 3, 2, 1, 4]
        expected = 0
        self.assertEqual(find_peak(nums), expected)

    def test10(self):
        nums = [3,4,5,6,1,2]
        expected = 5
        self.assertEqual(find_peak(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
