#!/usr/bin/env python3

import sys
import unittest

# number: 150
# section: stack
# difficulty: medium
# tags: array, math, stack, top 150

# constraints
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].

# TODO: refactor using dict?
def apply(op1, op2, op):
    if op == '+':
        return int(op2 + op1)
    elif op == '-':
        return int(op2 - op1)
    elif op == '*':
        return int(op2 * op1)
    elif op == '/':
        return int(op2 / op1)
    else:
        print(f"error on op:{op}")
        return 0

    return 0

# solution: stack
# complexity
# run-time: O(n)
# space: O(n)
def eval_rpn(tokens):
    stack = []
    ans = 0

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
