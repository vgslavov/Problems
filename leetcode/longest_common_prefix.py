#!/usr/bin/env python3

import sys
import unittest

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# O(n^2)
def longest_common_prefix1(strs):
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

# TODO: O(n)?
def longest_common_prefix2(strs):
    pass

class TestLongestCommonPrefix(unittest.TestCase):

    def test_empty(self):
        strs = []
        self.assertFalse(longest_common_prefix1(strs))

    def test_single_char(self):
        strs = ['a']
        self.assertEqual(longest_common_prefix1(strs), strs[0])

    def test_two_chars(self):
        strs = ['aa','aa']
        self.assertEqual(longest_common_prefix1(strs), strs[0])

    def test_three_chars(self):
        strs = ['aba','aba']
        self.assertEqual(longest_common_prefix1(strs), strs[0])

    def test_one_char_match(self):
        strs = ['cir','car']
        expected = 'c'
        self.assertEqual(longest_common_prefix1(strs), expected)

    def test_two_chars_match(self):
        strs = ['flower','flow','flight']
        expected = 'fl'
        self.assertEqual(longest_common_prefix1(strs), expected)

    def test_no_match(self):
        strs = ['dog','racecar','car']
        self.assertFalse(longest_common_prefix1(strs))

if __name__ == '__main__':
    sys.exit(unittest.main())
