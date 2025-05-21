#!/usr/bin/env python3

import sys
import unittest

# number: 56
# title: Merge Intervals
# url: https://leetcode.com/problems/merge-intervals/
# section: intervals
# difficulty: medium
# tags: array, sorting, top 150, meta

# constraints
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^4

# solution: sort + min/max
# complexity
# run-time: O(n*log n)
# space: O(1)!
def merge_intervals(intervals):
    intervals.sort()

    i = 1
    while i < len(intervals):
        #print("i:{}, intervals:{}".format(i, intervals))
        # beginning of current starts before end of previous
        if intervals[i][0] <= intervals[i-1][1]:
            intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
            intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
            # TODO: more efficient?
            del intervals[i-1]
        else:
            i += 1

    return intervals

class TestMergeIntervals(unittest.TestCase):

    def test_empty(self):
        intervals = []
        self.assertFalse(merge_intervals(intervals))

    def test_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_2(self):
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_3(self):
        intervals = [[1,4],[2,3]]
        expected = [[1,4]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_4(self):
        intervals = [[1,4],[0,2],[3,5]]
        expected = [[0,5]]
        self.assertEqual(merge_intervals(intervals), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
