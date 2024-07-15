#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

# WIP: O(n)
def longest_subseq(text1, text2):
    count1 = defaultdict(int)
    count2 = defaultdict(int)

    for c in text1:
        count1[c] += 1

    for c in text2:
        count2[c] += 1

    subseq = ''
    i = j = 0

    while i < len(text1) and j < len(text2):
        #print("subseq:{}".format(subseq))

        # match
        if text1[i] == text2[j]:
            subseq += text1[i]
            count1[text1[i]] -= 1
            count2[text2[j]] -= 1
            i += 1
            j += 1
            continue
        # no match, but both exist later
        elif text1[i] in count2 and text2[j] in count1:
            count2[text2[j]] -= 1
            j += 1

        if text1[i] not in count2:
            i += 1

        if text2[j] not in count1:
            j += 1

    return len(subseq)

# sorting loses order:
# O(n log n): dropping non-dominant term O(n)
def longest_subseq_bad1(text1, text2):

    # O(n log n)
    text1 = ''.join(sorted(text1))
    text2 = ''.join(sorted(text2))
    subseq = ''
    i = j = 0

    # O(n)
    while i < len(text1) and j < len(text2):
        if text1[i] == text2[j]:
            subseq += text1[i]
            i += 1
            j += 1
        elif text1[i] < text2[j]:
            i += 1
        else:
            j += 1

    return len(subseq)

class TestLongestSubseq(unittest.TestCase):

    def test_empty(self):
        text1 = ''
        text2 = ''
        self.assertFalse(longest_subseq(text1, text2))

    def test1(self):
        text1 = "abcde"
        text2 = "ace"
        expected = 3
        self.assertEqual(expected, longest_subseq(text1, text2))

    def test2(self):
        text1 = "abc"
        text2 = "abc"
        expected = 3
        self.assertEqual(expected, longest_subseq(text1, text2))

    def test3(self):
        text1 = "abc"
        text2 = "def"
        expected = 0
        self.assertEqual(expected, longest_subseq(text1, text2))

    def test4(self):
        text1 = "ezupkr"
        text2 = "ubmrapg"
        expected = 2
        self.assertEqual(expected, longest_subseq(text1, text2))

    def test5(self):
        text1 = "oxcpqrsvwf"
        text2 = "shmtulqrypy"
        expected = 2
        self.assertEqual(expected, longest_subseq(text1, text2))

if __name__ == '__main__':
    sys.exit(unittest.main())
