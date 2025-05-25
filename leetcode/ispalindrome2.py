#!/usr/bin/env python3

import sys
import unittest

# number: 680
# title: Valid Palindrome II
# url: https://leetcode.com/problems/valid-palindrome-ii/
# section: meta
# difficulty: easy
# tags: two pointers, string, greedy,  meta

# constraints
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.

# complexity
# run-time: O(n)
# space: O(1)
def check_palindrome(s: str, i: int, j: int) -> bool:
    while i < j:
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True

# solution: Leetcode recursive two pointers
# complexity
# run-time: O(n)
# space: O(1)
def ispalindrome2(s: str) -> bool:
    i = 0
    j = len(s)-1

    while i < j:
        if s[i] != s[j]:
            # fix i or j and check neighboring characters
            return check_palindrome(s, i, j-1) or check_palindrome(s, i+1, j)

        i += 1
        j -= 1

    return True

class TestIsPalindrome2(unittest.TestCase):
    def test1(self):
        s = "aba"
        self.assertTrue(ispalindrome2(s))

    def test2(self):
        s = "abca"
        self.assertTrue(ispalindrome2(s))

    def test3(self):
        s = "abc"
        self.assertFalse(ispalindrome2(s))

    def test4(self):
        s = "deeee"
        self.assertTrue(ispalindrome2(s))

    def test5(self):
        s = "cdbeeeabddddbaeedebdc"
        self.assertTrue(ispalindrome2(s))

    def test6(self):
        s = "eddboebddcaacddkbebdde"
        self.assertFalse(ispalindrome2(s))

    def test7(self):
        s = "ebcbbececabbacecbbcbe"
        self.assertTrue(ispalindrome2(s))

if __name__ == '__main__':
    sys.exit(unittest.main())
