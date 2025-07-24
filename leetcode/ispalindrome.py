#!/usr/bin/env python3

import sys
import unittest

# number: 125
# title: Valid Palindrome
# url: https://leetcode.com/problems/valid-palindrome/
# section: two pointers
# difficulty: easy
# tags: two pointers, string, top 150, meta, grind 75

# constraints
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

# solution: Pythonic & slow
# complexity
# run-time: O(n)
# space: O(n)
def ispalindrome(s):
    alnum = ''.join([c.lower() for c in s if c.isalnum()])

    return alnum == alnum[::-1]

# solution: two pointers
# complexity
# run-time: O(n)
# space: O(1)
def ispalindrome2(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True

# TODO: faster?

class TestIspalindrome(unittest.TestCase):
    def test_empty(self):
        s = ' '
        self.assertTrue(ispalindrome(s))
        self.assertTrue(ispalindrome2(s))

    def test_true(self):
        s = 'A man, a plan, a canal: Panama'
        self.assertTrue(ispalindrome(s))
        self.assertTrue(ispalindrome2(s))

    def test_false(self):
        s = 'race a car'
        self.assertFalse(ispalindrome(s))
        self.assertFalse(ispalindrome2(s))

    def test_num(self):
        s = '0P'
        self.assertFalse(ispalindrome(s))
        self.assertFalse(ispalindrome2(s))

if __name__ == '__main__':
    sys.exit(unittest.main())
