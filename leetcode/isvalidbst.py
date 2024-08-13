#!/usr/bin/env python3

import math
import sys
import unittest

# number: 98
# section: binary search tree
# difficulty: medium
# tags: tree, dfs, bfs, binary tree, top 150

# constraints
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: iterative dfs
# complexity
# run-time: O(n)
# space: O(n)
def dfs(node, small, large):
    if not node:
        return True

    if small >= node.val or node.val >= large:
        return False

    # all nodes in left subtree < current node
    left = dfs(node.left, small, node.val)
    # all nodes in right subtree > current node
    right = dfs(node.right, node.val, large)

    return left and right

def isvalidbst(root):
    return dfs(root, -math.inf, math.inf)

# TODO: add unit tests & solve iteratively using dfs

if __name__ == '__main__':
    sys.exit(unittest.main())
