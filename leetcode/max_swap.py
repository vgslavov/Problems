#!/usr/bin/env python3

import sys
import unittest

# number: 670
# title: Maximum Swap
# url: https://leetcode.com/problems/maximum-swap/
# section: meta
# difficulty: medium
# tags: math, greedy, meta

# constraints
# 1 <= num <= 10^8

# non-solution: brute force
# complexity
# run-time: O(n^3), TLE
# space: O(n)
def max_swap(num: int) -> int:
    num_s = str(num)
    # given number is min
    ans = num

    # use str for iteration
    for i in range(len(num_s)):
        for j in range(i+1, len(num_s)):
            # use list for swapping
            num_l = list(num_s)
            num_l[i], num_l[j] = num_l[j], num_l[i]
            curr = int(''.join(num_l))
            ans = max(ans, curr)

    return ans

# solution: LeetCode greedy
# complexity
# run-time: O(n)
# space: O(n)
# TODO: understand better
def max_swap2(num: int) -> int:
    # need only a list, no str
    num_l = list(str(num))

    # index of max element b/w i & end
    max_idx = [0] * len(num_l)
    # max of 1 is last
    max_idx[-1] = len(num_l)-1

    # revese pass: find max b/w i & end
    for i in reversed(range(len(num_l)-1)):
        max_idx[i] = i if num_l[i] > num_l[max_idx[i+1]] else max_idx[i+1]

    # forward pass: swap with max
    for i in range(len(num_l)):
        if int(num_l[i]) >= int(num_l[max_idx[i]]):
            continue

        # swap current with the max to the right of it
        num_l[i], num_l[max_idx[i]] = num_l[max_idx[i]], num_l[i]
        return int(''.join(num_l))
    
    # no swaps were performed
    return num

class TestMaxSwap(unittest.TestCase):
    def test_example1(self):
        num = 2736
        expected = 7236
        self.assertEqual(max_swap(num), expected)
        self.assertEqual(max_swap2(num), expected)

    def test_example2(self):
        num = 9973
        expected = 9973
        self.assertEqual(max_swap(num), expected)
        self.assertEqual(max_swap2(num), expected)

    def test_single_digit(self):
        num = 5
        expected = 5
        self.assertEqual(max_swap(num), expected)
        self.assertEqual(max_swap2(num), expected)

    def test_two_digits(self):
        num = 21
        expected = 21
        self.assertEqual(max_swap(num), expected)
        self.assertEqual(max_swap2(num), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())