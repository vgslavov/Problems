#!/usr/bin/env python3

import sys
import unittest

# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.

# O(n): slow
def isisomorphic(s, t):
    if len(s) != len(t):
        return False

    s2t = {}
    t2s = {}
    for i in range(len(t)):
        if s[i] not in s2t:
            s2t[s[i]] = t[i]
        elif s2t[s[i]] != t[i]:
            return False

        if t[i] not in t2s:
            t2s[t[i]] = s[i]
        elif t2s[t[i]] != s[i]:
            return False

    return True

# TODO: faster
def isisomorphic2(s, t):
    pass

class TestIsIsomorphic(unittest.TestCase):
    def test_empty(self):
        s = ''
        t = ''
        self.assertTrue(isisomorphic(s, t))

    def test_true1(self):
        s = "egg"
        t = "add"
        self.assertTrue(isisomorphic(s, t))

    def test_true1(self):
        s = "egg"
        t = "add"
        self.assertTrue(isisomorphic(s, t))

    def test_true2(self):
        s = "paper"
        t = "title"
        self.assertTrue(isisomorphic(s, t))

    def test_false1(self):
        s = "foo"
        t = "bar"
        self.assertFalse(isisomorphic(s, t))

    def test_false2(self):
        s = "badc"
        t = "baba"
        self.assertFalse(isisomorphic(s, t))

    def test_false3(self):
        s = "egcd"
        t = "adfd"
        self.assertFalse(isisomorphic(s, t))

if __name__ == '__main__':
    sys.exit(unittest.main())
