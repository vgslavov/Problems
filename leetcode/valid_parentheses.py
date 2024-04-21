#!/usr/bin/env python3

import sys
import unittest

# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# TODO: refactor ugly code, use dict to match open/close
def valid_parentheses(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif s[i] == '}':
            if not stack or stack[-1] != '{':
                return False
            else:
                stack.pop()
        elif s[i] == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop()
        else:
            print("invalid char")

    return not len(stack)

class TestValidParentheses(unittest.TestCase):
    def test_empty(self):
        s = ""
        self.assertTrue(valid_parentheses(s))

    def test_true1(self):
        s = "()"
        self.assertTrue(valid_parentheses(s))

    def test_true2(self):
        s = "()[]{}"
        self.assertTrue(valid_parentheses(s))

    def test_false1(self):
        s = "(]"
        self.assertFalse(valid_parentheses(s))

    def test_false2(self):
        s = "([)]"
        self.assertFalse(valid_parentheses(s))

    def test_false3(self):
        s = "["
        self.assertFalse(valid_parentheses(s))

    def test_false4(self):
        s = "]"
        self.assertFalse(valid_parentheses(s))

    def test_false5(self):
        s = "){"
        self.assertFalse(valid_parentheses(s))

    def test_false6(self):
        s = "(){}}{"
        self.assertFalse(valid_parentheses(s))

if __name__ == '__main__':
    sys.exit(unittest.main())
