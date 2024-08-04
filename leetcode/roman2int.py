#!/usr/bin/env python3

import sys
import unittest

# number: 13
# section: array/string
# difficulty: easy
# tags: hash table, math, string, top 150

# reference
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# constraints
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# complexity
# run-time: O(n)
# space: O(1)
# TODO: faster implementation?
def roman2int(s):
    values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    roman = s.upper()
    num = 0

    for i in range(len(s)):
        if i == len(s)-1:
            num += values[s[i]]
        elif s[i] == 'I':
            # more efficient than
            #if s[i+1] in ('V', 'X'):
            if s[i+1] == 'V' or s[i+1] == 'X':
                num -= values[s[i]]
            else:
                num += values[s[i]]
        elif s[i] == 'V':
            num += values[s[i]]
        elif s[i] == 'X':
            if s[i+1] == 'L' or s[i+1] == 'C':
                num -= values[s[i]]
            else:
                num += values[s[i]]
        elif s[i] == 'L':
            num += values[s[i]]
        elif s[i] == 'C':
            if s[i+1] == 'D' or s[i+1] == 'M':
                num -= values[s[i]]
            else:
                num += values[s[i]]
        elif s[i] == 'D':
            num += values[s[i]]
        elif s[i] == 'M':
            num += values[s[i]]
        else:
            print('invalid Roman number')
            return False

    return num

class TestRomanToInt(unittest.TestCase):

    def test_invalid(self):
        s = "xyz"
        self.assertFalse(roman2int(s))

    def test_empty(self):
        s = ""
        self.assertFalse(roman2int(s))

    def test_roman_3(self):
        s = "III"
        self.assertEqual(roman2int(s), 3)

    def test_roman_58(self):
        s = "LVIII"
        self.assertEqual(roman2int(s), 58)

    def test_roman_1994(self):
        s = "MCMXCIV"
        self.assertEqual(roman2int(s), 1994)

if __name__ == '__main__':
    sys.exit(unittest.main())
