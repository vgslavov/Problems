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

# solution: brute-force
# complexity
# run-time: O(n^2)
# space: O(1)
def longest_prefix1(strs):
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

# solution: trie
# complexity
# run-time: O(n)
# space: O(n)
class Trie:
    def __init__(self):
        self.count = 0
        self.children = {}
        # TODO: store shortest word to use to walk trie?

    def insert(self, word):
        curr = self
        curr.count += 1

        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()

            curr = curr.children[c]
            curr.count += 1

    # TODO: refactor
    def common_prefix(self):
        curr = self
        count = self.count
        prefix = ""

        while 1:
            if not curr.children:
                break

            # TODO: pick better?
            c = next(iter(curr.children))
            if curr.count != count:
                return prefix[:-1] if prefix else ""

            prefix += c
            curr = curr.children[c]

        return prefix if curr.count == count else prefix[:-1]

def longest_prefix2(strs):
    trie = Trie()

    # build trie
    for w in strs:
        trie.insert(w)

    return trie.common_prefix()

class TestLongestCommonPrefix(unittest.TestCase):

    def test_empty(self):
        strs = []
        self.assertFalse(longest_prefix1(strs))
        self.assertFalse(longest_prefix2(strs))

    def test_single_char(self):
        strs = ['a']
        expected = strs[0]
        self.assertEqual(longest_prefix1(strs), expected)
        self.assertEqual(longest_prefix2(strs), expected)

    def test_two_chars(self):
        strs = ['aa','aa']
        expected = strs[0]
        self.assertEqual(longest_prefix1(strs), expected)
        self.assertEqual(longest_prefix2(strs), expected)

    def test_three_chars(self):
        strs = ['aba','aba']
        expected = strs[0]
        self.assertEqual(longest_prefix1(strs), expected)
        self.assertEqual(longest_prefix2(strs), expected)

    def test_one_char_match(self):
        strs = ['cir','car']
        expected = 'c'
        self.assertEqual(longest_prefix1(strs), expected)
        self.assertEqual(longest_prefix2(strs), expected)

    def test_two_chars_match(self):
        strs = ['flower','flow','flight']
        expected = 'fl'
        self.assertEqual(longest_prefix1(strs), expected)
        self.assertEqual(longest_prefix2(strs), expected)

    def test_no_match(self):
        strs = ['dog','racecar','car']
        self.assertFalse(longest_prefix1(strs))
        self.assertFalse(longest_prefix2(strs))

    def test_no_match(self):
        strs = ['', 'b']
        self.assertFalse(longest_prefix1(strs))
        self.assertFalse(longest_prefix2(strs))

if __name__ == '__main__':
    sys.exit(unittest.main())
