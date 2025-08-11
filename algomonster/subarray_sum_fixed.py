#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: sliding fixed window

# solution: sliding fixed window
# complexity:
# run-time: O(n)
# space: O(1)
def subarray_sum_fixed(nums: list[int], k: int) -> int:
    ans = sum(nums[:k])
    curr = ans

    for right in range(k, len(nums)):
        left = right - k
        curr -= nums[left]
        curr += nums[right]
        ans = max(ans, curr)
        
    return ans

class TestSubarraySumFixed(unittest.TestCase):

    def test_example_cases(self):
        self.assertEqual(subarray_sum_fixed([1, 2, 3, 4, 5], 3), 12)
        self.assertEqual(subarray_sum_fixed([5, 4, 3, 2, 1], 2), 9)
        self.assertEqual(subarray_sum_fixed([1, 1, 1, 1, 1], 5), 5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_fixed(nums, k)
    print(res)