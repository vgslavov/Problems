#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

# TODO: WIP
def longest_substr(s):
    d = defaultdict(int)

    left = ans = 0
    ans_str = sub_str = ''

    for right in range(len(s)):
        if s[right] in d:
            if len(sub_str) > len(ans_str):
                ans_str = sub_str

            left += 1

        d[s[right]] += 1
        sub_str += s[right]

        ans = max(len(ans_str), len(sub_str))

    return ans

class TestLongestSubstr(unittest.TestCase):
    def test_empty(self):
        s = ''
        expected = 0
        self.assertEqual(len_longest_substr(s), expected)

    def test_space(self):
        s = ' '
        expected = 1
        self.assertEqual(len_longest_substr(s), expected)

    def test_1(self):
        s = "abcabcbb"
        expected = 3
        self.assertEqual(len_longest_substr(s), expected)

    def test_2(self):
        s = "bbbbb"
        expected = 1
        self.assertEqual(len_longest_substr(s), expected)

    def test_3(self):
        s = "pwwkew"
        expected = 3
        self.assertEqual(len_longest_substr(s), expected)

    def test_4(self):
        s = "dvdf"
        expected = 3
        self.assertEqual(len_longest_substr(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
