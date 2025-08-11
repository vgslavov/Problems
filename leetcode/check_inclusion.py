#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 567
# similar: 438
# title: Permutation in String
# url: https://leetcode.com/problems/permutation-in-string/
# section: meta 
# difficulty: medium
# tags: hash table, two pointers, string, sliding window, meta

# constraints
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.

# solution: LeetCode solution of #438, sliding window + defaultdict
# complexity
# run-time: O(n)
# space: O(1) (only 26 letters per dict)
def check_inclusion(s1: str, s2: str) -> bool:
    # s1 cannot be longer than s2 and be a permutation of s2
    if len(s1) > len(s2):
        return False

    # count the frequency of each character in s1
    d1 = defaultdict(int)
    for c in s1:
        d1[c] += 1

    # sliding window counter
    win_d = defaultdict(int)
    left = 0

    for right in range(len(s2)):
        # count the frequency of each character in the current window
        win_d[s2[right]] += 1

        # window is smaller than s1
        if right - left + 1 < len(s1):
            continue

        # check if the current window is a permutation of s1
        if win_d == d1:
            return True

        # remove the leftmost character from the window
        if win_d[s2[left]] > 1:
            win_d[s2[left]] -= 1
        else:
            del win_d[s2[left]]

        # slide the window
        left += 1

    return False

class TestCheckInclusion(unittest.TestCase):
    def test_empty(self):
        s1 = ""
        s2 = ""
        expected = False
        self.assertEqual(check_inclusion(s1, s2), expected)

    def test_1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        expected = True
        self.assertEqual(check_inclusion(s1, s2), expected)

    def test_2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        expected = False
        self.assertEqual(check_inclusion(s1, s2), expected)

    def test_3(self):
        s1 = "abc"
        s2 = "ccccbbbbaaaa"
        expected = False
        self.assertEqual(check_inclusion(s1, s2), expected)

    def test_4(self):
        s1 = "abc"
        s2 = "abccba"
        expected = True
        self.assertEqual(check_inclusion(s1, s2), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())