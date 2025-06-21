#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 560
# title: Subarray Sum Equals K
# url: https://leetcode.com/problems/subarray-sum-equals-k/
# difficulty: medium
# tags: array, hash table, prefix sum

# constraints:
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -107 <= k <= 10^7

# non-solution: brute force
# complexity:
# run-time: O(n^3), TLE
# space: O(n)
def subarray_sum(nums: list[int], k: int) -> int:
    ans = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            #print(f"len(nums): {len(nums)}, i: {i}, j: {j}, sum: {sum(nums[i:j])}, k: {k}")
            if sum(nums[i:j]) == k:
                ans += 1

    return ans

# non-solution: brute force
# complexity:
# run-time: O(n^2), TLE
# space: O(n)
def subarray_sum2(nums: list[int], k: int) -> int:
    ans = 0

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                ans += 1

    return ans

# non-solution: prefix sum with brute force
# complexity:
# run-time: O(n^2), TLE
# space: O(n)
def subarray_sum3(nums: list[int], k: int) -> int:
    # preallocate
    prefix = [0] * (len(nums) + 1)
    ans = 0

    # build prefix sum
    # 1 past end!
    for i in range(1, len(nums)+1):
        prefix[i] = prefix[i-1] + nums[i-1]

    for i in range(len(nums)):
        for j in range(i+1, len(prefix)):
            if prefix[j] - prefix[i] == k:
                ans += 1

    return ans

# solution: Leetcode prefix sum + defaultdict
# complexity:
# run-time: O(n)
# space: O(n)
def subarray_sum4(nums: list[int], k: int) -> int:
    ans = 0
    prefix_sum = 0

    # prefix sum to counts
    counts = defaultdict(int)
    # edge case: -1 index of prefix sum is 0
    counts[0] = 1

    for i in range(len(nums)):
        # build prefix sum but don't store intermediate results
        prefix_sum += nums[i]

        if prefix_sum-k in counts:
            ans += counts[prefix_sum-k]

        counts[prefix_sum] += 1

    return ans

class TestSubarraySum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(subarray_sum([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum2([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum3([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum4([1, 1, 1], 2), 2)

    def test_example2(self):
        self.assertEqual(subarray_sum([1, 2, 3], 3), 2)
        self.assertEqual(subarray_sum2([1, 2, 3], 3), 2)
        self.assertEqual(subarray_sum3([1, 2, 3], 3), 2)
        self.assertEqual(subarray_sum4([1, 2, 3], 3), 2)

    def test_example3(self):
        self.assertEqual(subarray_sum([-1, -1, 1], 0), 1)
        self.assertEqual(subarray_sum2([-1, -1, 1], 0), 1)
        self.assertEqual(subarray_sum3([-1, -1, 1], 0), 1)
        self.assertEqual(subarray_sum4([-1, -1, 1], 0), 1)

    def test_empty(self):
        self.assertEqual(subarray_sum([], 0), 0)
        self.assertEqual(subarray_sum2([], 0), 0)
        self.assertEqual(subarray_sum3([], 0), 0)
        self.assertEqual(subarray_sum4([], 0), 0)

    def test_single_element(self):
        self.assertEqual(subarray_sum([5], 5), 1)
        self.assertEqual(subarray_sum2([5], 5), 1)
        self.assertEqual(subarray_sum3([5], 5), 1)
        self.assertEqual(subarray_sum4([5], 5), 1)
        self.assertEqual(subarray_sum([5], 0), 0)
        self.assertEqual(subarray_sum2([5], 0), 0)
        self.assertEqual(subarray_sum3([5], 0), 0)
        self.assertEqual(subarray_sum4([5], 0), 0)

if __name__ == "__main__":
    sys.exit(unittest.main())