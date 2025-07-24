#!/usr/bin/env python3

import sys
import unittest

# number: 20
# title: Valid Parentheses
# url: https://leetcode.com/problems/valid-parentheses/
# section: stack
# difficulty: easy
# tags: string, stack, top 150, grind 75

# constraints
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

# solution: stack
# complexity
# run-time: O(n)
# space: O(n)
def is_valid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for i in range(len(s)):
        # opening brackets: keep adding
        if s[i] in mapping.values():
            stack.append(s[i])
        # closing brackets: match
        elif s[i] in mapping.keys():
            if not stack or stack[-1] != mapping[s[i]]:
                return False
            else:
                stack.pop()
        else:
            print("invalid char")

    # if empty, everything matched
    return not len(stack)

class TestValidParentheses(unittest.TestCase):
    def test_empty(self):
        s = ""
        self.assertTrue(is_valid(s))

    def test_true1(self):
        s = "()"
        self.assertTrue(is_valid(s))

    def test_true2(self):
        s = "()[]{}"
        self.assertTrue(is_valid(s))

    def test_false1(self):
        s = "(]"
        self.assertFalse(is_valid(s))

    def test_false2(self):
        s = "([)]"
        self.assertFalse(is_valid(s))

    def test_false3(self):
        s = "["
        self.assertFalse(is_valid(s))

    def test_false4(self):
        s = "]"
        self.assertFalse(is_valid(s))

    def test_false5(self):
        s = "){"
        self.assertFalse(is_valid(s))

    def test_false6(self):
        s = "(){}}{"
        self.assertFalse(is_valid(s))

if __name__ == '__main__':
    sys.exit(unittest.main())
