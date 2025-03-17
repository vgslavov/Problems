#!/usr/bin/env python3

import numbers
import sys
import unittest

# number: 12
# section: array / string
# difficulty: medium
# tags: hash table, math, string, top 150

# constraints
# 1 <= num <= 3999

# solution: greedy
# complexity
# run-time: O(1)
# space: O(1)
def int2roman(num: int) -> str:
    if not isinstance(num, int):
        return ""

    # largest to smallest
    romans = {"M":1000, "CM":900, "D":500, "CD": 400, "C": 100, "XC": 90,
              "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    ans = ""

    for roman,arabic in romans.items():
        # find first roman numeral that is less than or equal to num
        if arabic > num:
            continue

        # how many times does it fit?
        count = num // arabic
        ans += roman * count
        num -= arabic * count

    return ans

class TestInt2Roman(unittest.TestCase):
    def test_empty(self):
        num = None
        expected = ""
        self.assertEqual(int2roman(num), expected)

    def test_3749(self):
        num = 3749
        expected = "MMMDCCXLIX"
        self.assertEqual(int2roman(num), expected)

    def test_58(self):
        num = 58
        expected = "LVIII"
        self.assertEqual(int2roman(num), expected)

    def test_1994(self):
        num = 1994
        expected = "MCMXCIV"
        self.assertEqual(int2roman(num), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())