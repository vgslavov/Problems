#!/usr/bin/env python3

import sys
import unittest

# number: 1249
# title: Minimum Remove to Make Valid Parentheses
# url: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# section: meta
# difficulty: medium
# tags: stack, string

# constraints
# 1 <= s.length <= 10^5
# s[i] is either '(' , ')', or lowercase English letter.

# solution: stack + set
# complexity
# run-time: O(n)
# space: O(n)
def minrm2makevalid(s: str) -> str:
    stack = []
    ans = []
    idx2rm = set()

    # 1st pass: identify indices to remove
    for i in range(len(s)):
        if s[i].isalpha():
            continue
        # add opening to stack
        elif s[i] == '(':
            stack.append(i)
        # pop closing from stack if not empty
        elif s[i] == ')':
            if len(stack):
                stack.pop()
            else:
                idx2rm.add(i) 
        else:
            print(f"invalid char:{s[i]}")

    # cover trailing ((
    while len(stack):
        idx2rm.add(stack[-1])
        stack.pop()
        
    # 2nd pass: remove chars
    for i in range(len(s)):
        if i in idx2rm:
            continue
        ans.append(s[i])

    return ''.join(ans)

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())