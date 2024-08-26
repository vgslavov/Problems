#!/usr/bin/env python3

import heapq
import sys
import unittest

# related: #215 (find_k_largest)

# constraints
# 1 <= k <= 10^4
# 0 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# -10^4 <= val <= 10^4
# At most 10^4 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you
# search for the kth element.

# solution: heap + Pythonic nlargest
# complexity
# run-time: ?
# space: O(k)?
class KthLargest:

    def __init__(self, k, nums):
        self.heap = []
        self.k = k

        for n in nums:
            heapq.heappush(self.heap, n)

            # limit size of heap to k
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

        #print('heap:{}, k:{}'.format(self.heap, self.k))

    def add(self, val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        #print('heap:{}, k:{}'.format(self.heap, self.k))

        # TODO: speed up
        return heapq.nlargest(self.k, self.heap)[-1] if self.heap else None

class TestKthLargest(unittest.TestCase):

    def test_empty(self):
        nums = []
        k = 0
        val = 0
        obj = KthLargest(k, nums)
        self.assertFalse(obj.add(val))

    def test_add(self):
        nums = [4, 5, 8, 2]
        k = 3
        obj = KthLargest(k, nums)
        self.assertEqual(obj.add(3), 4)
        self.assertEqual(obj.add(5), 5)
        self.assertEqual(obj.add(10), 5)
        self.assertEqual(obj.add(9), 8)
        self.assertEqual(obj.add(4), 8)

if __name__ == '__main__':
    sys.exit(unittest.main())
