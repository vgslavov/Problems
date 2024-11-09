#!/usr/bin/env python3

import sys
import unittest

# number: 69
# section: math
# difficulty: easy
# tags: math, binary search, top 150, citadel

# constraints
#0 <= x <= 2^31 - 1

# solution: binary search
# complexity
# run-time: O(n)
# space: O(1)
def check(x, k):
    return False if k*k > x else True

def sqrt(x):
    if not x:
        return 0

    # possible answer range
    start = 1
    end = x

    while start <= end:
        mid = start + (end-start) // 2

        #print("start:{}, mid:{}, end:{}".format(start, mid, end))

        if check(x, mid):
            start = mid+1
        else:
            end = mid-1

    return end

class TestSqrt(unittest.TestCase):

    def test_0(self):
        x = 0
        expected = 0
        self.assertEqual(sqrt(x), expected)

    def test_1(self):
        x = 1
        expected = 1
        self.assertEqual(sqrt(x), expected)

    def test_2(self):
        x = 2
        expected = 1
        self.assertEqual(sqrt(x), expected)

    def test_3(self):
        x = 3
        expected = 1
        self.assertEqual(sqrt(x), expected)

    def test_4(self):
        x = 4
        expected = 2
        self.assertEqual(sqrt(x), expected)

    def test_8(self):
        x = 8
        expected = 2
        self.assertEqual(sqrt(x), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
