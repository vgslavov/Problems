#!/usr/bin/env python3

import sys
import unittest

# number: 228
# title: Summary Ranges
# url: https://leetcode.com/problems/summary-ranges/
# section: intervals
# difficulty: easy
# tags: array, top 150

# constraints
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.
#
# Return the smallest sorted list of ranges that cover all the numbers in the
# array exactly.

# complexity
# run-time: O(n)
# space: O(n)
def summary_ranges(nums):
    if not nums:
        return None
    elif len(nums) == 1:
        return [str(nums[0])]

    ranges = []
    start = end = 0

    for i in range(len(nums)):
        # consecutive numbers
        if i < len(nums)-1 and nums[i+1] - nums[i] == 1:
            continue
        # a == b
        elif nums[i] - nums[start] == 0:
            ranges.append(str(nums[i]))
        # [a, b]
        else:
            ranges.append("{}->{}".format(nums[start], nums[i]))
        start = i+1

    return ranges

# TODO: faster?

class TestSummaryRange(unittest.TestCase):
    def test_empty(self):
        nums = None
        self.assertFalse(summary_ranges(nums))

    def test_single(self):
        nums = [7]
        self.assertEqual(summary_ranges(nums), [str(nums[0])])

    def test_range(self):
        nums = [1,2,3,4,5,6,7]
        expected = ["1->7"]
        self.assertEqual(summary_ranges(nums), expected)

    def test_even(self):
        nums = [0,1,2,4,5,7]
        expected = ["0->2","4->5","7"]
        self.assertEqual(summary_ranges(nums), expected)

    def test_odd(self):
        nums = [0,2,3,4,6,8,9]
        expected = ["0","2->4","6","8->9"]
        self.assertEqual(summary_ranges(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
