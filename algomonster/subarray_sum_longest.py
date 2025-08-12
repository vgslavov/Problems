#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: sliding window, longest

# solution: sliding window
# complexity:
# run-time: O(n)
# space: O(1)
def subarray_sum_longest(nums: list[int], target: int) -> int:
    left = 0
    ans = 0
    win_sum = 0

    for right in range(len(nums)):
        win_sum += nums[right]

        while win_sum > target:
            win_sum -= nums[left]
            left += 1

        ans = max(ans, right-left+1)

    return ans

class TestSubarraySumLongest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(subarray_sum_longest([], 0), 0)

    def test_1(self):
        self.assertEqual(subarray_sum_longest([1, 2, 3, 4], 5), 2)

    def test_2(self):
        self.assertEqual(subarray_sum_longest([1, 2, 3, 4], 10), 4)

    def test_3(self):
        self.assertEqual(subarray_sum_longest([1, 2, 3, 4], 0), 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_longest(nums, target)
    print(res)