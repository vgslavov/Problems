#!/usr/bin/env python3

import math
import sys
import unittest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The number of nodes in the tree is in the range [0, 10^5].
# -1000 <= Node.val <= 1000

# iterative: slow
def min_depth(root):
    if not root:
        return 0

    ans = math.inf
    stack = [(root, 1)]

    while stack:
        node, depth = stack.pop()

        if node.left:
            stack.append((node.left, depth+1))

        if node.right:
            stack.append((node.right, depth+1))

        # it's a leaf!
        if not node.left and not node.right:
            ans = min(ans, depth)

    return ans

# TODO: recursive?

if __name__ == '__main__':
    sys.exit(unittest.main())
