#!/usr/bin/env python3

import sys
import unittest

# number: 1570
# title: Dot Product of Two Sparse Vectors
# url: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
# section: meta
# difficulty: medium
# tags: array, hash table, two pointers, design, meta

# constraints
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100

# solution: brute-force
# complexity
# run-time: O(n)
# space: O(1)
class SparseVector:
    def __init__(self, nums):
        self.__nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.__nums) != len(vec.__nums):
            return 0

        ans = 0

        for n1, n2 in zip(vec.__nums, self.__nums):
            ans += n1*n2

        return ans

# solution: dict
# complexity
# run-time: O(n)
# space: O(1)
class SparseVector2:
    def __init__(self, nums):
        # store nonzeros only: index to value
        self.__dict = {i:nums[i] for i in range(len(nums)) if nums[i]}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0

        for k,v in self.__dict.items():
            if k in vec.__dict:
                ans += v * vec.__dict[k]

        return ans

# Your SparseVector object will be instantiated and called as such:
num1 = [1,2,3]
v1 = SparseVector(num1)
num2 = [0,3,4,33]
v2 = SparseVector(num2)
ans = v1.dotProduct(v2)

if __name__ == '__main__':
    sys.exit(unittest.main())