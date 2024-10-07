#!/usr/bin/env python3

import math

# section: assessments
# difficulty: medium
# tags: meta

# constraints
# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is either 0 or 1.
# mat[i] is sorted in non-decreasing order.
#
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged
# Wrong Answer.

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# solution: brute-force
# complexity
# run-time: O(n^2)
# space: O(1)
def leftmost_col(binaryMatrix: 'BinaryMatrix') -> int:
    rows,cols = binaryMatrix.dimensions()

    for j in range(cols):
        for i in range(rows):
            if binaryMatrix.get(i,j) == 1:
                return j

    return -1

# solution: left-most match binary-search
# complexity
# run-time: O(log n)
# space: O(1)
def binary_search(binaryMatrix, row, length, k):
    left = 0
    right = length

    while left < right:
        mid = (left+right) // 2

        cell = binaryMatrix.get(row, mid)

        if cell >= k:
            right = mid
        else:
            left = mid+1

    return left

# solution: binary search
# complexity
# run-time: O(n*log n)
# space: O(1)
def leftmost_col2(binaryMatrix: 'BinaryMatrix') -> int:
    rows,cols = binaryMatrix.dimensions()
    ans = math.inf

    for i in range(rows):
        j = binary_search(binaryMatrix, i, cols, 1)
        #print(f"j:{j}")
        if j < cols and binaryMatrix.get(i,j) == 1:
            ans = min(ans, j)

    return ans if ans != math.inf else -1

# TODO: add unit test
# Input: mat = [[0,0],[1,1]]
# Output: 0

# Input: mat = [[0,0],[0,1]]
# Output: 1

# Input: mat = [[0,0],[0,0]]
# Output: -1

if __name__ == '__main__':
    sys.exit(unittest.main())
