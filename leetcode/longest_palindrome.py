#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 409
# title: Longest Palindrome
# url: https://leetcode.com/problems/longest-palindrome/
# difficulty: easy

# constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

# solution: defaultdict
# complexity:
# run-time: O(n)
# space: O(52) ~ O(1)
def longest_palindrome(s: str) -> int:
    counts = defaultdict(int)

    for c in s:
        counts[c] += 1

    ans = 0
    has_odd = False

    for v in counts.values():
        # even: count all
        if v % 2 == 0:
            ans += v
        # odd: subtract 1 but add it later
        else:
            ans += v-1
            has_odd = True

    # if 1 odd, count for the center of the palindrome
    if has_odd:
        return ans+1

    return ans

class TestLongestPalindrome(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_palindrome("abccccdd"), 7)
        self.assertEqual(longest_palindrome("a"), 1)
        self.assertEqual(longest_palindrome("aa"), 2)
        self.assertEqual(longest_palindrome("aaa"), 3)
        self.assertEqual(longest_palindrome("abc"), 1)
        self.assertEqual(longest_palindrome("bananas"), 5)

    def test_empty_string(self):
        self.assertEqual(longest_palindrome(""), 0)

    def test_all_same_characters(self):
        self.assertEqual(longest_palindrome("aaaaaa"), 6)

    def test_mixed_case(self):
        self.assertEqual(longest_palindrome("AaBbCc"), 1)

if __name__ == "__main__":
    sys.exit(unittest.main())