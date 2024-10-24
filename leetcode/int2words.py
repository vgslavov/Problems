#!/usr/bin/env python3

import sys
import unittest

# number:
# section: meta
# difficulty:
# tags: meta

# constraints

NUM_TO_STR = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
    1000: "Thousand",
    1000000: "Million",
    1000000000: "Billion"
}

def get_hundredths(digits: [], place=100) -> str:
    print(f"get_hundredths: digits:{digits},place:{place}")
    i = 0
    words = []

    while i < len(digits) and place > 0:
        print(f"digit:{digits[i]},place:{place}")

        if place in (1,10):
            words.append(NUM_TO_STR[digits[i]*place])
        elif place == 100:
            words.append(' '.join([NUM_TO_STR[digits[i]], NUM_TO_STR[place]]))
        elif place == 1000:
            # single digit
            if len(digits) == 1:
                words.append(' '.join([NUM_TO_STR[digits[i]], NUM_TO_STR[place]]))
            else:
                words.append(NUM_TO_STR[place])
        elif place == 10000:
            words.append(NUM_TO_STR[digits[i]*10 + digits[i-1]])
        else:
            print(f"TODO")
            return NUM_TO_STR[digits[i]]

        i += 1
        place //= 10

    return ' '.join(words)

# solution: dict
# complexity
# run-time: O(n)
# space: O(1)
def int2words(num: int) -> str:
    # 0
    if not num:
        return NUM_TO_STR[num]

    ans = []
    digits = []
    place = 1

    while num:
        digit = num % 10
        print(f"num:{num},digit:{digit}")

        digits.append(digit)

        # keep adding
        # TODO: generalize
        if place in [100,100000,100000000]:
            ans.append(get_hundredths(list(reversed(digits)), place))
            print(f"ans:{ans}")
            digits = []

        num //= 10
        place *= 10

    print(f"digits:{digits},place:{place}")

    # when num < 1000
    if digits:
        ans.append(get_hundredths(list(reversed(digits)), place//10))
        print(f"ans:{ans}")

    return ' '.join(reversed(ans))

class TestInt2Words(unittest.TestCase):
    def test0(self):
        num = 0
        expected = "Zero"
        self.assertEqual(int2words(num), expected)

    def test123(self):
        num = 123
        expected = "One Hundred Twenty Three"
        self.assertEqual(int2words(num), expected)

    def test12345(self):
        num = 12345
        expected = "Twelve Thousand Three Hundred Forty Five"
        self.assertEqual(int2words(num), expected)

    def test1234567(self):
        num = 1234567
        expected = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        self.assertEqual(int2words(num), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
