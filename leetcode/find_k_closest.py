#!/usr/bin/env python3

import heapq
import math
import sys
import unittest

# number: 973
# title: K Closest Points to Origin
# url: https://leetcode.com/problems/k-closest-points-to-origin/
# section: meta
# difficulty: medium
# tags: heap, math, meta

# constraints
# 1 <= k <= points.length <= 10^4
# -10^4 <= x_i, y_i <= 10^4

# solution: min heap
# complexity
# run-time: O(n*log n)
# space: O(n)
def find_k_closest(points, k):
    if not points:
        return None

    heap = []

    for p in points:
        dist = math.sqrt(pow(p[0] - 0, 2) + pow(p[1] - 0, 2))

        heapq.heappush(heap, (dist, p))

    ans = []
    for i in range(k):
        ans.append(heapq.heappop(heap)[1])

    # TODO: avoid sort()
    ans.sort()
    return ans

# solution: max heap
# complexity
# run-time: O(n*log k)
# space: O(k)
def find_k_closest2(points, k):
    if not points:
        return None

    heap = []

    for p in points:
        dist = math.sqrt(pow(p[0] - 0, 2) + pow(p[1] - 0, 2))

        # max heap!
        heapq.heappush(heap, (-dist, p))

        if len(heap) > k:
            heapq.heappop(heap)

    return [pair[1] for pair in heap]

class TestFindKClosest(unittest.TestCase):

    def test_empty(self):
        points = []
        k = 1
        self.assertFalse(find_k_closest(points, k))
        self.assertFalse(find_k_closest2(points, k))

    def test_k1(self):
        points = [[1,3],[-2,2]]
        k = 1
        expected = [[-2,2]]
        self.assertEqual(expected, find_k_closest(points, k))
        self.assertEqual(expected, find_k_closest2(points, k))

    def test_k2(self):
        points = [[3,3],[5,-1],[-2,4]]
        k = 2
        expected = [[-2,4],[3,3]]
        self.assertEqual(expected, find_k_closest(points, k))
        self.assertEqual(expected, find_k_closest2(points, k))


if __name__ == '__main__':
    sys.exit(unittest.main())
