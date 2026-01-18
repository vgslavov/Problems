#!/usr/bin/env python

import unittest

# EPI problem 5.6
def str2int(str):

    if not str:
        raise ValueError

    isneg = False
    if str[0] == '-':
        isneg = True
        str = str[1:]

    num = 0
    pos = pow(10, len(str)-1)
    for s in str:
        digit = ord(s) - ord('0')
        num += digit * pos
        pos /= 10

    return -num if isneg else num

class TestStr2Int(unittest.TestCase):

    def test_0(self):
        self.assertEqual(str2int('0'), 0)

    def test_empty(self):
        self.assertRaises(ValueError, str2int, '')

    def test_1d(self):
        self.assertEqual(str2int('1'), 1)

    def test_2d(self):
        self.assertEqual(str2int('12'), 12)

    def test_3d(self):
        self.assertEqual(str2int('123'), 123)

    def test_neg(self):
        self.assertEqual(str2int('-123'), -123)

if __name__ == '__main__':
    unittest.main()
