#!/usr/bin/env python3

import heapq
import sys
import unittest

# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# O(n + log k): slow!
def find_kth_largest1(nums, k):
    if not nums:
        return False
    elif k == 1:
        return max(nums)

    return heapq.nlargest(k, nums)[-1]

# O(n + log k): slow!
def find_kth_largest2(nums, k):
    if k == 1:
        return max(nums)

    nums2 = [-n for n in nums]
    heapq.heapify(nums2)

    ans = None
    for i in range(k):
        ans = -heapq.heappop(nums2)

    return ans

# O(n + log k): slow!
def find_kth_largest3(nums, k):
    if k == 1:
        return max(nums)

    # deep copy
    h = list(nums)
    heapq._heapify_max(h)

    ans = None
    for i in range(k):
        ans = heapq._heappop_max(h)

    return ans

# O(n log n): faster
def find_kth_largest4(nums, k):
    if not nums:
        return False
    elif k == 1:
        return max(nums)

    # or
    #return sorted(nums)[-k:][0]
    return sorted(nums, reverse=True)[:k][-1]

# O(n log n): fastest
def find_kth_largest5(nums, k):
    if not nums:
        return False
    elif k == 1:
        return max(nums)

    nums.sort()

    return nums[-k:][0]


class TestFindKthLargest(unittest.TestCase):
    def test_empty(self):
        nums = []
        k = 0
        self.assertFalse(find_kth_largest1(nums, k))
        self.assertFalse(find_kth_largest2(nums, k))
        self.assertFalse(find_kth_largest3(nums, k))
        self.assertFalse(find_kth_largest4(nums, k))
        self.assertFalse(find_kth_largest5(nums, k))

    def test_k1(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 1
        expected = 6
        self.assertEqual(find_kth_largest1(nums, k), expected)
        self.assertEqual(find_kth_largest2(nums, k), expected)
        self.assertEqual(find_kth_largest3(nums, k), expected)
        self.assertEqual(find_kth_largest4(nums, k), expected)
        self.assertEqual(find_kth_largest5(nums, k), expected)

    def test_k2(self):
        nums = [3,2,1,5,6,4]
        k = 2
        expected = 5
        self.assertEqual(find_kth_largest1(nums, k), expected)
        self.assertEqual(find_kth_largest2(nums, k), expected)
        self.assertEqual(find_kth_largest3(nums, k), expected)
        self.assertEqual(find_kth_largest4(nums, k), expected)
        self.assertEqual(find_kth_largest5(nums, k), expected)

    def test_k4(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        expected = 4
        self.assertEqual(find_kth_largest1(nums, k), expected)
        self.assertEqual(find_kth_largest2(nums, k), expected)
        self.assertEqual(find_kth_largest3(nums, k), expected)
        self.assertEqual(find_kth_largest4(nums, k), expected)
        self.assertEqual(find_kth_largest5(nums, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
