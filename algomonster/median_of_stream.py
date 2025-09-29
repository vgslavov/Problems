#!/usr/bin/env python3

import argparse
import heapq
import sys
import unittest

# tags: heap

# solution: min & max heaps
# complexity:
# run-time: O(q*log q), where q is # of queries
# space: O(n)
class MedianOfStream:
    def __init__(self):
        # store numbers *larger* than median
        self.min_heap = []

        # store numbers *smaller* than median
        self.max_heap = []

        # invariant:
        # self.max_heap[0] <= median <= self.min_heap[0]

    def add_number(self, num: float) -> None:
        # min heap contains the larger numbers
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        self._balance()

    def _balance(self) -> None:
        if abs(len(self.min_heap)-len(self.max_heap)) <= 1:
            return

        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_median(self) -> float:
        #print(f"get_median: max_heap:{self.max_heap}, min_heap:{self.min_heap}")

        if len(self.min_heap) == len(self.max_heap):
            # median is average of two middle values
            # subtract because max_heap stores negative values
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]

class TestMedianOfStream(unittest.TestCase):
    def test_median_of_stream(self):
        median_of_stream = MedianOfStream()
        numbers = [1, 5, 2, 4, 3]
        for num in numbers:
            median_of_stream.add_number(num)
        self.assertEqual(median_of_stream.get_median(), 3)
        median_of_stream.add_number(6)
        self.assertEqual(median_of_stream.get_median(), 3.5)
        median_of_stream.add_number(7)
        self.assertEqual(median_of_stream.get_median(), 4)
        median_of_stream.add_number(8)
        self.assertEqual(median_of_stream.get_median(), 4.5)
        median_of_stream.add_number(9)
        self.assertEqual(median_of_stream.get_median(), 5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    median_of_stream = MedianOfStream()
    n = int(input())
    for _ in range(n):
        line = input().strip()
        if line == "get":
            median = median_of_stream.get_median()
            print(f"{median:.1f}")
        else:
            num = float(line)
            median_of_stream.add_number(num)