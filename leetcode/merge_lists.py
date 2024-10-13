#!/usr/bin/env python3

import copy
import sys
import unittest

# number: 88
# section: array/string
# difficulty: easy
# tags: array, two pointers, sorting, top 150, meta

# constraints
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[j] <= 10^9

# solution: Pythonic & slow
# complexity
# run-time: O((m+n) * log(m+n))
# space: O(1)
def merge_lists1(nums1, m, nums2, n):
    # don't extend as len(nums1) > m
    nums1[m:] = nums2
    nums1.sort()

# solution: two pointers
# complexity
# run-time: O(m + n)
# space: O(m + n)
def merge_lists2(nums1, m, nums2, n):
    merged = []
    i = j = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < m:
        merged.append(nums1[i])
        i += 1

    while j < n:
        merged.append(nums2[j])
        j += 1

    # shallow copy
    #nums1 = merged[:]
    #nums1 = merged.copy()
    nums1 = copy.deepcopy(merged)

class TestMergeLists(unittest.TestCase):
    def test_empty1(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected = [1]

        merge_lists1(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

        merge_lists2(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

    def test_empty2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expected = [1]

        merge_lists1(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

        merge_lists2(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

    def test_merged(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]

        merge_lists1(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

        merge_lists2(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
