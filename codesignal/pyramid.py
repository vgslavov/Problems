#!/usr/bin/env python3

import sys
import unittest

# n = 4
#    *
#   ***
#  *****
# *******

def print_pyramid(n):
    cols = (n*2)-1

    for i in range(1, n+1):
        asterisks = (i*2)-1
        half_spaces = (cols-asterisks)//2
        print(f"{''.join([half_spaces*' ', asterisks*'*', half_spaces*' '])}")

    return True

class TestPrintPyramid(unittest.TestCase):
    def test10(self):
        n = 10
        self.assertTrue(print_pyramid(n))

if __name__ == '__main__':
    sys.exit(unittest.main())
