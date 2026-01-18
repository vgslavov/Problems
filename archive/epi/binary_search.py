#!/usr/bin/env python

import unittest

# sorted in ascending order
# time: O(log n)
def binary_search(nums, k):

    if not nums:
        return False

    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end)/2

        #print("start: {0}".format(start))
        #print("mid: {0}".format(mid))
        #print("end: {0}".format(end))

        # found
        if nums[mid] == k:
            return True
        # go right
        elif nums[mid] < k:
            start = mid+1
        # go left
        elif nums[mid] > k:
            end = mid-1
        else:
            return False

    return False

class TestBinarySearch(unittest.TestCase):

    def test_empty(self):
        nums = []
        k = 3
        self.assertFalse(binary_search(nums, k))

    def test_none(self):
        k = 3
        self.assertFalse(binary_search(None, k))

    def test_found_odd(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        self.assertTrue(binary_search(nums, k))

    def test_found_even(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 3
        self.assertTrue(binary_search(nums, k))

    def test_notfound_odd(self):
        nums = [1, 2, 3, 4, 5]
        k = 7
        self.assertFalse(binary_search(nums, k))

    def test_notfound_even(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 7
        self.assertFalse(binary_search(nums, k))

    def test_found_dups(self):
        nums = [1, 2, 3, 3, 5]
        k = 5
        self.assertTrue(binary_search(nums, k))

    def test_notfound_dups(self):
        nums = [1, 2, 3, 3, 5]
        k = 7
        self.assertFalse(binary_search(nums, k))

if __name__ == "__main__":
    unittest.main()
