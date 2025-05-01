#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 325
# section: meta
# difficulty: medium
# tags: array, hash table, prefix sum, meta

# constraints
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# -10^4 <= k <= 10^4

# solution: prefix sum + defaultdict
# complexity
# run-time: O(n)
# space: O(n)
def max_subarray_len2(nums, k) -> int:
    if not nums:
        return 0

    # calculate prefix sum
    # TODO: don't build full prefix sum, use a variable?
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1]+nums[i])

    #print(f"prefix:{prefix}")

    d = {}
    ans = 0
       
    for i in range(len(prefix)):
        # do check if sum so far is equal to k
        if prefix[i] == k:
            # add 1 because we want to count the first index
            ans = i + 1

        # like two sum
        sum = prefix[i]-k
        if sum in d:
            ans = max(ans, i-d[sum])

        # don't prebuild
        # don't overwrite the first index of prefix sum
        # because we want to keep the first index
        # (to maximize len)
        if prefix[i] not in d:
            d[prefix[i]] = i
            
    return ans

class TestMaxSubarrayLen2(unittest.TestCase):
    def test_empty(self):
        nums = []
        k = 0
        expected = 0
        self.assertEqual(max_subarray_len2(nums, k), expected)

    def test1(self):
        nums = [1,-1,5,-2,3]
        k = 3
        expected = 4
        self.assertEqual(max_subarray_len2(nums, k), expected)

    def test2(self):
        nums = [-2,-1,2,1]
        k = 1
        expected = 2
        self.assertEqual(max_subarray_len2(nums, k), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())