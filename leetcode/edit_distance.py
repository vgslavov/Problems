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

# solution: dict + sort
# complexity
# run-time: 
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

class TestEditDistance(unittest.TestCase):
    def test_empty(self):
        s = ""
        t = ""
        self.assertFalse(edit_distance(s, t))

    def test_same(self):
        s = "a"
        t = "a"
        self.assertFalse(edit_distance(s, t))

    def test_sort(self):
        s = "ab"
        t = "ba"
        self.assertFalse(edit_distance(s, t))

    def test1(self):
        s = "ab"
        t = "acb"
        self.assertTrue(edit_distance(s, t))

    def test2(self):
        s = "teacher"
        t = "detacher"
        self.assertFalse(edit_distance(s, t))

if __name__ == '__main__':
    sys.exit(unittest.main())
