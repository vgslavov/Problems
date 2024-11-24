#!/usr/bin/env python3

import sys
import unittest

# number: 349
# section: meta
# difficulty: easy
# tags: array, hash table, two pointers, binary search, sorting, meta

# constraints
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# solution: Pythonic set &
# complexity
# run-time: O(max(n, m))
# space: O(n+m)
def intersection(nums1, nums2):
    return sorted(list(set(nums1) & set(nums2)))

# solution: sort + two pointers
# complexity
# run-time: O(n*log n + m*log m)
# space: O(n+m)
def intersection2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i = j = 0
    ans = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            ans.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1

    return sorted(list(set(ans)))

# TODO: solve using dict for O(n) space

class TestIntersection(unittest.TestCase):
    def test_empty(self):
        nums1 = []
        nums2 = []
        expected = []
        self.assertEqual(intersection(nums1, nums2), expected)
        self.assertEqual(intersection2(nums1, nums2), expected)

    def test1(self):
        nums1 = [1,2,2,1]
        nums2 = [2,2]
        expected = [2]
        self.assertEqual(intersection(nums1, nums2), expected)
        self.assertEqual(intersection2(nums1, nums2), expected)

    def test2(self):
        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]
        expected = [4,9]
        self.assertEqual(intersection(nums1, nums2), expected)
        self.assertEqual(intersection2(nums1, nums2), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
