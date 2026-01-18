#!/usr/bin/env python

from bisect import bisect_left
import unittest

# from bisect doc
# time: O(log n)
def binary_search(nums, k):
    i = bisect_left(nums, k)
    if i != len(nums) and nums[i] == k:
        return True
    return False

# find index of min element in convex-sorted list
# time: O(log n)
def find_min_idx_convex(nums):

    # empty
    if not nums:
        return None

    # not convex
    if len(nums) < 3:
        return None

    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start + end)/2

        #print("start: {0}".format(start))
        #print("mid: {0}".format(mid))
        #print("end: {0}".format(end))

        # found min element
        if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
            return mid
        # decreasing, go right
        # don't add 1 to mid like in bin_search!
        elif nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]:
            start = mid
        # increasing, go left
        # don't add 1 to mid like in bin_search!
        elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
            end = mid
        # not convex
        else:
            return None

    return None

# find if k is in convex-sorted list
# time: O(log n)
def find_k_convex(nums, k):
    min_idx = find_min_idx_convex(nums)

    if not min_idx:
        return False

    if binary_search(nums[:min_idx], k) or binary_search(nums[min_idx:], k):
        return True

    return False

class TestFindKConvex(unittest.TestCase):

    def test_min_idx_two(self):
        nums = [20, 30]
        self.assertIsNone(find_min_idx_convex(nums))

    def test_min_idx_odd(self):
        nums = [30, 20, 10, 5, 10]
        self.assertEqual(find_min_idx_convex(nums), 3)

    def test_min_idx_even(self):
        nums = [30, 20, 10, 5, 10, 40]
        self.assertEqual(find_min_idx_convex(nums), 3)

    def test_min_idx_dups(self):
        nums = [5, 4, 3, 2, 2, 5]
        self.assertIsNone(find_min_idx_convex(nums))

    # TODO: detect sorted sequence
    #def test_min_idx_first(self):
    #    nums = [1, 2, 3, 4, 5]
    #    self.assertEqual(find_min_idx_convex(nums), 0)

    #def test_min_idx_last(self):
    #    nums = [5, 4, 3, 2, 1]
    #    self.assertEqual(find_min_idx_convex(nums), 4)

    def test_min_idx_none(self):
        self.assertIsNone(find_min_idx_convex(None), None)

    def test_min_idx_empty(self):
        self.assertIsNone(find_min_idx_convex([]), None)

    def test_found_odd(self):
        nums = [30, 20, 10, 5, 10]
        k = 5
        self.assertTrue(find_k_convex(nums, k))

    def test_found_even(self):
        nums = [30, 20, 10, 5, 10, 40]
        k = 5
        self.assertTrue(find_k_convex(nums, k))

    def test_notfound_odd(self):
        nums = [30, 20, 10, 5, 10]
        k = 15
        self.assertFalse(find_k_convex(nums, k))

    def test_notfound_even(self):
        nums = [30, 20, 10, 5, 10, 40]
        k = 15
        self.assertFalse(find_k_convex(nums, k))

if __name__ == "__main__":
    unittest.main()
