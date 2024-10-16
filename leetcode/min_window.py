#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number:
# section: meta
# difficulty:
# tags: meta

# constraints
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.

# solution: sliding window + dict
# complexity
# run-time: O(n+m)
# space: O(n)
def min_window(s: str, t: str) -> str:
    counts = defaultdict(int)

    for c in t:
        counts[c] += 1

    left = matched = 0
    ans = ""

    for right in range(len(s)):
        #print(f"left:{left},right:{right},ans:{ans}")

        if s[right] in counts:
            # how many chars in window match in t
            matched += 1

        # cmp to len(t), not len(counts): t can have dupes!
        if matched < len(t):
            continue

        # slide left side of window
        while left < len(s) and s[left] not in counts:
            left += 1

        # we have a winner!
        print(f"ans:{ans},matched:{s[left:right+1]}")
        if not ans or len(ans) >= len(s[left:right+1]):
            ans = s[left:right+1]

        # continue sliding the window
        left += 1
        matched -= 1

    return ans

class TestMinWindow(unittest.TestCase):
    def test_empty(self):
        s = ""
        t = ""
        expected = ""
        self.assertEqual(min_window(s, t), expected)

    def test1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        self.assertEqual(min_window(s, t), expected)

    def test2(self):
        s = "a"
        t = "a"
        expected = "a"
        self.assertEqual(min_window(s, t), expected)

    def test3(self):
        s = "a"
        t = "aa"
        expected = ""
        self.assertEqual(min_window(s, t), expected)

    def test4(self):
        s = "a"
        t = "b"
        expected = ""
        self.assertEqual(min_window(s, t), expected)

    def test5(self):
        s = "cabwefgewcwaefgcf"
        t = "cae"
        expected = "cwae"
        self.assertEqual(min_window(s, t), expected)

    def test6(self):
        s = "bba"
        t = "ab"
        expected = "ba"
        self.assertEqual(min_window(s, t), expected)

    def test7(self):
        s = "acbbaca"
        t = "aba"
        expected = "baca"
        self.assertEqual(min_window(s, t), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
