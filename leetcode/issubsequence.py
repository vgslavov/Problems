#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.

# O(n)
def issubsequence(s, t):
    i = j = 0

    while i < len(t) and j < len(s):
        if s[j] == t[i]:
            j += 1

        i += 1

    return len(s) == i

# TODO: extra
# Suppose there are lots of incoming s, say s_1, s2_, ..., s_k where k >= 10^9,
# and # you want to check one by one to see if t has its subsequence. In this
# scenario, how would you change your code?

class TestIssubsequence(unittest.TestCase):
    def test_empty(self):
        s = ''
        t = ''
        self.assertTrue(issubsequence(s, t))

    def test_true(self):
        s = 'abc'
        t = 'ahbgdc'
        self.assertTrue(issubsequence(s, t))

    def test_false1(self):
        s = 'axc'
        t = 'ahbgdc'
        self.assertFalse(issubsequence(s, t))

    def test_false2(self):
        s = 'acb'
        t = 'ahbgdc'
        self.assertFalse(issubsequence(s, t))

if __name__ == '__main__':
    sys.exit(unittest.main())
