#!/usr/bin/env python3

import string
import sys
import unittest

# number: 1832
# title: Check if the Sentence Is Pangram
# url: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# section: string
# difficulty: easy
# tags: string, meta

# constraints
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

# solution: set
# complexity
# run-time: O(n)
# space: O(1)
def ispangram(sentence):

    s = { c for c in sentence }

    for l in string.ascii_lowercase:
        if l not in s:
            return False

    return True

class TestIsPangram(unittest.TestCase):

    def test_empty(self):
        sentence = ''
        self.assertFalse(ispangram(sentence))

    def test_true(self):
        sentence = "thequickbrownfoxjumpsoverthelazydog"
        self.assertTrue(ispangram(sentence))

    def test_false(self):
        sentence = "leetcode"
        self.assertFalse(ispangram(sentence))

if __name__ == '__main__':
    sys.exit(unittest.main())
