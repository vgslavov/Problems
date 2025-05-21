#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 346
# title: Moving Average from Data Stream
# url: https://leetcode.com/problems/moving-average-from-data-stream/
# section: assessments
# difficulty: easy
# tags: array, design, queue, data stream, amazon

# constraints
# 1 <= size <= 1000
# -10^5 <= val <= 10^5
# At most 10^4 calls will be made to next.

# solution: deque
# complexity
# run-time: O(k)
# space: O(k)
class MovingAvg:

    def __init__(self, size: int):
        self.queue = deque(maxlen=size)
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.sum += val

        if not self.queue:
            self.queue.append(val)
            return float(val)

        # at capacity, remove the oldest value
        if len(self.queue) == self.size:
            self.sum -= self.queue[0]

        self.queue.append(val)
        return round(self.sum / len(self.queue), 5)

# TODO: faster?

class TestMovingAvg(unittest.TestCase):
    def test(self):
        size = 3
        obj = MovingAvg(size)
        self.assertEqual(obj.next(1), 1.0)
        self.assertEqual(obj.next(10), 5.5)
        self.assertEqual(obj.next(3), 4.66667)
        self.assertEqual(obj.next(5), 6.0)

if __name__ == '__main__':
    sys.exit(unittest.main())
