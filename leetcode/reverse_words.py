#!/usr/bin/env python3

import sys
import unittest

# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

# slow! & too much mem
def reverse_words(s):
    ss = s.strip().split(" ")

    ans = [w.strip() for w in ss if w]
    ans.reverse()

    return ' '.join(ans)

# TODO: faster
# TODO: If the string data type is mutable in your language, can you solve
# it in-place with O(1) extra space?

class TestReverseWords(unittest.TestCase):

    def test_empty(self):
        s = ''
        self.assertFalse(reverse_words(s))

    def test1(self):
        s = "the sky is blue"
        expected = "blue is sky the"
        self.assertEqual(expected, reverse_words(s))

    def test2(self):
        s = "  hello world  "
        expected = "world hello"
        self.assertEqual(expected, reverse_words(s))

    def test3(self):
        s = "a good   example"
        expected = "example good a"
        self.assertEqual(expected, reverse_words(s))

if __name__ == '__main__':
    sys.exit(unittest.main())
