#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.

# bad: matches out of order 
def issubsequence1(s, t):
    d = defaultdict(int)

    for c in t:
        d[c] += 1

    for c in s:
        if c not in d:
            return False

    return True

# O(n): slow?
def issubsequence2(s, t):
    i = j = match = 0

    while i < len(t) and j < len(s):
        if s[j] != t[i]:
            i += 1
        elif s[j] == t[i]:
            match += 1
            i += 1
            j += 1

    return match == len(s)

# TODO: O(n)
def issubsequence3(s, t):
    pass

# TODO: extra
# Suppose there are lots of incoming s, say s_1, s2_, ..., s_k where k >= 10^9,
# and # you want to check one by one to see if t has its subsequence. In this
# scenario, how would you change your code?

class TestIssubsequence(unittest.TestCase):
    def test_empty(self):
        s = ''
        t = ''
        self.assertTrue(issubsequence2(s, t))

    def test_true(self):
        s = 'abc'
        t = 'ahbgdc'
        self.assertTrue(issubsequence2(s, t))

    def test_false1(self):
        s = 'axc'
        t = 'ahbgdc'
        self.assertFalse(issubsequence2(s, t))

    def test_false2(self):
        s = 'acb'
        t = 'ahbgdc'
        self.assertFalse(issubsequence2(s, t))

if __name__ == '__main__':
    sys.exit(unittest.main())
