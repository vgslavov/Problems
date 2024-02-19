#!/usr/bin/env python3

import sys
import unittest

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

# slowest!
def word_pattern1(pattern, s):
    if not pattern and not s:
        return True

    words = s.split(' ')

    if len(pattern) != len(words):
        return False

    p2w = {}
    w2p = {}

    for i in range(len(pattern)):
        if pattern[i] in p2w:
            if p2w[pattern[i]] != words[i]:
                return False
        else:
            p2w[pattern[i]] = words[i]

        if words[i] in w2p:
            if w2p[words[i]] != pattern[i]:
                return False
        else:
            w2p[words[i]] = pattern[i]

    return True

# slow & ugly!
def word_pattern2(pattern, s):
    p2w = {}
    w2p = {}
    i = j = 0
    word = ''

    while i < len(s) and j < len(pattern):
        if s[i].isspace() or i == len(s) - 1:
            if s[i].isalpha():
                word += s[i]

            if word in w2p:
                if w2p[word] != pattern[j]:
                    return False
            else:
                w2p[word] = pattern[j]

            if pattern[j] in p2w:
                if p2w[pattern[j]] != word:
                    return False
            else:
                p2w[pattern[j]] = word

            word = ''
            j += 1
        elif s[i].isalpha():
            word += s[i]

        i += 1

    return i == len(s) and j == len(pattern)

class TestWordPattern(unittest.TestCase):
    def test_empty(self):
        pattern = ''
        s = ''
        self.assertTrue(word_pattern1(pattern, s))
        self.assertTrue(word_pattern2(pattern, s))

    def test_true(self):
        pattern = "abba"
        s = "dog cat cat dog"
        self.assertTrue(word_pattern1(pattern, s))
        self.assertTrue(word_pattern2(pattern, s))

    def test_false1(self):
        pattern = "abba"
        s = "dog cat cat fish"
        self.assertFalse(word_pattern1(pattern, s))
        self.assertFalse(word_pattern2(pattern, s))

    def test_false2(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        self.assertFalse(word_pattern1(pattern, s))
        self.assertFalse(word_pattern2(pattern, s))

    def test_false3(self):
        pattern = "aaa"
        s = "aa aa aa aa"
        self.assertFalse(word_pattern1(pattern, s))
        self.assertFalse(word_pattern2(pattern, s))

if __name__ == '__main__':
    sys.exit(unittest.main())
