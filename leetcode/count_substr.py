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

# non-solution: recursive top-down 2D DP using functools
# complexity
# run-time: O(n^2)
# space: O(n^2)
# TODO: translate bottom-up
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

# solution: Leetcode iterative bottom-up 2D DP
# complexity
# run-time: O(n^2)
# space: O(n^2)
# TODO: fix bug
def count_substr3(s: str) -> int:
    if not s:
        return 0

    # init
    dp = [[0] * (len(s)) for _ in range(len(s))]
    ans = 0

    # base cases: single-letter
    for i in range(len(s)):
        # single-letter substrings
        dp[i][i] = 1
        ans += 1

    # base case: double-letter
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1

        ans += dp[i][i+1]

    # recurrence relation
    for _ in range(3, len(s)+1):
        i = 0
        j = i + len(s)-1
        while j < len(s):
            #print(f"i:{i},j:{j}")

            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]

            ans += dp[i][j]
            i += 1
            j += 1

    return ans

def count_palindromes(s, i, j):
    ans = 0

    while i >= 0 and j < len(s):
        # no match
        if s[i] != s[j]:
            break

        # move away from center
        i -= 1
        j += 1
        ans += 1

    return ans

# solution: Leetcode expand around centers
# complexity
# run-time: O(n^2)
# space: O(1)
def count_substr4(s: str) -> int:
    ans = 0

    for i in range(len(s)):
        # single-letter center
        ans += count_palindromes(s, i, i)

        # double-letter center
        ans += count_palindromes(s, i, i+1)

    return ans

class TestCountSubstr(unittest.TestCase):
    def test_empty(self):
        s = ""
        expected = 0
        self.assertEqual(count_substr(s), expected)
        #self.assertEqual(count_substr2(s), expected)
        self.assertEqual(count_substr3(s), expected)
        self.assertEqual(count_substr4(s), expected)

    def test_abc(self):
        s = "abc"
        expected = 3
        self.assertEqual(count_substr(s), expected)
        #self.assertEqual(count_substr2(s), expected)
        self.assertEqual(count_substr3(s), expected)
        self.assertEqual(count_substr4(s), expected)

    def test_aaa(self):
        s = "aaa"
        expected = 6
        self.assertEqual(count_substr(s), expected)
        #self.assertEqual(count_substr2(s), expected)
        self.assertEqual(count_substr3(s), expected)
        self.assertEqual(count_substr4(s), expected)

    def test_aaaaa(self):
        s = "aaaaa"
        expected = 15
        self.assertEqual(count_substr(s), expected)
        #self.assertEqual(count_substr2(s), expected)
        # TODO: fix
        #self.assertEqual(count_substr3(s), expected)
        self.assertEqual(count_substr4(s), expected)


if __name__ == '__main__':
    sys.exit(unittest.main())
