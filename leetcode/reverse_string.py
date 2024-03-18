#!/usr/bin/env python3

import sys
import unittest

# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.

# O(n) time
# O(1) space
# in-place
def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

class TestReverseString(unittest.TestCase):
    def test_empty(self):
        s = ''
        reverse_string(s)
        self.assertFalse(s)

    def test_1(self):
        s = ["h","e","l","l","o"]
        expected = ["o","l","l","e","h"]
        reverse_string(s)
        self.assertEqual(s, expected)

    def test_2(self):
        s = ["H","a","n","n","a","h"]
        expected = ["h","a","n","n","a","H"]
        reverse_string(s)
        self.assertEqual(s, expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
