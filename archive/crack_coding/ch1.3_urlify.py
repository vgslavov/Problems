#!/usr/bin/env python3

import sys
import unittest
import urllib.parse

# split & join
def urlify1(s, n):
    return '%20'.join(s.split())

# urllib
def urlify2(s, n):
    # urllib converts ending spaces to %20
    return urllib.parse.quote(s.strip())

# manual
def urlify3(s, n):
    pass

class TestUrlify(unittest.TestCase):

    def test_empty(self):
        s = ''
        self.assertFalse(urlify1(s, 0))
        self.assertFalse(urlify2(s, 0))

    def test_endspace(self):
        s = 'Mr. E. O. Porter  '
        self.assertEqual(urlify1(s, 16), 'Mr.%20E.%20O.%20Porter')
        self.assertEqual(urlify2(s, 16), 'Mr.%20E.%20O.%20Porter')

if __name__ == '__main__':
    sys.exit(unittest.main())
