#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 5
# similar: 647
# title: Longest Palindromic Substring
# url: https://leetcode.com/problems/longest-palindromic-substring/
# section: meta
# difficulty: medium
# tags: meta, two pointers, string, dp, grind 75

# constraints
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def expand_center(s, left, right):
    ans = deque()

    while left >= 0 and right < len(s):
        # no match, stop
        if s[left] != s[right]:
            break

        # don't add itself
        if left == right:
            ans.append(s[left])
        else:
            ans.append(s[right])
            ans.appendleft(s[left])

        left -= 1
        right += 1

    return ''.join(ans)

# solution: expand from center
# complexity
# run-time: O(n^2)
# space: O(n)
def longest_palindromic_substr(s: str) -> str:
    ans = ""

    for i in range(len(s)):
        # check single letter 
        single = expand_center(s, i, i)

        # check double letter
        double = expand_center(s, i, i+1)

        ans = max([single, double, ans], key=len)

    return ans

# TODO: solve using DP

class TestLongestPalindromicSubstr(unittest.TestCase):
    def test_empty(self):
        s = ""
        self.assertFalse(longest_palindromic_substr(s))

    def test1(self):
        s = "babad"
        expected = "aba"
        self.assertEqual(longest_palindromic_substr(s), expected)

    def test2(self):
        s = "cbbd"
        expected = "bb"
        self.assertEqual(longest_palindromic_substr(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
