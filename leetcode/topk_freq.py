#!/usr/bin/env python3

from collections import defaultdict
import heapq
import sys
import unittest

# number: 347
# title: Top K Frequent Elements
# url: https://leetcode.com/problems/top-k-frequent-elements/
# section: meta
# difficulty: medium
# tags: array, hash table, divide & conquer, sorting, heap,
# bucket sort, counting, quickselect, meta

# constraints
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# solution: dict + min heap
# complexity
# run-time: O(n + u*log k) where u is unique
# space: O(n)
def topk_freq(nums, k):
    counts = defaultdict(int)

    for n in nums:
        counts[n] += 1

    heap = []
    for key,val in counts.items():
        heapq.heappush(heap, (val, key))

        if len(heap) > k:
            heapq.heappop(heap)

    return [key for _,key in heap]

class TestTopKFreq(unittest.TestCase):
    def test_example1(self):
        nums = [1,1,1,2,2,3]
        k = 2
        expected = [1, 2]
        result = topk_freq(nums, k)
        self.assertCountEqual(result, expected)

    def test_example2(self):
        nums = [1]
        k = 1
        expected = [1]
        result = topk_freq(nums, k)
        self.assertCountEqual(result, expected)

if __name__ == "__main__":
    sys.exit(unittest.main())