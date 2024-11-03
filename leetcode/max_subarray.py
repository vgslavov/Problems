#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 2958
# section: citadel
# difficulty: medium
# tags: array, hash table, sliding window, citadel

# constraints
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= nums.length

# solution: sliding window + dict
# complexity
# run-time: O(n)
# space: O(n)
def max_subarray(nums: [], k: int) -> int:
    freqs = defaultdict(int)
    left = ans = 0

    for right in range(len(nums)):
        #print(f"left:{left},right:{right}")

        # always expand window: don't compare w/ k!
        freqs[nums[right]] += 1

        # shrink it
        while freqs[nums[right]] > k:
            freqs[nums[left]] -= 1
            left += 1

        ans = max(ans, right-left+1)

    return ans

class TestMaxSubarray(unittest.TestCase):
    def test_empty(self):
        nums = []
        k = 0
        expected = 0
        self.assertEqual(max_subarray(nums, k), expected)

    def test1(self):
        nums = [1,2,3,1,2,3,1,2]
        k = 2
        expected = 6
        self.assertEqual(max_subarray(nums, k), expected)

    def test2(self):
        nums = [1,2,1,2,1,2,1,2]
        k = 1
        expected = 2
        self.assertEqual(max_subarray(nums, k), expected)

    def test3(self):
        nums = [5,5,5,5,5,5,5]
        k = 4
        expected = 4
        self.assertEqual(max_subarray(nums, k), expected)

    def test4(self):
        nums = [1]
        k = 1
        expected = 1
        self.assertEqual(max_subarray(nums, k), expected)

    def test5(self):
        nums = [1,11]
        k = 2
        expected = 2
        self.assertEqual(max_subarray(nums, k), expected)

    def test6(self):
        nums = [3,1,1]
        k = 1
        expected = 2
        self.assertEqual(max_subarray(nums, k), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())