#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number:
# section: meta
# difficulty:
# tags: meta

# constraints
# 0 <= s.length, t.length <= 10^4
# s and t consist of lowercase letters, uppercase letters, and digits.

# solution: bad, dict + sort
# complexity
# run-time: O(n+m)
# space: O(n)
def edit_distance(s: str, t: str) -> bool:
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

# solution: bad, two pointers
# complexity
# run-time: O(n+m)
# space: O(1)
def edit_distance2(s: str, t: str) -> bool:
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

# solution:
# complexity:
# run-time:
# space:
def edit_distance3(s: str, t: str) -> bool:
    # len(s)-1 <= len(t) <= len(s)+1
    if len(t) > len(s) + 1 or len(t) < len(s) - 1 or s == t:
        return False

    ndiff = 0

    # 1) strings are same length
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                ndiff += 1

            if ndiff > 1:
                return False

    # TODO: 2) string have diff lengths

    return ndiff == 1

class TestEditDistance(unittest.TestCase):
    def test_empty(self):
        s = ""
        t = ""
        self.assertFalse(edit_distance(s, t))
        self.assertFalse(edit_distance2(s, t))
        self.assertFalse(edit_distance3(s, t))

    def test_same(self):
        s = "a"
        t = "a"
        self.assertFalse(edit_distance(s, t))
        self.assertFalse(edit_distance2(s, t))
        self.assertFalse(edit_distance3(s, t))

    def test_sort(self):
        s = "ab"
        t = "ba"
        self.assertFalse(edit_distance(s, t))
        self.assertFalse(edit_distance2(s, t))
        self.assertFalse(edit_distance3(s, t))

    def test1(self):
        s = "ab"
        t = "acb"
        self.assertTrue(edit_distance(s, t))
        self.assertTrue(edit_distance2(s, t))
        self.assertTrue(edit_distance3(s, t))

    def test2(self):
        s = "teacher"
        t = "detacher"
        # not solvable
        #self.assertFalse(edit_distance(s, t))
        self.assertFalse(edit_distance2(s, t))
        self.assertFalse(edit_distance3(s, t))

    def test3(self):
        s = "a"
        t = ""
        #self.assertFalse(edit_distance(s, t))
        #self.assertTrue(edit_distance2(s, t))
        self.assertTrue(edit_distance3(s, t))


if __name__ == '__main__':
    sys.exit(unittest.main())
