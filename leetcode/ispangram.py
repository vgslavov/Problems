#!/usr/bin/env python3

import string
import sys
import unittest

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
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
