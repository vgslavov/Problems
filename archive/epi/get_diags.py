#!/usr/bin/env python

import unittest

# get diagonals of a matrix
# input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# output: [[1], [2,4], [3, 5, 7], [6, 8], [9]]
# invalid: not a list and not a list of lists

def get_diag(matrix, row, col):
    print("matrix[{0}][{1}]: {2}".format(row, col, matrix[row][col]))

    if not (matrix and isinstance(matrix, list)):
        return None

    out = []
    while row < len(matrix) and col >= 0:
        out.append(matrix[row][col])
        row += 1
        col -= 1

    return out

def get_diags(matrix):
    if not (matrix and isinstance(matrix, list) and isinstance(matrix[0], list)):
        return None

    nrows = len(matrix)
    ncols = len(matrix[0])

    out = []
    for col in range(0, ncols):
        out.append(get_diag(matrix, 0, col))

    for row in range(1, nrows):
        out.append(get_diag(matrix, row, ncols-1))

    return out

class TestGetDiags(unittest.TestCase):

    def test_empty(self):
        self.assertIsNone(get_diags([]), None)

    def test_none(self):
        self.assertIsNone(get_diags(None), None)

    def test_invalid1(self):
        self.assertIsNone(get_diags([1]), None)

    def test_invalid2(self):
        self.assertIsNone(get_diags([1,2]), None)

    def test_double(self):
        matrix = [[1,2]]
        out = [[1],[2]]
        self.assertEqual(get_diags(matrix), out)

    def test_1x1(self):
        matrix = [[1]]
        out = [[1]]
        self.assertEqual(get_diags(matrix), out)

    def test_1x2(self):
        matrix = [[1,2]]
        out = [[1],[2]]
        self.assertEqual(get_diags(matrix), out)

    def test_2x1(self):
        matrix = [[1],[2]]
        out = [[1],[2]]
        self.assertEqual(get_diags(matrix), out)

    def test_2x2(self):
        matrix = [[1,2],[3,4]]
        out = [[1],[2,3],[4]]
        self.assertEqual(get_diags(matrix), out)

    def test_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        out = [[1], [2,4], [3, 5, 7], [6, 8], [9]]
        self.assertEqual(get_diags(matrix), out)

if __name__ == "__main__":
    unittest.main()
