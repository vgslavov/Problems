#!/usr/bin/env python3

import sys
import unittest

# number: 58
# title: Length of Last Word
# url: https://leetcode.com/problems/length-of-last-word/
# section: array/string
# difficulty: easy
# tags: string, top 150

# constraints
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '
# There will be at least one word in s

# solution: Pythonic split
# complexity
# run-time: O(n)
# space: O(1)
def len_last_word1(s):
    return len(s.split()[-1]) if s else 0

# solution: manual & slow
# complexity
# run-time: O(n)
# space: O(n)
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

# solution: reversed
# complexity
# run-time: O(n)
# space: O(1)
def len_last_word3(s: str) -> int:
    count = 0

    for i in reversed(range(len(s))):
        if s[i].isalpha():
            count += 1
        elif count:
            break

    return count

class TestLenLastWord(unittest.TestCase):

    def test_empty(self):
        s = ''
        self.assertEqual(len_last_word1(s), 0)
        self.assertEqual(len_last_word2(s), 0)
        self.assertEqual(len_last_word3(s), 0)

    def test_last_word1(self):
        s = "Hello World"
        self.assertEqual(len_last_word1(s), 5)
        self.assertEqual(len_last_word2(s), 5)
        self.assertEqual(len_last_word3(s), 5)

    def test_last_word2(self):
        s = "   fly me   to   the moon  "
        self.assertEqual(len_last_word1(s), 4)
        self.assertEqual(len_last_word2(s), 4)
        self.assertEqual(len_last_word3(s), 4)

    def test_last_word3(self):
        s = "luffy is still joyboy"
        self.assertEqual(len_last_word1(s), 6)
        self.assertEqual(len_last_word2(s), 6)
        self.assertEqual(len_last_word3(s), 6)

if __name__ == '__main__':
    sys.exit(unittest.main())
