#!/usr/bin/env python3

import bisect
import sys
import unittest

def find_min_index(nums):
    if not nums:
        return None

    start, end = 0, len(nums) -1

    while start < end:
        # don't overflow
        mid = start + (end-start) // 2

        # go left
        if nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
            print('find_min_index: going left, start={}, mid={}, end={}'.format(start, mid, end))
            end = mid
        # go right
        elif nums[mid-1] > nums[mid] and nums[mid] > nums[mid+1]:
            print('find_min_index: going right, start={}, mid={}, end={}'.format(start, mid, end))
            start = mid
        # found it!
        elif nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
            print('found min_index={}'.format(mid))
            return mid
        else:
            print('error in find_min_index: start={}, mid={}, end={}'.format(start, mid, end))

    return None

# O(log N)
def binary_search1(nums, k, start, end):
    if not nums:
        print('empty list')
        return False

    if start > end:
        print('invalid range')
        return False

    mid = start + (end-start) // 2

    while start <= end:
        # go right
        if nums[start] > k and k > nums[mid]:
            start = mid
        # go left
        elif nums[mid] < k and k < nums[end]:
            end = mid
        # found it!
        elif nums[mid] == k:
            print('found k={}'.format(k))
            return True
        else:
            print('error in binary_search: start={}, mid={}, end={}'.format(start, mid, end))

    return False

# bisect: only works for sorted in *ascending* order
# O(log N)
def binary_search2(nums, k, start, end):
    if not nums:
        print('empty list')
        return False

    if start > end:
        print('invalid range')
        return False

    # basic check for sorting
    if nums[start] > nums[end]:
        print('not sorted')
        return False

    index = bisect.bisect_left(nums, k, start, end)
    # found only if index is in range
    # and element at that index matches
    if index < (end - start + 1) and nums[index] == k:
        return True

    return False

def inflected_search(nums, k):
    if not nums:
        print('empty list')
        return False

    # find index of min element
    min_index = find_min_index(nums)

    if not min_index:
        print('min index not found')
        return False

    # search left using custom binary search
    # then right, using bisect_left
    # (bisect_left only supports sorted in ascending order)
    return binary_search1(nums, k, 0, min_index) or \
           binary_search2(nums, k, min_index, len(nums)-1)

class TestInflectedSearch(unittest.TestCase):

    def test_empty(self):
        v = []
        k = 5
        self.assertFalse(inflected_search(v, k))

    def test_inflected_found_odd(self):
        v = [15, 10, 1, 11, 20]
        k = 10
        self.assertTrue(inflected_search(v, k))

    def test_inflected_found_even(self):
        v = [15, 10, 9, 8, 4, 11, 20, 30]
        k = 10
        self.assertTrue(inflected_search(v, k))

    #def test_inflected_notfound(self):
    #    v = [15, 10, 9, 2, 20, 30]
    #    k = 99
    #    self.assertFalse(inflected_search(v, k))

    #def test_ascending(self):
    #    v = [2, 11, 20, 30, 99, 100]
    #    k = 10
    #    self.assertTrue(inflected_search(v, k))

    #def test_descending(self):
    #    v = [99, 80, 70, 10, 2]
    #    k = 10
    #    self.assertTrue(inflected_search(v, k))

    #def test_duplicates_found(self):
    #    v = [99, 99, 99, 99, 99, 99]
    #    k = 99
    #    self.assertTrue(inflected_search(v, k))

    #def test_duplicates_notfound(self):
    #    v = [99, 99, 99, 99, 99, 99]
    #    k = 100
    #    self.assertTrue(inflected_search(v, k))

if __name__ == '__main__':
    sys.exit(unittest.main())
