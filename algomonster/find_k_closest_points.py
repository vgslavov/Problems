#!/usr/bin/env python3

import argparse
import heapq
import math
import sys
import unittest

# tags: heap

# solution: max heap
# complexity:
# run-time: O(n*log k)
# space: O(k)
def find_k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []

    for x,y in points:
        # distance b/w 2 points: sqrt((x1-x2)^2 + (y1-y2)^2)
        # origin: (0, 0)
        # optimization: no need to take sqrt!
        distance = (x**2 + y**2)
        # actual distance
        #distance = (x**2 + y**2) ** 0.5
        #distance = math.sqrt(pow(x, 2) + pow(y, 2))

        # heapq is min heap by default
        # make *max* heap by inverting the distance
        heapq.heappush(heap, (-distance, (x,y)))

        # don't store n, store k
        if len(heap) > k:
            # pop max value: k+1 closest to origin
            heapq.heappop(heap)

    # sort values, not keys!
    # (heap is already sorted)
    return sorted([p for _,p in heap])

class TestKClosestPoints(unittest.TestCase):
    def test_find_k_closest_points(self):
        points = [(1, 2), (3, 4), (5, 6)]
        k = 2
        expected = [(1, 2), (3, 4)]
        self.assertEqual(find_k_closest_points(points, k), expected)

        points = [(1, 2), (3, 4), (5, 6)]
        k = 3
        expected = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(find_k_closest_points(points, k), expected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    points = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = find_k_closest_points(points, k)
    for row in res:
        print(" ".join(map(str, row)))