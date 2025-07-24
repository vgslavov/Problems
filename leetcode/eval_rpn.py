#!/usr/bin/env python3

import sys
import unittest

# number: 150
# title: Evaluate Reverse Polish Notation
# url: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# section: stack
# difficulty: medium
# tags: array, math, stack, top 150, citadel, grind 75

# constraints
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].

def apply(op1, op2, op):
    ops = {
        '+': lambda x, y: int(x + y),
        '-': lambda x, y: int(x - y),
        '*': lambda x, y: int(x * y),
        '/': lambda x, y: int(x / y),
    }
    return ops.get(op, lambda x, y: 0)(op2, op1)

# solution: stack
# complexity
# run-time: O(n)
# space: O(n)
def eval_rpn(tokens):
    stack = []

    for t in tokens:
        if not t:
            continue
        # check if negative
        elif t.isnumeric() or t[0] == '-' and len(t) > 1:
            stack.append(int(t))
        elif len(stack) >= 2:
            stack.append(apply(stack.pop(), stack.pop(), t))
        else:
            print(f"stack is almost empty:{stack}")

    return stack.pop() if stack else 0

# TODO: solve recursively

class TestEvalRPN(unittest.TestCase):
    def test_empty(self):
        tokens = []
        expected = 0
        self.assertEqual(eval_rpn(tokens), expected)

    def test1(self):
        tokens = ["2","1","+","3","*"]
        expected = 9
        self.assertEqual(eval_rpn(tokens), expected)

    def test2(self):
        tokens = ["4","13","5","/","+"]
        expected = 6
        self.assertEqual(eval_rpn(tokens), expected)

    def test3(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        expected = 22
        self.assertEqual(eval_rpn(tokens), expected)

    def test4(self):
        tokens = ["3","-4","+"]
        expected = -1
        self.assertEqual(eval_rpn(tokens), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())
