#!/usr/bin/env python3

import sys
import unittest

# number: 104
# section: binary tree general
# difficulty: easy
# tags: tree, dfs, bfs, binary tree, top 150, leetcode 75

# constraints
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity
# run-time: ?, fast
# space: O(1)
def max_depth(root):
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    # post-order traversal
    return max(left, right) + 1

# solution: iterative dfs
# complexity
# run-time: O(n), slow
# space: O(n)
def max_depth2(root):
    if not root:
        return 0

    stack = [(root, 1)]
    ans = 0

    while stack:
        # pre-order traversal
        node, depth = stack.pop()

        ans = max(ans, depth)

        if node.left:
            stack.append((node.left, depth+1))

        # visiting right first as stack is LIFO!
        if node.right:
            stack.append((node.rigth, depth+1))

    return ans

# TODO: unit test

if __name__ == '__main__':
    sys.exit(unittest.main())
