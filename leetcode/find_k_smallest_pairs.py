#!/usr/bin/env python3

import heapq
import sys
import unittest

# number: 373
# section: heap
# difficulty: medium
# tags: array, heap, priority queue, top 150

# constraints
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 10^4

# solution: brute-force
# complexity
# run-time: O(n^2), slow
# space: O(n), mem limit exceeded
# TODO: optimize mem, attempted
def find_k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return False

    heap = []
    i = j = 0

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            heapq.heappush(heap, (nums1[i]+nums2[j], (nums1[i],nums2[j])))
            # TODO: reduce size of heap by using max heap
            # reorders output pairs
            #heapq.heappush(heap, (-(nums1[i]+nums2[j]), (nums1[i],nums2[j])))
            #if len(heap) > k:
            #    heapq.heappop(heap)

    #print(heap)
    return [list(heapq.heappop(heap)[1]) for i in range(k)]

# TODO: faster, less mem
def find_k_smallest_pairs2(nums1, nums2, k):
    heap = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        heapq.heappush(heap, (-(nums1[i]+nums2[j]), (nums1[i],nums2[j])))
        if len(heap) > k:
            heapq.heappop(heap)

        # TODO: advance i & j
        if j < len(nums2)-1 and nums1[i] < nums2[j+1]:
            j += 1
        else:
            i += 1

    print(heap)
    return [list(heapq.heappop(heap)[1]) for i in range(len(heap))]

class TestFindKSmallestPairs(unittest.TestCase):
    def test_empty(self):
        nums1 = []
        nums2 = []
        k = 0
        self.assertFalse(find_k_smallest_pairs(nums1, nums2, k))
        #self.assertFalse(find_k_smallest_pairs2(nums1, nums2, k))

    def test_k3(self):
        nums1 = [1,7,11]
        nums2 = [2,4,6]
        k = 3
        expected = [[1,2],[1,4],[1,6]]
        self.assertEqual(find_k_smallest_pairs(nums1, nums2, k), expected)
        #self.assertEqual(find_k_smallest_pairs2(nums1, nums2, k), expected)

    def test_k2(self):
        nums1 = [1,1,2]
        nums2 = [1,2,3]
        k = 2
        expected = [[1,1],[1,1]]
        self.assertEqual(find_k_smallest_pairs(nums1, nums2, k), expected)

    def test_diff_size(self):
        nums1 = [1,2,4,5,6]
        nums2 = [3,5,7,9]
        k = 3
        expected = [[1,3],[2,3],[1,5]]
        self.assertEqual(find_k_smallest_pairs(nums1, nums2, k), expected)

    def test_nums1xnums2(self):
        nums1 = [1,2,4,5,6]
        nums2 = [3,5,7,9]
        k = 20
        expected = [[1,3],[2,3],[1,5],[2,5],[4,3],[1,7],[5,3],[2,7],[4,5],[6,3],[1,9],[5,5],[2,9],[4,7],[6,5],[5,7],[4,9],[6,7],[5,9],[6,9]]
        self.assertEqual(find_k_smallest_pairs(nums1, nums2, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
