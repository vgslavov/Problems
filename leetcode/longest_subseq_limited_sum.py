#!/usr/bin/env python3

import sys
import unittest

# number: 2389
# title: Longest Subsequence With Limited Sum
# url: https://leetcode.com/problems/longest-subsequence-with-limited-sum/
# difficulty: easy
# tags: array, binary search, greedy, sorting, prefix sum

# constraints
# n == nums.length
# m == queries.length
# 1 <= n, m <= 1000
# 1 <= nums[i], queries[i] <= 10^6

# solution: brute-force
# complexity
# run-time: O(n^2)
# space: O(n)
def longest_subseq_limited_sum(nums, queries):
    # optimization:
    # to maximize longest subseq, start w/ smaller numbers
    nums.sort()

    ans = []
    for i in range(len(queries)):
        sum = 0
        subseq = []
        for j in range(len(nums)):
            # optimization: break if sorted
            # continue otherwise
            if sum + nums[j] > queries[i]:
                break  
            elif sum + nums[j] == queries[i]:
                ans.append(len(subseq)+1)
                sum = 0
                subseq = []
                break

            sum += nums[j]
            subseq.append(nums[j])

        # ensure there are 0-sized queries:
        # len(ans) == len(queries)
        if subseq or len(ans) < i+1:
            ans.append(len(subseq))

    return ans if ans else [0]

# TODO: solve in O(log n), use binary search

class TestLongestSubseqLimitedSum(unittest.TestCase):
    def test_empty(self):
        nums = []
        queries = []
        expected = [0]
        self.assertEqual(longest_subseq_limited_sum(nums, queries), expected)

    def test1(self):
        nums = [4,5,2,1]
        queries = [3,10,21]
        expected = [2,3,4]
        self.assertEqual(longest_subseq_limited_sum(nums, queries), expected)

    def test2(self):
        nums = [2,3,4,5]
        queries = [1]
        expected = [0]
        self.assertEqual(longest_subseq_limited_sum(nums, queries), expected)

    def test3(self):
        nums = [624082]
        queries = [972985,564269,607119,693641,787608,46517,500857,140097]
        expected = [1,0,0,1,1,0,0,0]
        self.assertEqual(longest_subseq_limited_sum(nums, queries), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
