#!/usr/bin/env python3

import itertools
import sys
import unittest

# number: 1079
# title: Letter Tile Possibilities
# url: https://leetcode.com/problems/letter-tile-possibilities/
# section: assessments
# difficulty: medium
# tags: hash table, string, backtracking, counting, google

# constraints
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

# solution: itertools
# complexity
# run-time: O(2^n)
# space: O(n!)
def num_tiles(tiles: str) -> int:
    n = 0

    for i in range(1, len(tiles)+1):
        #print(f"i:{i}")
        n += len(set(sorted(list(itertools.permutations(list(tiles),i)))))

    return n

# TODO: calc permutations manually

class TestNumTiles(unittest.TestCase):
    def test_empty(self):
        s = ''
        expected = 0
        self.assertEqual(num_tiles(s), expected)

    def test_aab(self):
        s = "AAB"
        expected = 8
        self.assertEqual(num_tiles(s), expected)

    def test_aaabbc(self):
        s = "AAABBC"
        expected = 188
        self.assertEqual(num_tiles(s), expected)

    def test_v(self):
        s = "V"
        expected = 1
        self.assertEqual(num_tiles(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
