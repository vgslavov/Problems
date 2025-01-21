#!/usr/bin/env python3

import sys
import unittest

# number: 701
# section:
# difficulty: medium
# tags: tree, bst, binary tree

# constraints
# The number of nodes in the tree will be in the range [0, 10^4].
# -10^8 <= Node.val <= 10^8
# All the values Node.val are unique.
# -10^8 <= val <= 10^8
# It's guaranteed that val does not exist in the original BST.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# run-time: O(log n)
# space: O(1)
def insert_bst(root, val):
    # leaf
    if not root:
        return TreeNode(val)
    # insert as left leaf
    elif not root.left and val < root.val:
        root.left = TreeNode(val)
        return root
    # insert as right leaf
    elif not root.right and val > root.val:
        root.right = TreeNode(val)
        return root
    # go left
    elif val < root.val:
        insert_bst(root.left, val)
        return root
    # go right
    elif val > root.val:
        insert_bst(root.right, val)
        return root
    else:
        print('error: duplicate of {} found'.format(val))

    return root 

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
