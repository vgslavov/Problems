#!/usr/bin/env python3

import sys
import unittest

# number:
# section:
# difficulty: easy
# tags: recursion

# constraints
# 1 <= s.length <= 10^5
# s is list!
# s[i] is a printable ascii character.
# in-place

# solution: iterative
# run-time: O(n)
# space: O(1)
def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def reverse_helper(s, i, j):
    # base case
    if i >= j:
        return

    # swap in-place
    s[i], s[j] = s[j], s[i]

    return reverse_helper(s, i+1, j-1)

# solution: recursive
# run-time: O(n)
# space: O(1), why not O(n) due to recursion?
def reverse_string2(s):
    return reverse_helper(s, 0, len(s)-1)

class TestReverseString(unittest.TestCase):
    def test_empty(self):
        s = ''
        reverse_string(s)
        self.assertFalse(s)

    def test_empty2(self):
        s = ''
        reverse_string2(s)
        self.assertFalse(s)

    def test_1_1(self):
        s = ["h","e","l","l","o"]
        expected = ["o","l","l","e","h"]
        reverse_string(s)
        self.assertEqual(s, expected)

    def test_1_2(self):
        s = ["h","e","l","l","o"]
        expected = ["o","l","l","e","h"]
        reverse_string2(s)
        self.assertEqual(s, expected)

    def test_2_1(self):
        s = ["H","a","n","n","a","h"]
        expected = ["h","a","n","n","a","H"]
        reverse_string(s)
        self.assertEqual(s, expected)

    def test_2_2(self):
        s = ["H","a","n","n","a","h"]
        expected = ["h","a","n","n","a","H"]
        reverse_string2(s)
        self.assertEqual(s, expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
