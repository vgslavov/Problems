#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 238
# section: array/string
# difficulty: medium
# tags: array, prefix sum, top 150, meta

# constraints
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.

# solution: prefix sum + deque + two pointers
# complexity
# run-time: O(n), slow!
# space: O(n)
def product_except_self(nums):
    if not nums:
        return []

    prefix1 = [1]
    prefix2 = deque([nums[-1]])
    neg_count = 0

    if nums[0] < 0:
        neg_count += 1

    # fwd prefix sum
    for i in range(1, len(nums)):
        if nums[i] < 0:
            neg_count += 1
        prefix1.append(prefix1[-1] * nums[i-1])

    #print("neg_count:{}".format(neg_count))
    #print("prefix1:{}".format(prefix1))

    # backward prefix sum
    for i in reversed(range(len(nums)-2)):
        prefix2.appendleft(prefix2[0] * nums[i+1])

    #print("prefix2:{}".format(prefix2))

    # odd number of negative signs
    isneg = neg_count % 2 != 0
    i = j = 0

    while i < len(prefix1) and j < len(prefix2):
        tmp = nums[i]
        nums[i] = prefix1[i] * prefix2[j]

        # multiplication by 0 loses - signs
        if tmp == 0 and isneg and nums[i] > 0:
            nums[i] *= -1

        i += 1
        j += 1

    # TODO: use extend?

    while i < len(prefix1):
        nums[i] = prefix1[i]
        i += 1

    while j < len(prefix2):
        nums[j] = prefix2[j]
        j += 1

    return nums

# TODO: refactor & solve w/ O(1) space

class TestProductExceptSelf(unittest.TestCase):
    def test_empty(self):
        nums = []
        expected = []
        self.assertEqual(product_except_self(nums), expected)

    def test_1(self):
        nums = [1,2,3,4]
        expected = [24,12,8,6]
        self.assertEqual(product_except_self(nums), expected)

    def test_2(self):
        nums = [-1,1,0,-3,3]
        expected = [0,0,9,0,0]
        self.assertEqual(product_except_self(nums), expected)

    def test_3(self):
        nums = [1,-1]
        expected = [-1,1]
        self.assertEqual(product_except_self(nums), expected)

    def test_4(self):
        nums = [9,0,-2]
        expected = [0,-18,0]
        self.assertEqual(product_except_self(nums), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
