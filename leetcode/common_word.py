#!/usr/bin/env python3

from collections import defaultdict
import re
import sys
import unittest

# number: 819
# title: Most Common Word
# url: https://leetcode.com/problems/most-common-word/
# section: assessments
# difficulty: easy
# tags: array, hash able, string, counting, amazon

# constraints
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.

# solution: manual tokenize + dict + sort
# complexity
# run-time: O(n*log n)
# space: O(n)
def common_word(paragraph, banned):
    if not paragraph:
        return ""

    counts = defaultdict(int)
    banned_set = set(banned)
    delim = set("!?',;. ")
    word = ""

    for i in range(len(paragraph)):
        if paragraph[i].isalpha():
            word += paragraph[i].lower()
            continue
        elif paragraph[i] in delim and not word:
            continue

        if word in banned_set:
            word = ""
            continue

        counts[word] += 1
        word = ""

    if word:
        counts[word] += 1

    #print(f"counts:{counts}")

    return sorted(zip(counts.values(), counts.keys()))[-1][1]

# solution: re.split + dict + sort
# complexity
# run-time: O(n*log n)
# space: O(n)
def common_word2(paragraph, banned):
    if not paragraph:
        return ""

    # split by non-word chars
    words = re.split("\W+", paragraph)
    counts = defaultdict(int)
    banned_set = set(banned)

    for w in words:
        wl = w.lower()

        if not wl or wl in banned_set:
            continue

        counts[wl] += 1

    return sorted(zip(counts.values(), counts.keys()))[-1][1]

class TestCommonWord(unittest.TestCase):
    def test_empty(self):
        paragraph = ""
        banned = []
        expected = ""
        self.assertEqual(common_word(paragraph, banned), expected)
        self.assertEqual(common_word2(paragraph, banned), expected)

    def test1(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        expected = "ball"
        self.assertEqual(common_word(paragraph, banned), expected)
        self.assertEqual(common_word2(paragraph, banned), expected)

    def test2(self):
        paragraph = "a."
        banned = []
        expected = "a"
        self.assertEqual(common_word(paragraph, banned), expected)
        self.assertEqual(common_word2(paragraph, banned), expected)

    def test3(self):
        paragraph = "a, a, a, a, b,b,b,c, c"
        banned = ["a"]
        expected = "b"
        self.assertEqual(common_word(paragraph, banned), expected)
        self.assertEqual(common_word2(paragraph, banned), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
