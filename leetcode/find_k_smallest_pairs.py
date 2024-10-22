#!/usr/bin/env python3

import heapq
import sys
import unittest

# number: 373
# section: heap
# difficulty: medium
# tags: array, heap, priority queue, top 150

# constraints
# m = len(nums1)
# n = len(nums2)
# 1 <= m, n <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 10^4
# k <= m * n

# solution: brute-force
# complexity
# run-time: O(m*n log m*n), slow (TLE)
# space: O(k)
def find_k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return False

    heap = []
    i = j = 0

    # optimization: don't go beyond min
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            heapq.heappush(heap, (-(nums1[i]+nums2[j]), [nums1[i],nums2[j]]))
            # optimization: don't grow heap beyond k
            if len(heap) > k:
                heapq.heappop(heap)

    #print(heap)
    return sorted([heapq.heappop(heap)[1] for _ in range(k)])

# solution: brute force, heap + 2 pointers
# complexity
# run-time: O(m*n log m*n)? too slow
# space: O(k)
# TODO: optimize, TLE, when to break?
def find_k_smallest_pairs2(nums1, nums2, k):
    heap = []
    i = j = 0

    while i < len(nums1) or j < len(nums2):
        if i < len(nums1) and j < len(nums2):
            curr_sum = nums1[i] + nums2[j]
            #print(f"curr_sum:{curr_sum}")
            heapq.heappush(heap, (-curr_sum, [nums1[i],nums2[i]]))

            if len(heap) > k:
                heapq.heappop(heap)

        if i < len(nums1):
            for z in range(min(i,len(nums2))):
                nums1_sum = nums1[i] + nums2[z]
                #print(f"nums1_sum:{nums1_sum}")
                heapq.heappush(heap, (-nums1_sum, [nums1[i],nums2[z]]))

                if len(heap) > k:
                    heapq.heappop(heap)

            i += 1

        if j < len(nums2):
            for z in range(min(j,len(nums1))):
                nums2_sum = nums1[z] + nums2[j]
                #print(f"nums2_sum:{nums2_sum}")
                heapq.heappush(heap, (-nums2_sum, [nums1[z],nums2[j]]))

                if len(heap) > k:
                    heapq.heappop(heap)

            j += 1

        # TODO: figure out when to break
        #if (len(heap) == k
        #    and min([heap[0][0], -curr_sum, -nums1_sum, -nums2_sum]) == heap[0][0]
        #):
        #    break

        #print(f"heap:{heap}")

    return sorted([heapq.heappop(heap)[1] for _ in range(k)])

# solution: leetcode, Dijkstra-like using heap
# complexity
# run-time: O(k log k)
# space: O(k)
def find_k_smallest_pairs3(nums1, nums2, k):
    # can't sum w/o an input
    if not nums1 or not nums2:
        return None

    # (sum, [nums1 index, nums2 index])
    heap = [(nums1[0]+nums2[0], [0,0])]
    # (nums1 index, nums2 index)
    visited = set()
    # [nums1 value, nums2, value]
    ans = []

    while k > 0 and len(heap):
        # next min sum
        s, [i,j] = heapq.heappop(heap)
        #print(f"s:{s},i:{i},j:{j}")
        ans.append([nums1[i],nums2[j]])

        if i+1 < len(nums1) and (i+1,j) not in visited:
            heapq.heappush(heap, (nums1[i+1]+nums2[j],[i+1,j]))
            # mark indices as visited only if you push to heap, to prevent dupes
            visited.add((i+1,j))

        if j+1 < len(nums2) and (i,j+1) not in visited:
            heapq.heappush(heap, (nums1[i]+nums2[j+1],[i,j+1]))
            visited.add((i,j+1))

        #print(f"ans:{ans}")
        #print(f"heap:{heap}")
        #print(f"visited:{visited}")
        #print(f"k:{k}")
        k -= 1

    return ans

class TestFindKSmallestPairs(unittest.TestCase):
    def test_empty(self):
        nums1 = []
        nums2 = []
        k = 0
        self.assertFalse(find_k_smallest_pairs(nums1, nums2, k))
        self.assertFalse(find_k_smallest_pairs2(nums1, nums2, k))

    def test_k3(self):
        nums1 = [1,7,11]
        nums2 = [2,4,6]
        k = 3
        expected = sorted([[1,2],[1,4],[1,6]])
        self.assertEqual(find_k_smallest_pairs(nums1, nums2, k), expected)
        self.assertEqual(find_k_smallest_pairs2(nums1, nums2, k), expected)

    def test_k2(self):
        nums1 = [1,1,2]
        nums2 = [1,2,3]
        k = 2
        expected = sorted([[1,1],[1,1]])
        self.assertEqual(find_k_smallest_pairs(nums1, nums2, k), expected)
        self.assertEqual(find_k_smallest_pairs2(nums1, nums2, k), expected)

    def test_diff_size(self):
        nums1 = [1,2,4,5,6]
        nums2 = [3,5,7,9]
        k = 3
        expected = sorted([[1,3],[2,3],[1,5]])
        self.assertEqual(find_k_smallest_pairs(nums1, nums2, k), expected)
        self.assertEqual(find_k_smallest_pairs2(nums1, nums2, k), expected)

    def test_nums1xnums2(self):
        nums1 = [1,2,4,5,6]
        nums2 = [3,5,7,9]
        k = 20
        expected = sorted([[1,3],[2,3],[1,5],[2,5],[4,3],[1,7],[5,3],[2,7],[4,5],[6,3],[1,9],[5,5],[2,9],[4,7],[6,5],[5,7],[4,9],[6,7],[5,9],[6,9]])
        self.assertEqual(find_k_smallest_pairs(nums1, nums2, k), expected)
        self.assertEqual(find_k_smallest_pairs2(nums1, nums2, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
