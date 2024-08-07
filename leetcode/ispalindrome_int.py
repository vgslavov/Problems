#!/usr/bin/env python3

import sys
import unittest

# number:
# section: math
# difficulty: easy
# tags: math

# constraints
# 2^31 <= x <= 2^31 - 1

# solution: str & Pythonic slicing
# complexity
# run-time: O(n)?
# space: O(1)
def ispalindrome(num):
    s = str(num)

    return s == s[::-1]

# solution: str & two pointers
# complexity
# run-time: O(n), faster
# space: O(1)
def ispalindrome2(num):
    s = str(num)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

# TODO: don't convert to str

class TestIsPalindrome(unittest.TestCase):
    def test_0(self):
        num = 0
        self.assertTrue(ispalindrome(num))
        self.assertTrue(ispalindrome2(num))

    def test_121(self):
        num = 121
        self.assertTrue(ispalindrome(num))
        self.assertTrue(ispalindrome2(num))

    def test_ve121(self):
        num = -121
        self.assertFalse(ispalindrome(num))
        self.assertFalse(ispalindrome2(num))

    def test_10(self):
        num = 10
        self.assertFalse(ispalindrome(num))
        self.assertFalse(ispalindrome2(num))

if __name__ == '__main__':
    sys.exit(unittest.main())
