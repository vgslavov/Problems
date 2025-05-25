#!/usr/bin/env python3

import sys
import unittest

# number: 452
# title: Minimum Number of Arrows to Burst Balloons
# url: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# section: intervals
# difficulty: medium
# tags: array, greedy, sorting, top 150

# constraints
# 1 <= points.length <= 10^5
# points[i].length == 2
# -2^31 <= xstart < xend <= 2^31 - 1

# solution: Leetcode greedy
# run-time: O(n*log n)
# space: O(1)
def find_min_arrows(points):
    # sort by end
    points.sort(key = lambda x: x[1])
    ans = 1
    first_end = points[0][1]

    for start, end in points:
        # more arrows if gap b/w first end & next start
        if start > first_end:
            ans += 1
            first_end = end

    return ans

class TestFindMinArrows(unittest.TestCase):
    def test_one(self):
        points = [[0,1]]
        expected = 1
        self.assertEqual(find_min_arrows(points), expected)

    def test2(self):
        points = [[10,16],[2,8],[1,6],[7,12]]
        expected = 2
        self.assertEqual(find_min_arrows(points), expected)

    def test3(self):
        points = [[1,2],[3,4],[5,6],[7,8]]
        expected = 4
        self.assertEqual(find_min_arrows(points), expected)

    def test3(self):
        points = [[1,2],[2,3],[3,4],[4,5]]
        expected = 2
        self.assertEqual(find_min_arrows(points), expected)

    def test4(self):
        points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
        expected = 2
        self.assertEqual(find_min_arrows(points), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
