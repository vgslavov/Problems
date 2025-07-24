#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 3
# title: Longest Substring Without Repeating Characters
# url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# section: sliding window
# difficulty: medium
# tags: hash table, string, sliding window, top 150, meta, grind 75

# constraints
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# w/o repeating chars

# solution: sliding window + dict
# complexity
# run-time: O(n)
# space: O(n)
def longest_substr(s):
    if len(s) == 1:
        return 1

    # key: char, value: index in s
    d = {}
    left = ans = 0
    slist = list(s)

    for right in range(len(slist)):
        # found duplicate
        if slist[right] in d:
            prev_idx = d[slist[right]]
            sub_start = min(left, prev_idx)
            sub_end = max(left, prev_idx)

            for i in range(sub_start, sub_end):
                if slist[i] in d:
                    del d[slist[i]]

            # decrease window
            left += abs(left - prev_idx) + 1

        # save index of char at window end
        d[slist[right]] = right

        # d always contains chars within current window
        ans = max(ans, len(d))

        #print(f"left:{left},right:{right},ans:{ans},d:{d}")

    return ans

# solution: sliding window + dict
# complexity
# run-time: O(n), faster
# space: O(n)
def longest_substr2(s):
    ans = 0
    left = 0
    counts = defaultdict(int)

    for right in range(len(s)):
        counts[s[right]] += 1

        while counts[s[right]] > 1:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]

            left += 1

        ans = max(ans, right-left+1)

    return ans

class TestLongestSubstr(unittest.TestCase):
    def test_empty(self):
        s = ''
        expected = 0
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

    def test_space(self):
        s = ' '
        expected = 1
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

    def test_1(self):
        s = "abcabcbb"
        expected = 3
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

    def test_2(self):
        s = "bbbbb"
        expected = 1
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

    def test_3(self):
        s = "pwwkew"
        expected = 3
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

    def test_4(self):
        s = "dvdf"
        expected = 3
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

    def test_5(self):
        s = "au"
        expected = 2
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

    def test_6(self):
        s = "tmmzuxt"
        expected = 5
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

    def test_7(self):
        s = "bpfbhmipx"
        expected = 7
        self.assertEqual(longest_substr(s), expected)
        self.assertEqual(longest_substr2(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
