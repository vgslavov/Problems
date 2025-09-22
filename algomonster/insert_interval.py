#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: merge intervals

def overlap(x, y):
    return not (x[1] < y[0] or y[1] < x[0])
    
# solution: append, sort & max
# complexity:
# run-time: O(n*log n)
# space: O(n)
def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    intervals.append(new_interval)
    intervals.sort()
    ans = []

    for start,end in intervals:
        if ans and overlap(ans[-1], [start,end]):
            ans[-1][1] = max(ans[-1][1], end)
        else:
            ans.append([start,end])
        
    return ans

# solution: AlgoMonster insert & merge intervals
# complexity:
# run-time: O(n)
# space: O(n)
def insert_interval2(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    ans = []
    i = 0
    n = len(intervals)

    # 1. add all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        ans.append(intervals[i])
        i += 1

    # 2. merge new_interval with overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    ans.append(new_interval)

    # 3. add all remaining intervals
    while i < n:
        ans.append(intervals[i])
        i += 1

    return ans

class TestInsertInterval(unittest.TestCase):
    
    def test_insert_interval(self):
        self.assertEqual(insert_interval([[1,3],[6,9]],[2,5]), [[1,5],[6,9]])
        self.assertEqual(insert_interval2([[1,3],[6,9]],[2,5]), [[1,5],[6,9]])

        self.assertEqual(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]), [[1,2],[3,10],[12,16]])
        self.assertEqual(insert_interval2([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]), [[1,2],[3,10],[12,16]])

        self.assertEqual(insert_interval([], [5,7]), [[5,7]])
        self.assertEqual(insert_interval2([], [5,7]), [[5,7]])

        self.assertEqual(insert_interval([[1,5]], [2,3]), [[1,5]])
        self.assertEqual(insert_interval2([[1,5]], [2,3]), [[1,5]])

        self.assertEqual(insert_interval([[1,5]], [2,7]), [[1,7]])
        self.assertEqual(insert_interval2([[1,5]], [2,7]), [[1,7]])

        self.assertEqual(insert_interval([[1,5]], [6,8]), [[1,5],[6,8]])
        self.assertEqual(insert_interval2([[1,5]], [6,8]), [[1,5],[6,8]])

        self.assertEqual(insert_interval([[3,5],[12,15]],[6,6]), [[3,5],[6,6],[12,15]])
        self.assertEqual(insert_interval2([[3,5],[12,15]],[6,6]), [[3,5],[6,6],[12,15]])

        self.assertEqual(insert_interval([[1,2],[3,4],[5,6]],[7,8]), [[1,2],[3,4],[5,6],[7,8]])
        self.assertEqual(insert_interval2([[1,2],[3,4],[5,6]],[7,8]), [[1,2],[3,4],[5,6],[7,8]])

        self.assertEqual(insert_interval([[1,2],[3,4],[5,6]],[0,0]), [[0,0],[1,2],[3,4],[5,6]])
        self.assertEqual(insert_interval2([[1,2],[3,4],[5,6]],[0,0]), [[0,0],[1,2],[3,4],[5,6]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    new_interval = [int(x) for x in input().split()]
    res = insert_interval(intervals, new_interval)
    for row in res:
        print(" ".join(map(str, row)))