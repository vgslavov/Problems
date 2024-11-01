#!/usr/bin/env python3

import sys
import unittest

# number: 700
# section: recursion
# difficulty: easy
# tags: tree, bst, binary tree

# constraints
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 10^7
# root is a binary search tree.
# 1 <= val <= 10^7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# complexity
# run-time: O(log n)
# space: O(n)
def search_bst(root, val):
    if not root:
        return None
    elif root.val == val:
        return root
    elif val > root.val:
        return search_bst(root.right, val)
    else:
        return search_bst(root.left, val)

if __name__ == '__main__':
    sys.exit(unittest.main())
