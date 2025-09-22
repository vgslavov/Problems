#!/usr/bin/env python3

import sys
import unittest

# number: 56
# title: Merge Intervals
# url: https://leetcode.com/problems/merge-intervals/
# section: intervals
# difficulty: medium
# tags: array, sorting, top 150, meta, grind 75

# constraints
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^4

# solution: sort + min/max
# complexity
# run-time: O(n*log n)?
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

def overlap(x, y):
    return not (x[1] < y[0] or y[1] < x[0])

# solution: sort + max
# complexity
# run-time: O(n*log n)
# space: O(n)
def merge_intervals2(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    ans = []

    for start, end in intervals:
        if ans and overlap(ans[-1], [start, end]):
            ans[-1][1] = max(ans[-1][1], end)
        else:
            ans.append([start, end])

    return ans

class TestMergeIntervals(unittest.TestCase):

    def test_empty(self):
        intervals = []
        self.assertFalse(merge_intervals(intervals))
        self.assertFalse(merge_intervals2(intervals))

    def test_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(merge_intervals(intervals), expected)
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        self.assertEqual(merge_intervals2(intervals), expected)

    def test_2(self):
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        self.assertEqual(merge_intervals(intervals), expected)
        intervals = [[1,4],[4,5]]
        self.assertEqual(merge_intervals2(intervals), expected)

    def test_3(self):
        intervals = [[1,4],[2,3]]
        expected = [[1,4]]
        self.assertEqual(merge_intervals(intervals), expected)
        intervals = [[1,4],[2,3]]
        self.assertEqual(merge_intervals2(intervals), expected)

    def test_4(self):
        intervals = [[1,4],[0,2],[3,5]]
        expected = [[0,5]]
        self.assertEqual(merge_intervals(intervals), expected)
        intervals = [[1,4],[0,2],[3,5]]
        self.assertEqual(merge_intervals2(intervals), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
