#!/usr/bin/env python3

import sys
import unittest

# number: 22
# title: Generate Parentheses
# url: https://leetcode.com/problems/generate-parentheses/
# section: backtracking
# difficulty: medium
# tags: string, dp, backtracking, top 150, neetcode 150

# solution: backtracking
# complexity:
# run-time: O(4^n / sqrt(n))
# space: O(4^n / sqrt(n))
def generate_parenthesis(n: int) -> list[str]:
    def dfs(open, close):
        # base case
        if open == close == n:
            ans.append(''.join(stack))
            return

        # decision to add open parenthesis
        if open < n:
            stack.append('(')
            dfs(open+1, close)
            stack.pop()

        # decision to add close parenthesis
        if open > close:
            stack.append(')')
            dfs(open, close+1)
            stack.pop()

    ans = []
    stack = []
    dfs(0, 0)
    return ans

# TODO: solve using algomerithmic approach

if __name__ == "__main__":
    sys.exit(unittest.main())