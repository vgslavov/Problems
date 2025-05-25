#!/usr/bin/env python3

import sys
import unittest

# number: 100
# title: Same Tree
# url: https://leetcode.com/problems/same-tree/
# section: binary tree general
# difficulty: easy
# tags: tree, dfs, bfs, binary tree, top 150

# constraints
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4

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
def issametree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False

    #print("p.val={}, q.val={}".format(p.val, q.val))
    if p.val != q.val:
        return False

    # fail immediately
    if not issametree(p.left, q.left):
        return False

    if not issametree(p.right, q.right):
        return False

    return True

# TODO: add unit tests & solve using iterative dfs

if __name__ == '__main__':
    sys.exit(unittest.main())
