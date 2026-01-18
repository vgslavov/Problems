#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# dict
def check_permutation1(s1, s2):
    if s1 == s2:
        return True

    if len(s1) != len(s2):
        return False

    d = defaultdict(int)

    for c1, c2 in zip(s1, s2):
        d[c1] += 1
        d[c2] += 1

    return not len([k for k, v in d.items() if v == 1])

# sort: sorted
def check_permutation2(s1, s2):
    return sorted(s1) == sorted(s2)

# sort: list.sort
def check_permutation3(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    return l1 == l2

class TestCheckPermutation(unittest.TestCase):

    def test_empty(self):
        s1 = ''
        s2 = ''
        self.assertTrue(check_permutation1(s1, s2))
        self.assertTrue(check_permutation2(s1, s2))
        self.assertTrue(check_permutation3(s1, s2))

    def test_permutation(self):
        s1 = "abcd"
        s2 = "dcba"
        self.assertTrue(check_permutation1(s1, s2))
        self.assertTrue(check_permutation2(s1, s2))
        self.assertTrue(check_permutation3(s1, s2))

    def test_identical(self):
        s1 = "abcd"
        s2 = "abcd"
        self.assertTrue(check_permutation1(s1, s2))
        self.assertTrue(check_permutation2(s1, s2))
        self.assertTrue(check_permutation3(s1, s2))

    def test_notpermutation(self):
        s1 = "abcd"
        s2 = "dcbd"
        self.assertFalse(check_permutation1(s1, s2))
        self.assertFalse(check_permutation2(s1, s2))
        self.assertFalse(check_permutation3(s1, s2))

    def test_diffsize(self):
        s1 = "abcd"
        s2 = "dcbde"
        self.assertFalse(check_permutation1(s1, s2))
        self.assertFalse(check_permutation2(s1, s2))
        self.assertFalse(check_permutation3(s1, s2))

if __name__ == "__main__":
    sys.exit(unittest.main())
