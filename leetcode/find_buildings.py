#!/usr/bin/env python3

import sys
import unittest

# number: 1762
# title: Buildings With an Ocean View
# url: https://leetcode.com/problems/buildings-with-an-ocean-view/
# difficulty: medium
# tags: array, stack, monotonic stack

# constraints:
# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^9

# solution: stack
# complexity:
# run-time: O(n)
# space: O(n)
def find_buildings(heights):
    stack = []

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] <= h:
            stack.pop()
        stack.append(i)

    return stack

class TestFindBuildings(unittest.TestCase):
    def test_find_buildings(self):
        self.assertEqual(find_buildings([4, 2, 3, 1]), [0, 2, 3])
        self.assertEqual(find_buildings([4, 3, 2, 1]), [0, 1, 2, 3])
        self.assertEqual(find_buildings([1, 3, 2, 4]), [3])
        self.assertEqual(find_buildings([2, 2, 2, 2]), [3])

if __name__ == "__main__":
    sys.exit(unittest.main())