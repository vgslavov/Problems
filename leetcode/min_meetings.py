#!/usr/bin/env python3

import heapq
import sys
import unittest

# number: 253
# title: Meeting Rooms II
# url: https://leetcode.com/problems/meeting-rooms-ii/
# section: meta
# difficulty: medium
# tags: array, two pointers, greedy, sorting, heap, prefix sum, citadel

# constraints
# 1 <= intervals.length <= 10^4
# 0 <= starti < endi <= 10^6

# solution: min heap
# complexity
# run-time: O(n log n)
# space: O(n)
def min_meetings(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    
    # sort by start time
    intervals.sort(key=lambda x: x[0])

    # min heap for storing start/end times
    rooms = []

    # add end time of first meeting
    heapq.heappush(rooms, intervals[0][1])

    # skip first meeting
    for start, end in intervals[1:]:
        # the next meeting is starting after the end of the earliest ending one
        if rooms[0] <= start:
            heapq.heappop(rooms)

        # add next meeting's end time to heap
        heapq.heappush(rooms, end)

    return len(rooms)

if __name__ == '__main__':
    sys.exit(unittest.main())