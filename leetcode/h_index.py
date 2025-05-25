#!/usr/bin/env python3

import sys
import unittest

# number: 274
# title: H-Index
# url: https://leetcode.com/problems/h-index/
# section: array / string
# difficulty: medium
# tags: array, sorting, couting sort, top 150

# constraints
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

# solution: Leetcode sorting
# complexity
# run-time: O(n*log n)
# space: O(1)
def h_index(citations) -> int:
    # descending order of citations
    citations.sort(reverse=True)

    i = 0
    # keep going until we find a citation that is less than the index
    while i < len(citations) and citations[i] > i:
        i += 1

    return i

# TODO: implement counting sort solution

class TestHIndex(unittest.TestCase):
    def test_empty(self):
        citations = []
        expected = 0
        self.assertEqual(h_index(citations), expected)

    def test_3(self):     
        citations = [3,0,6,1,5]
        expected = 3
        self.assertEqual(h_index(citations), expected)

    def test_0(self):
        citations = [0]
        expected = 0
        self.assertEqual(h_index(citations), expected)

    def test_1(self):
        citations = [1]
        expected = 1
        self.assertEqual(h_index(citations), expected)

    def test_100(self):
        citations = [100]
        expected = 1
        self.assertEqual(h_index(citations), expected)

    def test_1_1(self):
        citations = [1,1]
        expected = 1
        self.assertEqual(h_index(citations), expected)

    def test_1_3_1(self):
        citations = [1,3,1]
        expected = 1
        self.assertEqual(h_index(citations), expected)

    def test_0_0_2(self):
        citations = [0,0,2]
        expected = 1
        self.assertEqual(h_index(citations), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())