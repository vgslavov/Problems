#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: two pointers
# leetcode: 125

# solution: two pointers, opposite direction
# complexity:
# run-time: O(n)
# space: O(1)
def ispalindrome(s: str) -> bool:
    left = 0
    right = len(s)-1

    while left < right:
        if not s[left].isalpha():
            left += 1
            continue

        if not s[right].isalpha():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
        
    return True

class TestIsPalindrome(unittest.TestCase):
    def test_example_1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(ispalindrome(s))

    def test_example_2(self):
        s = "race a car"
        self.assertFalse(ispalindrome(s))

    def test_example_3(self):
        s = " "
        self.assertTrue(ispalindrome(s))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    s = input()
    res = ispalindrome(s)
    print("true" if res else "false")