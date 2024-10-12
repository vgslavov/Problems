#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 575
# section: assessments
# difficulty: easy
# tags: array, hash table, microsoft

# constraints
# n == candyType.length
# 2 <= n <= 10^4
# n is even.
# -10^5 <= candyType[i] <= 10^5

# solution: dict
# complexity
# run-time: O(n)
# space: O(n)
def distribute_candies(candyType):
    counts = defaultdict(int)

    for c in candyType:
        counts[c] += 1

    return min(len(counts.keys()), len(candyType)//2)

# solution: set
# complexity
# run-time: O(n)
# space: O(n)
def distribute_candies2(candyType):
    return min(len(set(candyType)), len(candyType)//2)

class TestDistributeCandies(unittest.TestCase):
    def test1(self):
        types = [1,1,2,2,3,3]
        expected = 3
        self.assertEqual(distribute_candies(types), expected)
        self.assertEqual(distribute_candies2(types), expected)

    def test2(self):
        types = [1,1,2,3]
        expected = 2
        self.assertEqual(distribute_candies(types), expected)
        self.assertEqual(distribute_candies2(types), expected)

    def test3(self):
        types = [6,6,6,6]
        expected = 1
        self.assertEqual(distribute_candies(types), expected)
        self.assertEqual(distribute_candies2(types), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
