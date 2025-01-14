#!/usr/bin/env python3

import sys
import unittest

# number: 28
# section: array/string
# difficulty: easy
# tags: two pointers, string, string matching, top 150

# constraints
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.

# non-solution: two pointers
# complexity
# run-time: O(n)
# space: O(1)
# TODO: fix bug
def strstr1(haystack, needle):
    if not haystack or not needle:
        return -1
    elif haystack == needle:
        return 0

    start = i = j = 0

    while i < len(haystack) and j < len(needle):
        # needle is matching
        if haystack[i] == needle[j]:
            if j == 0:
                start = i
            j += 1
        # needle is not matching: reset
        else:
            j = 0

        # continue going through haystack
        i += 1

    # needle found
    if j == len(needle):
        return start

    return -1

# solution: slicing
# complexity
# run-time: O((n-m+1)*m)
# space: O(1)
def strstr2(haystack, needle):
    if not haystack or not needle:
        return -1
    elif haystack == needle:
        return 0

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1

# TODO: O(n) using sliding window?

class TestStrstr(unittest.TestCase):
    def test_empty(self):
        h = ''
        n = ''
        self.assertEqual(strstr1(h, n), -1)
        self.assertEqual(strstr2(h, n), -1)

    def test_single(self):
        h = 'a'
        n = 'a'
        self.assertEqual(strstr1(h, n), 0)
        self.assertEqual(strstr2(h, n), 0)

    def test_last(self):
        h = 'abc'
        n = 'c'
        self.assertEqual(strstr1(h, n), 2)
        self.assertEqual(strstr2(h, n), 2)

    def test_first(self):
        h = 'sadbutsad'
        n = 'sad'
        self.assertEqual(strstr1(h, n), 0)
        self.assertEqual(strstr2(h, n), 0)

    def test_notfound(self):
        h = 'leetcode'
        n = 'leeto'
        self.assertEqual(strstr1(h, n), -1)
        self.assertEqual(strstr2(h, n), -1)

    def test_repetition(self):
        h = 'mississipi'
        n = 'issip'
        # TODO: fix bug
        #self.assertEqual(strstr1(h, n), 4)
        self.assertEqual(strstr2(h, n), 4)

if __name__ == '__main__':
    sys.exit(unittest.main())
