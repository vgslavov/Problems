#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 383
# title: Ransom Note
# url: https://leetcode.com/problems/ransom-note/
# section: hashmap
# difficulty: easy
# tags: hash table, string, counting, top 150, grind 75

# constraints
# 1 <= ransom_note.length, magazine.length <= 10^5
# ransom_note and magazine consist of lowercase English letters.

# complexity
# run-time: O(m+n), slow
# space: O(m)
def can_construct(ransom_note, magazine):
    letters = defaultdict(int)

    for c in magazine:
        letters[c] += 1

    for c in ransom_note:
        if c not in letters or not letters[c]:
            return False

        letters[c] -= 1

    return True

# TODO: faster?

class TestCanConstruct(unittest.TestCase):

    def test_empty(self):
        note = ''
        mag = ''
        self.assertTrue(can_construct(note, mag))

    def test_false1(self):
        note = "a"
        mag = "b"
        self.assertFalse(can_construct(note, mag))

    def test_false2(self):
        note = "aa"
        mag = "ab"
        self.assertFalse(can_construct(note, mag))

    def test_true(self):
        note = "aa"
        mag = "aab"
        self.assertTrue(can_construct(note, mag))

if __name__ == '__main__':
    sys.exit(unittest.main())
