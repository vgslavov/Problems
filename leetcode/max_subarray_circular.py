#!/usr/bin/env python3

import math
import sys
import unittest

# number: 918
# section: Kadane's algo
# difficulty: medium
# tags: array, divide & conquer, dp, queue, monotonic queue

# constraints
# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# return the maximum possible sum of a *non-empty* subarray of nums

# solution: Kadane's algo + calc total/min sum
# complexity
# run-time: O(n)
# space: O(1)
def max_subarray_circular(nums):
    if not nums:
        return 0

    total_sum = curr_max_sum = curr_min_sum = 0
    max_sum = -math.inf
    min_sum = math.inf

    for n in nums:
        # calculate max sum
        curr_max_sum = max(n, curr_max_sum+n)
        max_sum = max(curr_max_sum, max_sum)

        # calculate min sum
        curr_min_sum = min(n, curr_min_sum+n)
        min_sum = min(curr_min_sum, min_sum)

        # calculate total sum
        total_sum += n

    # total_sum == min_sum when all n < 0
    return max_sum if total_sum == min_sum else max(max_sum, total_sum-min_sum)

# non-solution: Kadane's algo + circular indices
# complexity
# run-time:
# space:
def max_subarray_circular_bad(nums):
    if not nums:
        return 0

    curr_sum = 0
    max_sum = -math.inf
    n = len(nums)

    for i in range(-1, n):
        next_i = (i+1) % n
        print(next_i)
        curr_sum = max(nums[next_i], curr_sum+nums[next_i])
        max_sum = max(curr_sum, max_sum)

    return max_sum

class TestMaxSubarrayCircular(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = 0
        self.assertEqual(max_subarray_circular(nums), expected)

    def test_middle1(self):
        nums = [1,-2,3,-2]
        expected = 3
        self.assertEqual(max_subarray_circular(nums), expected)

    def test_middle2(self):
        nums = [-3,-2,-3]
        expected = -2
        self.assertEqual(max_subarray_circular(nums), expected)

    def test_split(self):
        nums = [5,-3,5]
        expected = 10
        self.assertEqual(max_subarray_circular(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
