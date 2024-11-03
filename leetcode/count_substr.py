#!/usr/bin/env python3

from functools import cache
import sys
import unittest

# number: 647
# section: citadel
# difficulty: medium
# tags: two pointers, string, dp, citadel

# constraints
# 1 <= s.length <= 1000
# s consists of lowercase English letters.

def ispalindrome(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

# solution: brute-force
# complexity
# run-time: O(n^3), too slow: TLE
# space: O(1)
def count_substr(s: str) -> int:
    count = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            count += ispalindrome(s, i, j)

    return count

# solution: recursive top-down 1D DP using functools
# complexity
# run-time: O(n^2)
# space: O(n)
# TODO: finish
def count_substr2(s: str) -> int:
    @cache
    def dp(i, j):
        print(f"i:{i},j:{j}")

        # base case
        # single letter palindrome
        if i == j:
            return 1
        # be safe
        elif i > j or j > len(s)-1 or i > len(s)-1:
            return 0
        # 2-letter palindrome
        elif (j == i + 1) and (s[i] == s[j]):
            return 1

        # recurrence relation
        ans = 0
        for z in range(i, len(s)-1):
            if s[z] == s[z+1]:
                ans += 1

        print(f"s:{s},ans:{ans}")

        for z in range(i, len(s)-1):
            if s[i] == s[j]:
                return ans + dp(i+1, j-1) + 1
            else:
                return ans + dp(i+1, j-1)

    return dp(0, len(s)-1)

class TestCountSubstr(unittest.TestCase):
    def test_empty(self):
        s = ""
        expected = 0
        self.assertEqual(count_substr(s), expected)
        self.assertEqual(count_substr2(s), expected)

    def test_abc(self):
        s = "abc"
        expected = 3
        self.assertEqual(count_substr(s), expected)
        self.assertEqual(count_substr2(s), expected)

    def test_aaa(self):
        s = "aaa"
        expected = 6
        self.assertEqual(count_substr(s), expected)
        self.assertEqual(count_substr2(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
