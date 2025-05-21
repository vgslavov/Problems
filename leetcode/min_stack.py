#!/usr/bin/env python3

import sys
import unittest

# number: 155
# title: Min Stack
# url: https://leetcode.com/problems/min-stack/
# section: stack
# difficulty: medium
# tags: stack, design, top 150

# constraints
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and get_min operations will always be called on non-empty stacks.
# At most 3 * 10^4 calls will be made to push, pop, top, and get_min.

# complexity
# run-time: O(1) per op
# space: O(n)
class MinStack:

    def __init__(self):
        # each item in stack is a tuple: (value, current min)
        self.stack = []

    def push(self, val: int) -> None:
        cmin = val if not len(self.stack) else min(val, self.get_min())
        self.stack.append((val, cmin))

    def pop(self) -> None:
        #top = self.stack[-1][0]
        #del self.stack[-1]
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]

# TODO: less space
# don't store duplicates in tuples

class TesetMinStack(unittest.TestCase):

    def test1(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        self.assertEqual(obj.get_min(), -3)
        obj.pop()
        self.assertEqual(obj.top(), 0)
        self.assertEqual(obj.get_min(), -2)

if __name__ == '__main__':
    sys.exit(unittest.main())
