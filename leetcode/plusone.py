#!/usr/bin/env python3

import sys
import unittest

# number: 66
# section: math
# difficulty: easy
# tags: array, math, top 150

# constraints
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# solution: pow + str + Pythonic list comprehension
# complexity
# run-time: O(n)
# space: O(1)
def plusone(digits):
    num = 0
    place = 0

    for i in reversed(range(len(digits))):
        num += digits[i] * pow(10, place)
        place += 1

    num += 1

    return [int(c) for c in str(num)]

# solution: str + Pythonic list comprehensions
# complexity
# run-time: O(n), slower
# space: O(n)?
def plusone2(digits):
    if not digits:
        return [1]

    num = int(''.join([str(d) for d in digits])) + 1

    return [int(c) for c in str(num)]

# TODO: don't convert to str

class TestPlusOne(unittest.TestCase):
    def test_empty(self):
        digits = []
        expected = [1]
        self.assertEqual(plusone(digits), expected)
        self.assertEqual(plusone2(digits), expected)

    def test_123(self):
        digits = [1,2,3]
        expected = [1,2,4]
        self.assertEqual(plusone(digits), expected)
        self.assertEqual(plusone2(digits), expected)

    def test_4321(self):
        digits = [4,3,2,1]
        expected = [4,3,2,2]
        self.assertEqual(plusone(digits), expected)
        self.assertEqual(plusone2(digits), expected)

    def test_9(self):
        digits = [9]
        expected = [1,0]
        self.assertEqual(plusone(digits), expected)
        self.assertEqual(plusone2(digits), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
