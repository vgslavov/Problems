#!/usr/bin/env python3

from collections import defaultdict
import argparse
import sys
import unittest

# tags: prefix sum

# solution: prefix sum + dict
# complexity:
# run-time: O(n)
# space: O(n)
def subarray_sum(arr: list[int], target: int) -> list[int]:
    curr_sum = 0

    # key: prefix_sum
    # value: index
    prefix_sums = defaultdict(int)
    # empty array
    prefix_sums[0] = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        # sum([i, j]) = sum([0, j]) - sum([0, i-1])
        # 0-----[i<----k---->j]---->
        complement = curr_sum - target

        if complement in prefix_sums:
            return [prefix_sums[complement], i+1]

        # right exclusive index: [)
        prefix_sums[curr_sum] = i + 1

    return []

class TestSubarraySum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(subarray_sum([], 0), [])

    def test_no_match(self):
        self.assertEqual(subarray_sum([1, 2, 3], 7), [])

    def test_match(self):
        self.assertEqual(subarray_sum([1, 2, 3, 4], 6), [0, 3])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum(arr, target)
    print(" ".join(map(str, res)))