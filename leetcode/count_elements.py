#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

# O(n)
def count_elements(nums):
    d = defaultdict(int)

    for num in nums:
        d[num] += 1

    count = 0
    for num in nums:
        if num + 1 in d and d[num+1]:
            count += 1

    return count

# TODO: faster O(n)?

class TestCountElements(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = 0
        self.assertEqual(count_elements(nums), expected)

    def test_1(self):
        nums = [1,2,3]
        expected = 2
        self.assertEqual(count_elements(nums), expected)

    def test_2(self):
        nums = [1,1,3,3,5,5,7,7]
        expected = 0
        self.assertEqual(count_elements(nums), expected)

    def test_3(self):
        nums = [1,1,2]
        expected = 2
        self.assertEqual(count_elements(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
