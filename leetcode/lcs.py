#!/usr/bin/env python3

from collections import defaultdict
from functools import cache
import sys
import unittest

# number: 1143
# section: dp (multi-d)
# difficulty: medium
# tags: string, dp

# constraints
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

# solution: Leetcode top-down recursive 2DP using functools
# complexity
# run-time: O(n*m)
# space: O(n*m)
def lcs1(text1, text2):
    @cache
    def dp(i, j):
        # base case
        if i == len(text1) or j == len(text2):
            return 0

        # recurrence relation
        # match
        if text1[i] == text2[j]:
            return 1 + dp(i+1, j+1)

        # no match
        return max(dp(i, j+1), dp(i+1, j))

    return dp(0, 0)

# solution: Leetcode bottom-up iterative 2DP
# complexity
# run-time: O(n*m)
# space: O(n)
def lcs2(text1, text2):
    if not text1 or not text2:
        return 0

    # init: add 1!
    dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

    # recurrence relation
    # [start, stop) by step:
    # go backwards from last to first inclusive!
    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            # match
            if text1[i] == text2[j]:
                # advance both
                dp[i][j] = 1 + dp[i+1][j+1]
            # no match
            else:
                # add longest
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])

    # longest stored in 1st element!
    return dp[0][0]

# non-solution: dict
# complexity
# run-time: O(n)
# space: O(n)
def lcs_bad1(text1, text2):
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

# non-solution: sorting loses order :(
# complexity
# run-time: O(n*log n)
# space: O(1)
def lcs_bad2(text1, text2):

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
        self.assertFalse(lcs_bad1(text1, text2))
        self.assertFalse(lcs1(text1, text2))
        self.assertFalse(lcs2(text1, text2))

    def test1(self):
        text1 = "abcde"
        text2 = "ace"
        expected = 3
        self.assertEqual(expected, lcs_bad1(text1, text2))
        self.assertEqual(expected, lcs1(text1, text2))
        self.assertEqual(expected, lcs2(text1, text2))

    def test2(self):
        text1 = "abc"
        text2 = "abc"
        expected = 3
        self.assertEqual(expected, lcs_bad1(text1, text2))
        self.assertEqual(expected, lcs1(text1, text2))
        self.assertEqual(expected, lcs2(text1, text2))

    def test3(self):
        text1 = "abc"
        text2 = "def"
        expected = 0
        self.assertEqual(expected, lcs_bad1(text1, text2))
        self.assertEqual(expected, lcs1(text1, text2))
        self.assertEqual(expected, lcs2(text1, text2))

    def test4(self):
        text1 = "ezupkr"
        text2 = "ubmrapg"
        expected = 2
        self.assertEqual(expected, lcs_bad1(text1, text2))
        self.assertEqual(expected, lcs1(text1, text2))
        self.assertEqual(expected, lcs2(text1, text2))

    def test5(self):
        text1 = "oxcpqrsvwf"
        text2 = "shmtulqrypy"
        expected = 2
        # fails
        #self.assertEqual(expected, lcs_bad1(text1, text2))
        self.assertEqual(expected, lcs1(text1, text2))
        self.assertEqual(expected, lcs2(text1, text2))

if __name__ == '__main__':
    sys.exit(unittest.main())
