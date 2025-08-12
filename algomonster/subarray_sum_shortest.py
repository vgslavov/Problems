#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: sliding window, shortest

# solution: sliding window
# complexity:
# run-time: O(n)
# space: O(1)
def subarray_sum_shortest(nums: list[int], target: int) -> int:
    left = win_sum = 0
    ans = len(nums)

    for right in range(len(nums)):
        win_sum += nums[right]

        while win_sum >= target:
            ans = min(ans, right-left+1)
            win_sum -= nums[left]
            left += 1
            
    return ans

class TestSubarraySumShortest(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(subarray_sum_shortest([1, 7, 1, 7, 3, 0, 2, 5], 10), 2)
        self.assertEqual(subarray_sum_shortest([1, 6, 8], 8), 1)
        self.assertEqual(subarray_sum_shortest([6, 6, 6, 6, 6, 6, 6], 19), 4)
        self.assertEqual(subarray_sum_shortest([1, 1, 1], 3), 3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_shortest(nums, target)
    print(res)