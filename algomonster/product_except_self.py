#!/usr/bin/env python3

import argparse
from collections import deque
import sys
import unittest

# tags: prefix sum
# leetcode: 238

# non-solution: division
# * compute product of all numbers
# * iterate & divide by each
#
# issues:
# * not allowed if zeros present
# * floating point arithmetic issues

# solution: prefix & suffix products
# complexity
# run-time: O(n)
# space: O(n)
def product_except_self(nums: list[int]) -> list[int]:
    # forward prefix sum
    prefix_prod = [1]

    # skip first
    for i in range(1, len(nums)):
        prefix_prod.append(prefix_prod[-1]*nums[i-1])

    # backward prefix sum
    suffix_prod = deque([1])

    # skip last
    for i in range(len(nums)-2, -1, -1):
        suffix_prod.appendleft(suffix_prod[0]*nums[i+1])

    ans = []

    assert len(prefix_prod) == len(suffix_prod)

    for p,s in zip(prefix_prod, suffix_prod):
        ans.append(p*s)
    
    return ans

# solution: AlgoMonster in-place prefix & suffix running products
# complexity
# run-time: O(n)
# space: O(n)
def product_except_self2(nums: list[int]) -> list[int]:
    # preallocate & initialize to 1!
    ans = [1] * len(nums)

    # calc fwd prefix running product
    left = 1
    for i in range(len(nums)):
        # init before multiply!
        ans[i] = left
        left *= nums[i]

    # calc backwards/suffix running product
    right = 1
    for i in reversed(range(len(nums))):
        # init before multiply!
        ans[i] *= right
        right *= nums[i]

    return ans

class TestProductExceptSelf(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(product_except_self2([1, 2, 3, 4]), [24, 12, 8, 6])

        self.assertEqual(product_except_self([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(product_except_self2([0, 0, 0, 0]), [0, 0, 0, 0])

        self.assertEqual(product_except_self([1]), [1])
        self.assertEqual(product_except_self2([1]), [1])

        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
        self.assertEqual(product_except_self2([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    res = product_except_self(nums)
    print(" ".join(map(str, res)))