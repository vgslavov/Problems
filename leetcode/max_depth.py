#!/usr/bin/env python3

import sys
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100

# recursive: fast!
def max_depth(root):
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1

# iterative: slow!
def max_depth2(root):
    if not root:
        return 0

    stack = [(root, 1)]
    ans = 0

    while stack:
        node, depth = stack.pop()

        ans = max(ans, depth)

        if node.left:
            stack.append((node.left, depth+1))

        if node.right:
            stack.append((node.rigth, depth+1))

    return ans

if __name__ == '__main__':
    sys.exit(unittest.main())
