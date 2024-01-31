#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5

# slicing
# TODO: fix when k > len(nums)
def rotate_array1(nums, k):
    return nums[-k:] + nums[:-k]

# using deque rotate
def rotate_array2(nums, k):
    q = deque(nums)
    q.rotate(k)

    return list(q)

# using deque manual
def rotate_array3(nums, k):
    q = deque(nums)

    if not nums:
        return []

    while k:
        q.appendleft(q.pop())
        k -= 1

    return list(q)

# TODO: extra: in-place w/ O(1) space
def rotate_array4(nums, k):
    pass

class TestRotateArray(unittest.TestCase):

    def test_empty(self):
        nums = []
        k = 5
        expected = nums
        self.assertEqual(rotate_array1(nums, k), expected)
        self.assertEqual(rotate_array2(nums, k), expected)
        self.assertEqual(rotate_array3(nums, k), expected)

    def test_no_rotate(self):
        nums = [1, 2, 3, 4]
        k = 0
        expected = nums
        self.assertEqual(rotate_array1(nums, k), expected)
        self.assertEqual(rotate_array2(nums, k), expected)
        self.assertEqual(rotate_array3(nums, k), expected)

    def test_rotate1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        expected = [5,6,7,1,2,3,4]
        self.assertEqual(rotate_array1(nums, k), expected)
        self.assertEqual(rotate_array2(nums, k), expected)
        self.assertEqual(rotate_array3(nums, k), expected)

    def test_rotate2(self):
        nums = [-1,-100,3,99]
        k = 2
        expected = [3,99,-1,-100]
        self.assertEqual(rotate_array1(nums, k), expected)
        self.assertEqual(rotate_array2(nums, k), expected)
        self.assertEqual(rotate_array3(nums, k), expected)

    def test_rotate3(self):
        nums = [1,2]
        k = 3
        expected = [2,1]
        # TODO: fix when k > len(nums)
        #self.assertEqual(rotate_array1(nums, k), expected)
        self.assertEqual(rotate_array2(nums, k), expected)
        self.assertEqual(rotate_array3(nums, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
