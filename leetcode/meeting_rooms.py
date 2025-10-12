#!/usr/bin/env python3

import sys
import unittest

# number: 252
# title: Meeting Rooms
# url: https://leetcode.com/problems/meeting-rooms/
# difficulty: easy
# tags: array, sorting, intervals, grind 75

# constraints:
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i < end_i <= 10^6

def overlap(x, y):
    # not <= cause end/start can overlap
    return max(x[0], y[0]) < min(x[1], y[1])

# solution: sort + linear scan
# complexity:
# run-time: O(n*log n)
# space: O(1)
def can_attend_meetings(intervals: list[list[int]]) -> bool:
    intervals.sort()

    for i in range(1, len(intervals)):
        if overlap(intervals[i-1], intervals[i]):
            return False

    return True

class TestCanAttendMeetings(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(can_attend_meetings([[0,30],[5,10],[15,20]]) is False)

    def test_example2(self):
        self.assertTrue(can_attend_meetings([[7,10],[2,4]]) is True)

    def test_empty(self):
        self.assertTrue(can_attend_meetings([]) is True)

    def test_one(self):
        self.assertTrue(can_attend_meetings([[1,2]]) is True)

    def test_touching(self):
        self.assertTrue(can_attend_meetings([[1,2],[2,3]]) is True)

    def test_touching_reverse(self):
        self.assertTrue(can_attend_meetings([[2,3],[1,2]]) is True)

    def test_large(self):
        self.assertTrue(can_attend_meetings([[0,1000000],[1,2],[3,4]]) is False)

if __name__ == "__main__":
    sys.exit(unittest.main())