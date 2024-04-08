#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# 1 <= ransom_note.length, magazine.length <= 10^5
# ransom_note and magazine consist of lowercase English letters.

# O(n): slow
def can_construct1(ransom_note, magazine):
    letters = defaultdict(int)

    for c in magazine:
        letters[c] += 1

    for c in ransom_note:
        if c not in letters or not letters[c]:
            return False

        letters[c] -= 1

    return True

# TODO: faster
def can_construct2(ransom_note, magazine):
    pass

class TestCanConstruct(unittest.TestCase):

    def test_empty(self):
        note = ''
        mag = ''
        self.assertTrue(can_construct1(note, mag))

    def test_false1(self):
        note = "a"
        mag = "b"
        self.assertFalse(can_construct1(note, mag))

    def test_false2(self):
        note = "aa"
        mag = "ab"
        self.assertFalse(can_construct1(note, mag))

    def test_true(self):
        note = "aa"
        mag = "aab"
        self.assertTrue(can_construct1(note, mag))

if __name__ == '__main__':
    sys.exit(unittest.main())
