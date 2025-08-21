#!/usr/bin/env python3

import argparse
from itertools import accumulate
import sys
import unittest

# tags: prefix sum

# solution: prefix sum
# complexity:
# run-time: O(n) to build prefix sum, O(1) per query
# space: O(n)
def range_sum_query_immutable(nums: list[int], left: int, right: int) -> int:
    if not nums:
        return 0

    # first element is 0!
    prefix_sum = [0, nums[0]]

    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1]+nums[i])

    return prefix_sum[right+1]-prefix_sum[left]

# solution: Pythonic accumulate
# complexity:
# run-time: O(n) to build prefix sum, O(1) per query
# space: O(n)
def range_sum_query_immutable2(nums: list[int], left: int, right: int) -> int:
    if not nums:
        return 0

    # build prefix sum
    prefix_sum = list(accumulate(nums, initial=0))

    return prefix_sum[right+1]-prefix_sum[left]

class TestRangeSumQueryImmutable(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(range_sum_query_immutable([], 0, 0), 0)
        self.assertEqual(range_sum_query_immutable2([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(range_sum_query_immutable([5], 0, 0), 5)
        self.assertEqual(range_sum_query_immutable2([5], 0, 0), 5)

    def test_multiple_elements(self):
        self.assertEqual(range_sum_query_immutable([1, 2, 3, 4, 5], 1, 3), 9)
        self.assertEqual(range_sum_query_immutable2([1, 2, 3, 4, 5], 1, 3), 9)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    left = int(input())
    right = int(input())
    res = range_sum_query_immutable(nums, left, right)
    print(res)