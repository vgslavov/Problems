#!/usr/bin/env python3

import sys
import unittest

# number: 43
# title: Multiply Strings
# url: https://leetcode.com/problems/multiply-strings/
# section: meta
# difficulty: medium
# tags: math, string, simulation, meta

# constraints
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# complexity
# run-time: O(log n)
# space: O(1)
def int2str(n):
    #print(f"n:{n}")
    if n == 0:
        return "0"

    s = ""

    while n:
        d = n % 10
        s += str(d)
        # integer division!
        n //= 10

    #print(f"s:{s}")
    return ''.join(reversed(s))

# complexity
# run-time: O(n)
# space: O(1)
def str2int(s):
    #print(f"s:{s}")
    n = 0
    digit = 1

    for c in reversed(s):
        # subtract ASCII!
        n += (ord(c) - ord('0')) * digit
        digit *= 10

    return n

# solution: str 2 int 2 str
# complexity
# run-time: O(n+m)
# space: O(1)
def multiply_str(num1: str, num2: str) -> str:
    if not num1 or not num2:
        return ""

    return int2str(str2int(num1)*str2int(num2))

class TestMutiplyStr(unittest.TestCase):
    def test_empty(self):
        num1 = ""
        num2 = ""
        expected = ""
        self.assertEqual(multiply_str(num1, num2), expected)

    def test1(self):
        num1 = "2"
        num2 = "3"
        expected = "6"
        self.assertEqual(multiply_str(num1, num2), expected)

    def test2(self):
        num1 = "123"
        num2 = "456"
        expected = "56088"
        self.assertEqual(multiply_str(num1, num2), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
