#!/usr/bin/env python3

import string
import sys
import unittest

# number: 848
# title: Shifting Letters
# url: https://leetcode.com/problems/shifting-letters/
# difficulty: medium
# tags: string, array, prefix sum

# constraints:
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# shifts.length == s.length
# 0 <= shifts[i] <= 10^9

# solution: diff array + prefix sum
# run-time: O(n + n) ~ O(n)
# space: O(n)
def shifting_letters(s: str, shifts: list[int]) -> str:
    # build a diff array
    diff = [0] * len(s)

    for i in range(len(shifts)):
        diff[0] += shifts[i]
        # inclusive
        if i+1 < len(diff):
            diff[i+1] -= shifts[i]

    # build a prefix sum
    prefix = [diff[0]]

    for i in range(1, len(diff)):
        prefix.append(prefix[-1]+diff[i])

    az = list(string.ascii_lowercase)
    d = {c:i for i,c in enumerate(string.ascii_lowercase)}
    l = list(s)

    # apply to s
    for i in range(len(prefix)):
        l[i] = az[(d[l[i]]+prefix[i]) % len(az)]

    return ''.join(l)

class TestShiftingLetters(unittest.TestCase):
    def test_example1(self):
        s = "abc"
        shifts = [3, 5, 9]
        self.assertEqual(shifting_letters(s, shifts), "rpl")

    def test_example2(self):
        s = "aaa"
        shifts = [1, 2, 3]
        self.assertEqual(shifting_letters(s, shifts), "gfd")

if __name__ == "__main__":
    sys.exit(unittest.main())