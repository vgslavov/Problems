#!/usr/bin/env python3

import argparse
from collections import defaultdict
import sys
import unittest

# tags: prefix sum

# solution: prefix sum + dict
# complexity:
# run-time: O(n)
# space: O(n)
def subarray_sum_total(arr: list[int], target: int) -> int:
    ans = 0
    curr_sum = 0

    # key: prefix sum so far
    # value: frequency of prefix sum
    prefix_sums = defaultdict(int)
    # empty subarray freq
    prefix_sums[0] = 1

    for i in range(len(arr)):
        curr_sum += arr[i]

        # sum([i, j]) = sum([0, j]) - sum([0, i-1])
        # 0-----[i<-------->j]---->
        # target = curr_sum - complement
        complement = curr_sum - target

        if complement in prefix_sums:
            ans += prefix_sums[complement]

        prefix_sums[curr_sum] += 1
        
    return ans

class TestSubarraySumTotal(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(subarray_sum_total([], 0), 0)

    def test_no_match(self):
        self.assertEqual(subarray_sum_total([1, 2, 3], 7), 0)

    def test_match(self):
        self.assertEqual(subarray_sum_total([1, 2, 3, 4], 6), 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_total(arr, target)
    print(res)