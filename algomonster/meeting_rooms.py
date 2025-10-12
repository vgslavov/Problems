#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: merge intervals
# leetcode: 252

def overlap(x, y):
    return not (x[1] <= y[0] or y[1] <= x[0])
    
# solution: sort & check overlap
# complexity:
# run-time: O(n*log n)
# space: O(1)
def meeting_rooms(intervals: list[list[int]]) -> bool:
    intervals.sort()
    
    for i in range(1, len(intervals)):
        if overlap(intervals[i-1], intervals[i]):
            return False
    
    return True

class TestMeetingRooms(unittest.TestCase):
    
    def test_meeting_rooms(self):
        self.assertEqual(meeting_rooms([[0,30],[5,10],[15,20]]), False)
        self.assertEqual(meeting_rooms([[7,10],[2,4]]), True)
        self.assertEqual(meeting_rooms([[1,5],[5,6]]), True)
        self.assertEqual(meeting_rooms([[1,5],[4,6]]), False)
        self.assertEqual(meeting_rooms([]), True)
        self.assertEqual(meeting_rooms([[1,10],[2,3],[4,5],[6,7],[8,9]]), False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = meeting_rooms(intervals)
    print("true" if res else "false")