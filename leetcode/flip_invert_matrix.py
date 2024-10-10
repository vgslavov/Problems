#!/usr/bin/env python3

import sys
import unittest

# number: 832
# section: assessments
# difficulty: easy
# tags: array, two pointers, bit manipulation, matrix, simulation, microsoft

# constraints
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.

# solution: Pythonic reversed
# complexity
# run-time: O(n)
# space: O(1)
def flip_invert_matrix(image):
    # flip/reverse
    for i in range(len(image)):
        image[i] = list(reversed(image[i]))

    #print(f"reversed:{image}")

    # invert
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == 0:
                image[i][j] = 1
            else:
                image[i][j] = 0

    return image

# TODO: reverse in-place

class TestFlipInvertMatrix(unittest.TestCase):
    def test_empty(self):
        image = []
        expected = []
        self.assertEqual(flip_invert_matrix(image), expected)

    def test1(self):
        image = [[1,1,0],[1,0,1],[0,0,0]]
        expected = [[1,0,0],[0,1,0],[1,1,1]]
        self.assertEqual(flip_invert_matrix(image), expected)

    def test2(self):
        image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
        expected = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        self.assertEqual(flip_invert_matrix(image), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
