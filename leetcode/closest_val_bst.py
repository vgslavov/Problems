#!/usr/bin/env python3

import math
import sys
import unittest

# number: 270
# section: assessment
# difficulty: easy
# tags: binary search, tree, dfs, bst, bineary tree, meta

# constraints
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^9
# -10^9 <= target <= 10^9

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity
# run-time: O(log n)
# space: O(n)
def min_diff(root, target):
    # to be safe
    if not root:
        return math.inf, None
    # leaf
    elif not root.left and not root.right:
        return abs(root.val - target), root.val

    # use BST properties!
    if target == root.val:
        return 0, root.val
    elif target < root.val:
        diff, val = min_diff(root.left, target)
    else:
        diff, val = min_diff(root.right, target)

    # works if duplicate diffs: picks smallest val
    return min((abs(root.val - target),root.val), (diff,val))

def closest_val_bst(root, target):
    return int(min_diff(root, target)[1])

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
