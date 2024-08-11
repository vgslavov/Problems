#!/usr/bin/env python3

import sys
import unittest

# number: 222
# section: binary tree general
# difficulty: easy
# tags: binary search, bit manipulation, tree, binary tree, top 150

# constraints
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.

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
def count_nodes(root):
    if not root:
        return 0

    left = count_nodes(root.left)
    right = count_nodes(root.right)

    # post-order
    return left+right+1

# TODO: add unit tests & solve iteratively

if __name__ == '__main__':
    sys.exit(unittest.main())
