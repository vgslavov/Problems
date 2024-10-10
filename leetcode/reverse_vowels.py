#!/usr/bin/env python3

import sys
import unittest

# number: 345
# section: assessments
# difficulty: easy
# tags: two pointers, string, meta

# constraints
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.

# solution: two pointers
# complexity
# run-time: O(n)
# space: O(n) because of join?
def reverse_vowels(s: str) -> str:
    if not s:
        return ""

    l = list(s)
    left = 0
    right = len(l)-1
    vowels = {'a','e','i','o','u'}

    while left < right:
        if l[left].lower() not in vowels:
            left += 1
            continue

        if l[right].lower() not in vowels:
            right -= 1
            continue

        # swap
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1

    return ''.join(l)

class TestReverseVowels(unittest.TestCase):
    def test_empty(self):
        s = ''
        expected = ''
        self.assertEqual(reverse_vowels(s), expected)

    def test1(self):
        s = "IceCreAm"
        expected = "AceCreIm"
        self.assertEqual(reverse_vowels(s), expected)

    def test2(self):
        s = "leetcode"
        expected = "leotcede"
        self.assertEqual(reverse_vowels(s), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
