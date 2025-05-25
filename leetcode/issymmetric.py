#!/usr/bin/env python3

import sys
import unittest

# number: 101
# title: Symmetric Tree
# url: https://leetcode.com/problems/symmetric-tree/
# section: binary tree general
# difficulty: easy
# tags: tree, dfs, bfs, binary tree, top 150

# constraints
# The number of nodes in the tree is in the range [1, 1000].
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
def compare(self, p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False

    if p.val != q.val:
        return False

    if not compare(p.left, q.right):
        return False

    if not compare(p.right, q.left):
        return False

    return True

def issymmetric(root):
    if not root:
        return False

    return compare(root.left, root.right)

# TODO: add unit tests & solve iteratively

if __name__ == '__main__':
    sys.exit(unittest.main())
