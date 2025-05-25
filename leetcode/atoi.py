#!/usr/bin/env python3

import sys
import unittest

# number: 8
# title: String to Integer (atoi)
# url: https://leetcode.com/problems/string-to-integer-atoi/
# section: meta
# difficulty: medium
# tags: string, meta

# constraints
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9),
# ' ', '+', '-', and '.'.

# solution: divide & conquer
# complexity
# run-time: O(n)
# space: O(1)
def atoi(s: str) -> int:
    if not s:
        return 0

    # remove spaces
    ss = s.strip()

    isneg = False
    num = 0

    # check sign
    if ss and ss[0] == '-':
        isneg = True
        ss = ss[1:]
    elif ss and ss[0] == '+':
        ss = ss[1:]

    # delete non-digit suffix
    for i in range(len(ss)):
        if not ss[i].isdigit():
            ss = ss[:i]
            break

    # convert in reverse
    digit = 1
    for i in reversed(range(len(ss))):
        # distance from ascii of 0
        num += (ord(ss[i]) - ord('0')) * digit
        digit *= 10

    # round
    max_num = pow(2, 31)
    if num >= max_num:
        if isneg:
            num = max_num
        else:
            num = max_num - 1

    return -num if isneg else num

class TestAtoi(unittest.TestCase):
    def test_empty(self):
        s = ''
        expected = 0
        self.assertEqual(atoi(s), expected)

    def test42(self):
        s = '42'
        expected = 42
        self.assertEqual(atoi(s), expected)

    def test_042(self):
        s = '-042'
        expected = -42
        self.assertEqual(atoi(s), expected)

    def test_1337c0d3(self):
        s = '1337c0d3'
        expected = 1337
        self.assertEqual(atoi(s), expected)

    def test_0_1(self):
        s = '0-1'
        expected = 0
        self.assertEqual(atoi(s), expected)

    def test_words987(self):
        s = 'words and 987'
        expected = 0
        self.assertEqual(atoi(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
