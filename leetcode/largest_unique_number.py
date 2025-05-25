#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 1133
# title: Largest Unique Number
# url: https://leetcode.com/problems/largest-unique-number/
# section: hash table
# difficulty: easy
# tags: hash table, array, sorting

# constraints
# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 1000

# solution: dict 
# complexity
# run-time: O(n)
# space: O(n)
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

# solution: dict + Pythonic filter & max
# complexity
# run-time: O(n)
# space: O(n)
def largest_unique_number2(nums):
    d = defaultdict(int)

    for n in nums:
        d[n] += 1

    # convert to list to prevent passing empty arg to max()
    filtered = list(filter(lambda x: x[1] == 1, d.items()))

    return max(filtered)[0] if filtered else -1

class TestLargestUniqueNumber(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = -1
        self.assertEqual(largest_unique_number(nums), expected)
        self.assertEqual(largest_unique_number2(nums), expected)

    def test_success(self):
        nums = [5,7,3,9,4,9,8,3,1]
        expected = 8
        self.assertEqual(largest_unique_number(nums), expected)
        self.assertEqual(largest_unique_number2(nums), expected)

    def test_failure(self):
        nums = [9,9,8,8]
        expected = -1
        self.assertEqual(largest_unique_number(nums), expected)
        self.assertEqual(largest_unique_number2(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
