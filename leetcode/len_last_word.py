#!/usr/bin/env python3

import sys
import unittest

# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '
# There will be at least one word in s

# fast
def len_last_word1(s):
    return len(s.split()[-1]) if s else 0

# slow
def len_last_word2(s):
    words = []
    word = ''

    for i in range(len(s)):
        if s[i].isalpha():
            word += s[i]
        elif s[i].isspace():
            if word:
                words.append(word)
                word = ''
        else:
            print('invalid char')
            continue

    if word:
        words.append(word)

    return len(words[-1]) if s else 0

class TestLenLastWord(unittest.TestCase):

    def test_empty(self):
        s = ''
        self.assertEqual(len_last_word1(s), 0)
        self.assertEqual(len_last_word2(s), 0)

    def test_last_word1(self):
        s = "Hello World"
        self.assertEqual(len_last_word1(s), 5)
        self.assertEqual(len_last_word2(s), 5)

    def test_last_word2(self):
        s = "   fly me   to   the moon  "
        self.assertEqual(len_last_word1(s), 4)
        self.assertEqual(len_last_word2(s), 4)

    def test_last_word3(self):
        s = "luffy is still joyboy"
        self.assertEqual(len_last_word1(s), 6)
        self.assertEqual(len_last_word2(s), 6)

if __name__ == '__main__':
    sys.exit(unittest.main())
