#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 771
# title: Jewels and Stones
# url: https://leetcode.com/problems/jewels-and-stones/
# difficulty: easy
# tags: string, hash table

# constraints
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.

# solution: dict
# complexity
# run-time: O(n+m)
# space: O(n)
def num_jewelsinstones(jewels, stones):
    d_j = defaultdict(int)

    for j in jewels:
        d_j[j] += 1

    count = 0

    for s in stones:
        if s in d_j:
            count += 1

    return count

# TODO: faster using bitmap?

class TestNumJewels(unittest.TestCase):
    def test_empty(self):
        jewels = ''
        stones = ''
        expected = 0
        self.assertEqual(num_jewelsinstones(jewels, stones), expected)

    def test_1(self):
        jewels = "aA"
        stones = "aAAbbbb"
        expected = 3
        self.assertEqual(num_jewelsinstones(jewels, stones), expected)

    def test_2(self):
        jewels = "z"
        stones = "ZZ"
        expected = 0
        self.assertEqual(num_jewelsinstones(jewels, stones), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
