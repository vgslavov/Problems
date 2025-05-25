#!/usr/bin/env python3

import sys
import unittest

# number: 1051
# title: Height Checker
# url: https://leetcode.com/problems/height-checker/
# section: assessments
# difficulty: easy
# tags: array, sorting, counting sort, google

# constraints
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100

# solution: sorted
# complexity
# run-time: O(n)
# space: O(1)
def height_checker(heights):
    expected = sorted(heights)
    ans = 0

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            ans += 1

    return ans

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
