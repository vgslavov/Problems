#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: merge intervals

def overlap(x, y):
    return not (y[1] < x[0] or x[1] < y[0])
    
# solution: sort & max
# complexity:
# run-time: O(n*log n)
# space: O(n)
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    ans = []

    for start, end in intervals:
        # start of current is before previou end
        if ans and overlap(ans[-1], [start, end]):
            ans[-1][1] = max(ans[-1][1], end)
        else:
            ans.append([start, end])
        
    return ans

class TestMergeIntervals(unittest.TestCase):
    
    def test_merge_intervals(self):
        self.assertEqual(merge_intervals([[1,3],[2,4],[5,7],[6,8]]), [[1,4],[5,8]])
        self.assertEqual(merge_intervals([[1,4],[4,5]]), [[1,5]])
        self.assertEqual(merge_intervals([[1,4],[0,2],[3,5]]), [[0,5]])
        self.assertEqual(merge_intervals([[1,4]]), [[1,4]])
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([[1,4],[5,6]]), [[1,4],[5,6]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_intervals(intervals)
    for row in res:
        print(" ".join(map(str, row)))