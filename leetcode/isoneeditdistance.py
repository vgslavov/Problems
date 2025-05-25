#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 161
# title: One Edit Distance
# url: https://leetcode.com/problems/one-edit-distance/
# section: meta
# difficulty: medium
# tags: two pointers, string, meta

# constraints
# 0 <= s.length, t.length <= 10^4
# s and t consist of lowercase letters, uppercase letters, and digits.

# non-solution: dict + sort
# complexity
# run-time: O(n+m)
# space: O(n)
def isoneeditdistance_bad1(s: str, t: str) -> bool:
    # O(n*log n + m*log m)
    if sorted(s) == sorted(t):
        return False

    counts = defaultdict(int)
    ndiff = 0

    # O(m)
    for c in t:
        counts[c] += 1

    # O(n)
    for c in s:
        if c in t and counts[c]:
            counts[c] -=1
        else:
            ndiff += 1

        if ndiff > 1:
            False

    non_zero = sum(1 for k in counts.keys() if counts[k])
    print(f"non_zero:{non_zero}")
    print(f"counts:{counts}")
    print(f"ndiff:{ndiff}")

    return False if non_zero > 1 or ndiff > 1 else True

# non-solution: two pointers
# complexity
# run-time: O(n+m)
# space: O(1)
def isoneeditdistance_bad2(s: str, t: str) -> bool:
    # len(s)-1 <= len(t) <= len(s)+1
    if len(t) > len(s) + 1 or len(t) < len(s) - 1 or s == t:
        return False

    i = j = ndiff = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        elif j < len(t)-1 and s[i] == t[j+1]:
            ndiff += 1
            i += 1
            j += 2
        elif i < len(s)-1 and s[i+1] == t[j]:
            ndiff += 1
            i += 2
            j += 1
        else:
            ndiff += 1
            i += 1
            j += 1

        if ndiff > 1:
            return False

    if i < len(s) or j < len(t):
        return False

    # single edit
    return ndiff == 1

# complexity
# run-time: O(n)
# space: O(1)
def same_length(s, t):
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        # everything after diff char should be same
        if s[i] != t[i]:
            return s[i+1:] == t[i+1:]

    return False

# solution: Leetcode two pointers
# complexity
# run-time: O(min(n,m))
# space: O(1)
def isoneeditdistance(s: str, t: str) -> bool:
    # identical or too big of a diff in len
    if abs(len(s)-len(t)) > 1 or s == t:
        return False

    if len(s) == len(t):
        return same_length(s, t)

    i = j = ndiff = 0

    while i < len(s) and j < len(t):
        #print(f"i:{i},j:{j}")
        if s[i] == t[j]:
            i += 1
            j += 1
            continue

        ndiff += 1

        if ndiff > 1:
            return False

        # skip extra char!
        if len(s) > len(t):
            i += 1
        else:
            j += 1

    #print(f"ndiff:{ndiff}")

    return True

class TestEditDistance(unittest.TestCase):
    def test_empty(self):
        s = ""
        t = ""
        self.assertFalse(isoneeditdistance(s, t))

    def test_same(self):
        s = "a"
        t = "a"
        self.assertFalse(isoneeditdistance(s, t))

    def test_sort(self):
        s = "ab"
        t = "ba"
        self.assertFalse(isoneeditdistance(s, t))

    def test1(self):
        s = "ab"
        t = "acb"
        self.assertTrue(isoneeditdistance(s, t))

    def test2(self):
        s = "teacher"
        t = "detacher"
        self.assertFalse(isoneeditdistance(s, t))

    def test3(self):
        s = "a"
        t = ""
        self.assertTrue(isoneeditdistance(s, t))

    def test4(self):
        s = "cab"
        t = "ad"
        self.assertFalse(isoneeditdistance(s, t))

    def test5(self):
        s = "cab"
        t = "ab"
        self.assertTrue(isoneeditdistance(s, t))

    def test6(self):
        s = "cab"
        t = "acd"
        self.assertFalse(isoneeditdistance(s, t))

if __name__ == '__main__':
    sys.exit(unittest.main())
