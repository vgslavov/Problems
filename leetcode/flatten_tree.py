#!/usr/bin/env python3

import sys
import unittest

# number: 114
# section: binary tree general
# difficulty: medium
# tags: linked list, stack, tree, dfs, binary tree

# constraint
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root):
    if not root:
        return None
    # leaf
    elif not root.left and not root.right:
        return root

    # flatten left
    left_tail = dfs(root.left)

    # flatten right
    right_tail = dfs(root.right)

    # connect left tail to right child of current node
    # and move left to right
    if left_tail:
        left_tail.right = root.right
        root.right = root.left
        root.left = None

    # return rightmost tail
    return right_tail if right_tail else left_tail

# solution: leetcode recursive dfs
# complexity
# run-time: O(n)
# space: O(n)
def flatten(root):
    dfs(root)

if __name__ == '__main__':
    sys.exit(unittest.main())
