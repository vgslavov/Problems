#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number 3:
# section: sliding window
# difficulty: medium
# tags: hash table, string, sliding window, top 150

# constraints
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# w/o repeating chars

# solution: dict
# complexity
# run-time: O(n)
# space: O(n)
# TODO: fix?
def longest_substr(s):
    d = defaultdict(int)

    sub_str = ''
    ans = ''
    for c in s:
        if c in d:
            if len(sub_str) > len(ans):
                ans = sub_str

            sub_str = ''
            d = defaultdict(int)

        sub_str += c
        d[c] += 1

    print("ans:{}, sub_str:{}".format(ans, sub_str))

    return max(len(ans), len(sub_str))

# solution: sliding window
# complexity
# run-time: O(n)
# space: O(n)
# TODO: finish, attempted
def longest_substr2(s):
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
        self.assertEqual(longest_substr(s), expected)

    def test_space(self):
        s = ' '
        expected = 1
        self.assertEqual(longest_substr(s), expected)

    def test_1(self):
        s = "abcabcbb"
        expected = 3
        self.assertEqual(longest_substr(s), expected)

    def test_2(self):
        s = "bbbbb"
        expected = 1
        self.assertEqual(longest_substr(s), expected)

    def test_3(self):
        s = "pwwkew"
        expected = 3
        self.assertEqual(longest_substr(s), expected)

    def test_4(self):
        s = "dvdf"
        expected = 3
        self.assertEqual(longest_substr(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
