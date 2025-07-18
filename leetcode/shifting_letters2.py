#!/usr/bin/env python3

import string
import sys
import unittest

# number: 2381
# title: Shifting Letters II
# url: https://leetcode.com/problems/shifting-letters-ii/
# difficulty: medium
# tags: string, array, prefix sum

# constraints:
# 1 <= s.length, shifts.length <= 5 * 10^4
# shifts[i].length == 3
# 0 <= starti <= endi < s.length
# 0 <= directioni <= 1
# s consists of lowercase English letters.

# solution: diff array + prefix sum
# n: len(s)
# m: len(shifts)
# run-time: O(n + m)
# space: O(n)
def shifting_letters2(s: str, shifts: list[list[int]]) -> str:
    # diff array as long as s
    diff = [0] * len(s)

    # calc diff array over shifts: O(m)
    for start,end,direct in shifts:
        diff[start] += 1 if direct else -1
        if end+1 < len(diff):
            diff[end+1] += -1 if direct else 1

    # calc prefix sum of diff array: O(n)
    prefix = [diff[0]]

    for i in range(1, len(diff)):
        prefix.append(prefix[-1]+diff[i])

    l = list(s)
    az = list(string.ascii_lowercase)
    # key: char, value: index in az
    d = {c:i for i,c in enumerate(az)}

    # apply to str: O(n)
    for i in range(len(prefix)):
        if i < len(l):
            # look up char in az
            # shift by prefix position
            # and wrap around using modulo
            l[i] = az[(d[l[i]] + prefix[i]) % len(az)]

    return ''.join(l)

class TestShiftingLetters(unittest.TestCase):
    def test_example1(self):
        s = "abc"
        shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
        self.assertEqual(shifting_letters2(s, shifts), "ace")

    def test_example2(self):
        s = "dztz"
        shifts = [[0, 0, 0], [1, 1, 1]]
        self.assertEqual(shifting_letters2(s, shifts), "catz")

    def test_example3(self):
        s = "iaozjb"
        shifts = [[0,4,0],[0,2,1],[1,3,1],[0,4,1],[4,4,1],[2,3,0],
                  [5,5,0],[3,3,0],[2,3,0],[5,5,1],[5,5,1],[5,5,0]]
        self.assertEqual(shifting_letters2(s, shifts), "jcoxkb") 

    def test_example4(self):
        s = "xuwdbdqik"
        shifts = [[4,8,0],[4,4,0],[2,4,0],[2,4,0],[6,7,1],[2,2,1],
                  [0,2,1],[8,8,0],[1,3,1]]
        self.assertEqual(shifting_letters2(s, shifts), "ywxcxcqii")

    def test_example5(self):
        s = "gwwzxlugtvdibjzwobwdakjubutyfgxrmo"
        shifts = [[24,27,1],[11,19,1],[25,26,0],[13,32,0],[28,30,1],
                  [16,29,1],[4,12,0],[10,28,1],[12,23,0],[17,25,0],
                  [16,30,1],[13,18,1],[22,33,1],[28,28,0],[28,31,0],
                  [31,33,0],[9,10,0],[9,28,0],[13,20,1],[22,23,0],
                  [21,22,1],[25,26,0],[8,11,0],[0,20,1],[32,32,1]]
        self.assertEqual(shifting_letters2(s, shifts), "hxxaxlugssbiblbysezfbkjtduubgiypmo")

if __name__ == "__main__":
    sys.exit(unittest.main())