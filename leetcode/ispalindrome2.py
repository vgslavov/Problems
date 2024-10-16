#!/usr/bin/env python3

import sys
import unittest

# number:
# section: meta
# difficulty:
# tags: meta

# constraints
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.

# solution: two pointers
# complexity:
# run-time: O(n)
# space: O(1)
def ispalindrome2(s: str) -> bool:
    left = nomatch = 0
    right = len(s)-1

    while left < right:
        print(f"left:{left},right:{right}")
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        nomatch += 1
        print(f"nomatch:{nomatch} at left:{left},right:{right}")

        old_right = right
        old_left = left

        if right > 0 and s[left] == s[right-1]:
            old_right -= 1

        if left < len(s) and s[left+1] == s[right]:
            old_left += 1

        right = old_right
        left = old_left

        if nomatch > 1:
            print(f"nomatch:{nomatch}")
            return False

    if nomatch > 1:
        return False

    return True

class TestIsPalindrome2(unittest.TestCase):
    def test1(self):
        s = "aba"
        self.assertTrue(ispalindrome2(s))

    def test2(self):
        s = "abca"
        self.assertTrue(ispalindrome2(s))

    def test3(self):
        s = "abc"
        self.assertFalse(ispalindrome2(s))

    def test4(self):
        s = "deeee"
        self.assertTrue(ispalindrome2(s))

    def test5(self):
        s = "cdbeeeabddddbaeedebdc"
        self.assertTrue(ispalindrome2(s))

    def test6(self):
        s = "eddboebddcaacddkbebdde"
        self.assertFalse(ispalindrome2(s))

    # TODO: fix algo
    def test7(self):
        s = "ebcbbececabbacecbbcbe"
        self.assertTrue(ispalindrome2(s))

if __name__ == '__main__':
    sys.exit(unittest.main())
