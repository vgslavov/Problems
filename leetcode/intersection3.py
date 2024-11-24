#!/usr/bin/env python3

import sys
import unittest

# number: 1213
# section: meta
# difficulty: easy
# tags: array, hash table, binary search, counting

# constraints
# n = len(arr1)
# m = len(arr2)
# l = len(arr3)
# 1 <= n, m, l <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000
# input is sorted

# solution: 3 pointers
# complexity
# run-time: O(max(n,m,l))
# space: O(1)
def intersection3(arr1, arr2, arr3):
    ans = []
    i = j = k = 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            ans.append(arr1[i])
            i += 1
            j += 1
            k += 1
            continue

        if arr2[j] >= arr1[i] <= arr3[k]:
            i += 1
        elif arr1[i] >= arr2[j] <= arr3[k]:
            j += 1
        elif arr1[i] >= arr3[k] <= arr2[j]:
            k += 1

    return ans

# solution: Pythonic set &
# complexity
# run-time: O(max(n,m,l))?
# space: O(1)?
def intersection3_2(arr1, arr2, arr3):
    return sorted(list(set(arr1) & set(arr2) & set(arr3)))

class TestIntersection3(unittest.TestCase):
    def test1(self):
        arr1 = [1,2,3,4,5]
        arr2 = [1,2,5,7,9]
        arr3 = [1,3,4,5,8]
        expected = [1,5]
        self.assertEqual(intersection3(arr1, arr2, arr3), expected)
        self.assertEqual(intersection3_2(arr1, arr2, arr3), expected)

    def test2(self):
        arr1 = [197,418,523,876,1356]
        arr2 = [501,880,1593,1710,1870]
        arr3 = [521,682,1337,1395,1764]
        expected = []
        self.assertEqual(intersection3(arr1, arr2, arr3), expected)
        self.assertEqual(intersection3_2(arr1, arr2, arr3), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
