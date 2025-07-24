#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 242
# title: Valid Anagram
# url: https://leetcode.com/problems/valid-anagram/
# section: hashmap
# difficulty: easy
# tags: hash table, string, sorting, top 150, grind 75

# constraints
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

# complexity: dict
# run-time: O(n+m)
# space: O(n)
def isanagram(s, t):
    if len(s) != len(t):
        return False

    count = defaultdict(int)

    for c in s:
        count[c] += 1

    for c in t:
        if c in count and count[c]:
            count[c] -= 1
        else:
            return False

    return True

# solution: sort
# complexity
# run-time: O(n*log n)
# space: O(1)
def isanagram2(s, t):
    if len(s) != len(t):
        return False

    return ''.join(sorted(s)) == ''.join(sorted(t))

# TODO: extra
# What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?

class TestIsAnagram(unittest.TestCase):
    def test_empty(self):
        s = ''
        t = ''
        self.assertTrue(isanagram(s, t))
        self.assertTrue(isanagram2(s, t))

    def test_true(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(isanagram(s, t))
        self.assertTrue(isanagram2(s, t))

    def test_false(self):
        s = "rat"
        t = "car"
        self.assertFalse(isanagram(s, t))
        self.assertFalse(isanagram2(s, t))

    def test_false_short(self):
        s = "ab"
        t = "a"
        self.assertFalse(isanagram(s, t))
        self.assertFalse(isanagram2(s, t))

if __name__ == '__main__':
    sys.exit(unittest.main())
