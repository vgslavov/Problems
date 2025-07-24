#!/usr/bin/env python3

import math
import sys
import unittest

# number: 98
# title: Validate Binary Search Tree
# url: https://leetcode.com/problems/validate-binary-search-tree/
# section: binary search tree
# difficulty: medium
# tags: tree, dfs, bfs, binary tree, top 150, meta, sig, me, grind 75

# constraints
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, start, end):
    if not node:
        return True

    if start >= node.val or node.val >= end:
        return False

    # all nodes in left subtree < current node
    # all nodes in right subtree > current node
    return dfs(node.left, start, node.val) and dfs(node.right, node.val, end)

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(n)
def isbst(root):
    return dfs(root, -math.inf, math.inf)

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
