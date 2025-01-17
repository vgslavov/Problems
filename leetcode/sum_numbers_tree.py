#!/usr/bin/env python3

import sys
import unittest

# number: 129
# section: binary tree
# difficulty: medium
# tags: tree, dfs, binary tree, top 150

# contraints
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(n)
def sum_numbers(root):
    def dfs(root, root_leaf):
        nonlocal total

        if not root:
            return
        elif not root.left and not root.right:
            total += root_leaf * 10 + root.val
            return

        root_leaf = root_leaf * 10 + root.val
        dfs(root.left, root_leaf)
        dfs(root.right, root_leaf)

    total = 0
    dfs(root, 0)

    return total

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
