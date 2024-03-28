#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 1000

# O(n)
def largest_unique_number(nums):
    d = defaultdict(int)

    for n in nums:
        d[n] += 1

    ans = -1
    for k,v in d.items():
        if v > 1:
            continue

        ans = max(ans, k)

    return ans

# TODO: use max+filter+lambda

class TestLargestUniqueNumber(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = -1
        self.assertEqual(largest_unique_number(nums), expected)

    def test_success(self):
        nums = [5,7,3,9,4,9,8,3,1]
        expected = 8
        self.assertEqual(largest_unique_number(nums), expected)

    def test_failure(self):
        nums = [9,9,8,8]
        expected = -1
        self.assertEqual(largest_unique_number(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
