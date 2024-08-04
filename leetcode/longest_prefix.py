#!/usr/bin/env python3

import sys
import unittest

# number: 14
# section: array/string
# difficulty: easy
# tags: string, trie, top 150

# constraints
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# complexity
# run-time: O(n^2)
# space: O(1)
def longeset_prefix1(strs):
    if not strs or not len(strs[0]):
        return ''
    elif len(strs) == 1:
        return strs[0]

    prefix = ''
    curr_prefix = ''

    # go over 1st word
    for i in range(len(strs[0])):
        # go over rest of words
        for j in range(1, len(strs)):
            # mismatch
            if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                return prefix

            curr_prefix = strs[0][i]

        prefix += curr_prefix
        curr_prefix = ''

    return prefix if prefix else ''

# TODO: O(n) using trie?

class TestLongestCommonPrefix(unittest.TestCase):

    def test_empty(self):
        strs = []
        self.assertFalse(longeset_prefix1(strs))

    def test_single_char(self):
        strs = ['a']
        self.assertEqual(longeset_prefix1(strs), strs[0])

    def test_two_chars(self):
        strs = ['aa','aa']
        self.assertEqual(longeset_prefix1(strs), strs[0])

    def test_three_chars(self):
        strs = ['aba','aba']
        self.assertEqual(longeset_prefix1(strs), strs[0])

    def test_one_char_match(self):
        strs = ['cir','car']
        expected = 'c'
        self.assertEqual(longeset_prefix1(strs), expected)

    def test_two_chars_match(self):
        strs = ['flower','flow','flight']
        expected = 'fl'
        self.assertEqual(longeset_prefix1(strs), expected)

    def test_no_match(self):
        strs = ['dog','racecar','car']
        self.assertFalse(longeset_prefix1(strs))

if __name__ == '__main__':
    sys.exit(unittest.main())
