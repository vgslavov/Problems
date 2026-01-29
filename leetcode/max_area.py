#!/usr/bin/env python3

import sys
import unittest

# number: 11
# title: Container With Most Water
# url: https://leetcode.com/problems/container-with-most-water/
# section: two pointers
# difficulty: medium
# tags: array, two pointers, greedy, top 150, grind 75

# constraints
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

# solution: two pointers
# complexity
# run-time: O(n)
# space: O(1)
def max_area(height):
    i = 0
    j = len(height)-1

    ans = 0
    while i < j:
        l = j - i
        h = min(height[i], height[j])
        ans = max(ans, l*h)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return ans

class TestMaxArea(unittest.TestCase):

    def test_empty(self):
        height = []
        expected = 0
        self.assertEqual(max_area(height), expected)

    def test1(self):
        height = [1,8,6,2,5,4,8,3,7]
        expected = 49
        self.assertEqual(max_area(height), expected)

    def test2(self):
        height = [1,1]
        expected = 1
        self.assertEqual(max_area(height), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
