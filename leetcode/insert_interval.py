#!/usr/bin/env python3

import sys
import unittest

# number: 57
# section: intervals
# difficulty: medium
# tags: array, interval

# constraints
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^5
# intervals is sorted by start_i in ascending order.
# new_interval.length == 2
# 0 <= start <= end <= 10^5

# solution: intervals
# complexity
# run-time: O(n), slow!
# space: O(n)
def insert_intervals(intervals, new_interval):
    ans = []
    inserted = False

    if not intervals:
        return [new_interval]

    def merge(start, end, append=True):
        if ans and start <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], end)
            return True
        elif append:
            ans.append([start,end])
            return True

        return False

    for start, end in intervals:
        #print("start:{},end:{}".format(start,end))

        if not inserted:
            if new_interval[0] < start:
                append = True
            else:
                append = False

            inserted = merge(new_interval[0], new_interval[1], append)

        merge(start, end)

        #print("ans:{}".format(ans))

    if not inserted:
        merge(new_interval[0], new_interval[1])

    return ans

class TestInsertIntervals(unittest.TestCase):
    def test_empty_intervals(self):
        intervals = []
        new = [5,7]
        expected = [new]
        self.assertEqual(insert_intervals(intervals, new), expected)

    def test_empty_all(self):
        intervals = []
        new = []
        expected = [new]
        self.assertEqual(insert_intervals(intervals, new), expected)

    def test_empty_all(self):
        intervals = []
        new = []
        expected = [new]
        self.assertEqual(insert_intervals(intervals, new), expected)

    def test_1(self):
        intervals = [[1,3],[6,9]]
        new = [2,5]
        expected = [[1,5],[6,9]]
        self.assertEqual(insert_intervals(intervals, new), expected)

    def test_2(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        new = [4,8]
        expected = [[1,2],[3,10],[12,16]]
        self.assertEqual(insert_intervals(intervals, new), expected)

    def test_3(self):
        intervals = [[1,5]]
        new = [2,7]
        expected = [[1,7]]
        self.assertEqual(insert_intervals(intervals, new), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
