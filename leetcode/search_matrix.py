#!/usr/bin/env python3

import bisect
import sys
import unittest

# number: 74
# section: binary search
# difficulty: medium
# tags: array, binary search, matrix

# constraints
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4

# complexity
# run-time: O(log(m) + log(n))
# space: O(1)
def binary_search(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return left

# complexity
# run-time: O(log(m) + log(n))
# space: O(1)
def find_row(matrix, target):
    left = 0
    right = len(matrix)-1

    # don't return None, that's False, same as 0th index
    if not matrix:
        return -1
    elif target < matrix[0][0] or target > matrix[-1][-1]:
        return -1

    while left <= right:
        mid = left + (right-left) // 2

        # equal to: need for 1-sized rows!
        if matrix[mid][0] <= target and target <= matrix[mid][-1]:
            return mid
        elif matrix[mid][0] > target:
            right = mid-1
        else:
            left = mid+1

    return -1

# solution: manual binary search x2
# complexity
# run-time: O(log(m) + log(n))
# space: O(1)
# TODO: combine 2 steps?
def search_matrix(matrix, target):
    row = find_row(matrix, target)
    #print('row:{}'.format(row))
    if row == -1:
        return False

    idx = binary_search(matrix[row], target)
    if idx < len(matrix[row]) and matrix[row][idx] == target:
        return True

    return False

# solution: manual binary search + Pythonic bisect
# complexity
# run-time: O(log(m) + log(n))
# space: O(1)
def search_matrix2(matrix, target):
    row = find_row(matrix, target)
    #print('row:{}'.format(row))
    if row == -1:
        return False

    idx = bisect.bisect_left(matrix[row], target)
    if idx < len(matrix[row]) and matrix[row][idx] == target:
        return True

    return False

class TestSearchMatrix(unittest.TestCase):
    def test_empty(self):
        matrix = []
        target = None
        self.assertFalse(search_matrix(matrix, target))
        self.assertFalse(search_matrix2(matrix, target))

    def test1(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        self.assertTrue(search_matrix(matrix, target))
        self.assertTrue(search_matrix2(matrix, target))

    def test2(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        self.assertFalse(search_matrix(matrix, target))
        self.assertFalse(search_matrix2(matrix, target))

    def test3(self):
        matrix = [[1]]
        target = 1
        self.assertTrue(search_matrix(matrix, target))
        self.assertTrue(search_matrix2(matrix, target))

if __name__ == '__main__':
    sys.exit(unittest.main())
