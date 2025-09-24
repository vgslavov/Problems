#!/usr/bin/env python3

import argparse
from collections import deque
import heapq
import sys
import unittest

# tags: heap, sliding window, monotonic queue

# solution: max heap
# complexity:
# run-time: O(n*log k)
# space: O(k)
def sliding_window_max(nums: list[int], k: int) -> list[int]:
    ans = []
    heap = []
    left = 0

    for right in range(len(nums)):
        # max heap: value, index
        heapq.heappush(heap, (-nums[right], right))

        # reached window size
        if right >= k - 1:
            # pop all indices outside window
            while heap[0][1] < left:
                heapq.heappop(heap)

            # window max
            ans.append(-heap[0][0])

            # slide window
            left += 1

    return ans

# solution: deque
# complexity:
# run-time: O(n)
# space: O(k)
# TODO: understand better
def sliding_window_max2(nums: list[int], k: int) -> list[int]:
    ans = []
    dq = deque()

    for i in range(len(nums)):
        # remove elements not in the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # add max for current window
        if i >= k - 1:
            ans.append(nums[dq[0]])

    return ans

class TestSlidingWindowMaximum(unittest.TestCase):
    def test_sliding_window_maximum(self):
        nums = [1, 3, 2, 5, 8, 7]
        k = 3
        expected = [3, 5, 8, 8]
        self.assertEqual(sliding_window_max(nums, k), expected)
        self.assertEqual(sliding_window_max2(nums, k), expected)

        nums = [9, 11]
        k = 2
        expected = [11]
        self.assertEqual(sliding_window_max(nums, k), expected)
        self.assertEqual(sliding_window_max2(nums, k), expected)

        nums = [4, -2]
        k = 2
        expected = [4]
        self.assertEqual(sliding_window_max(nums, k), expected)
        self.assertEqual(sliding_window_max2(nums, k), expected)

        nums = [1, 2, 3, 4, 5]
        k = 1
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(sliding_window_max(nums, k), expected)
        self.assertEqual(sliding_window_max2(nums, k), expected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    k = int(input())
    res = sliding_window_maximum(nums, k)
    print(" ".join(map(str, res)))