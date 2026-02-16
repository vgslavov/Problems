#! /usr/bin/env python3

import itertools
from typing import Iterator
import sys
import unittest

# number: 844
# title: Backspace String Compare
# url: https://leetcode.com/problems/backspace-string-compare/
# difficulty: easy
# tags: two pointers, string, stack, grind 75

# constraints:
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.

# run-time: O(n)
# space: O(n)
def remove_char(s: str, pattern: str) -> list:
    stack = []

    for c in s:
        if c == pattern:
            if not stack:
                continue
            else:
                stack.pop()
        else:
            stack.append(c)

    return stack

# solution: stack
# complexity:
# run-time: O(n+m)
# space: O(n+m)
def backspace_compare(s: str, t: str) -> bool:
    return remove_char(s, '#') == remove_char(t, '#')

def skip_pattern(s: str, pattern: str) -> Iterator[str]:
    skip = 0

    for c in reversed(s):
        if c == pattern:
            skip += 1
        elif skip:
            skip -= 1
        else:
            yield c

# solution: Pythonic, reversed + generator + itertools
# complexity:
# run-time: O(n+m)
# space: O(1)
def backspace_compare2(s: str, t: str) -> bool:
    return all(
        x == y
        for x, y in itertools.zip_longest(
            skip_pattern(s, '#'),
            skip_pattern(t, '#'),
        )
    )

# solution: reversed + generator
# complexity:
# run-time: O(n+m)
# space: O(1)
def backspace_compare3(s: str, t: str) -> bool:
    gs = skip_pattern(s, '#')
    gt = skip_pattern(t, '#')

    while True:
        try:
            cs = next(gs)
        except StopIteration:
            cs = None

        try:
            ct = next(gt)
        except StopIteration:
            ct = None

        # characters differ
        if cs != ct:
            return False

        # reached the end of both strings
        if cs is None and ct is None:
            return True

class TestBackspaceCompare(unittest.TestCase):
    def test_backspaceCompare(self):
        self.assertTrue(backspace_compare("ab#c", "ad#c"))
        self.assertTrue(backspace_compare2("ab#c", "ad#c"))
        self.assertTrue(backspace_compare3("ab#c", "ad#c"))

        self.assertTrue(backspace_compare("ab##", "c#d#"))
        self.assertTrue(backspace_compare2("ab##", "c#d#"))
        self.assertTrue(backspace_compare3("ab##", "c#d#"))

        self.assertFalse(backspace_compare("a#c", "b"))
        self.assertFalse(backspace_compare2("a#c", "b"))
        self.assertFalse(backspace_compare3("a#c", "b"))

        self.assertTrue(backspace_compare("a##c", "#a#c"))
        self.assertTrue(backspace_compare2("a##c", "#a#c"))
        self.assertTrue(backspace_compare3("a##c", "#a#c"))

        self.assertTrue(backspace_compare("a#b#c#d#", "####"))
        self.assertTrue(backspace_compare2("a#b#c#d#", "####"))
        self.assertTrue(backspace_compare3("a#b#c#d#", "####"))

        self.assertFalse(backspace_compare("a#b#c#d#", "###e"))
        self.assertFalse(backspace_compare2("a#b#c#d#", "###e"))
        self.assertFalse(backspace_compare3("a#b#c#d#", "###e"))

if __name__ == "__main__":
    sys.exit(unittest.main())