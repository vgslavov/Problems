#!/usr/bin/env python

import unittest

# EPI problem 5.6
def int2str(num):

    # check if int
    if not isinstance(num, (int, long)):
        raise TypeError

    isneg = False
    if num < 0:
        isneg = True
        num = -num

    str = ""
    while num:
        digit = num % 10
        # either prepend or append + reverse
        str = chr(ord('0') + digit) + str
        num /= 10

    if not str:
        return "0"

    if isneg:
        str = "-" + str

    return str

class TestInt2Str(unittest.TestCase):

    def test_0(self):
        self.assertEqual(int2str(0), "0")

    def test_nonnum(self):
        self.assertRaises(TypeError, int2str, "str")

    def test_empty(self):
        self.assertRaises(TypeError, int2str, "")

    def test_1d(self):
        self.assertEqual(int2str(1), "1")

    def test_2d(self):
        self.assertEqual(int2str(12), "12")

    def test_3d(self):
        self.assertEqual(int2str(123), "123")

    def test_neg(self):
        self.assertEqual(int2str(-123), "-123")

if __name__ == "__main__":
    unittest.main()
