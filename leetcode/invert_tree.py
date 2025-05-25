#!/usr/bin/env python3

import sys
import unittest

# number: 226
# title: Invert Binary Tree
# url: https://leetcode.com/problems/invert-binary-tree/
# section: binary tree general
# difficulty: easy
# tags: tree, dfs, bfs, binary tree, top 150

# constraints
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

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
def invert_tree(root):
    if not root:
        return

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# TODO: add unit tests & solve iteratively

if __name__ == '__name__':
    sys.exit(unittest.main())
