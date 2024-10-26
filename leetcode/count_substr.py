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
    def dp(i):
        # base case
        if i == 1:
            return 1

        ans = 0
        # recurrence relation
        for j in range(i):
            if ispalindrome(s, i, j):
                ans += dp(j) + 1

        return ans

    return sum(dp(i) for i in range(len(s)))

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
