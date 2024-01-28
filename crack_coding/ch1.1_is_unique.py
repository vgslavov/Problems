#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# set
def is_unique1(s):
    return len(set(s)) == len(s)

# set comprehension
def is_unique2(s):
    return len({char for char in s}) == len(s)

# dict
def is_unique3(s):
    d = defaultdict(int)
    for char in s:
        d[char] += 1

    return not len([k for k,v in d.items() if v > 1])

class TestIsUnique(unittest.TestCase):

    def test_empty(self):
        s = ''
        self.assertTrue(is_unique1(s))
        self.assertTrue(is_unique2(s))
        self.assertTrue(is_unique3(s))

    def test_unique(self):
        s = 'abcde'
        self.assertTrue(is_unique1(s))
        self.assertTrue(is_unique2(s))
        self.assertTrue(is_unique3(s))

    def test_notunique(self):
        s = 'abcded'
        self.assertFalse(is_unique1(s))
        self.assertFalse(is_unique2(s))
        self.assertFalse(is_unique3(s))

if __name__ == '__main__':
    sys.exit(unittest.main())
