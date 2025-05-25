#!/usr/bin/env python3

import heapq
import sys
import unittest

# number: 703
# similar: 215
# title: Kth Largest Element in a Stream
# url: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# section:
# difficulty: easy
# tags: tree, design, bst, heap, binary tree, data stream

# constraints
# 1 <= k <= 10^4
# 0 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# -10^4 <= val <= 10^4
# At most 10^4 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you
# search for the kth element.

# solution: min heap
# complexity
# run-time: O(log k) for add(), O(log n) for construct
# space: O(k)
class KthLargest:

    def __init__(self, k, nums):
        self.heap = []
        self.k = k

        for n in nums:
            self.add(n)

    def add(self, val):
        heapq.heappush(self.heap, val)

        # pop *after* adding!
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        #print('heap:{}, k:{}'.format(self.heap, self.k))

        #return heapq.nlargest(self.k, self.heap)[-1] if self.heap else None
        # no need for nlargest, kth largest is top of min heap
        return self.heap[0] if self.heap else None

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

    def test_add2(self):
        nums = [7,7,7,7,8,3]
        k = 4
        obj = KthLargest(k, nums)
        self.assertEqual(obj.add(2), 7)
        self.assertEqual(obj.add(10), 7)
        self.assertEqual(obj.add(9), 7)
        self.assertEqual(obj.add(9), 8)

if __name__ == '__main__':
    sys.exit(unittest.main())
