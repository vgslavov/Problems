#!/usr/bin/env python3

import sys
import unittest

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
# run-time: O(n)?
# space: O(1)
def insert_bst(root, val):
    if not root:
        print('empty: leaf')
        return TreeNode(val)
    elif root.val and val < root.val and not root.left:
        root.left = TreeNode(val)
        print('inserted as left of {}'.format(root.val))
        return root
    elif root.val and val > root.val and not root.right:
        root.right = TreeNode(val)
        print('inserted as right of {}'.format(root.val))
        return root

    # go right
    if val < root.val:
        print('inserting in left')
        insertIntoBST(root.left, val)
        return root
    # go left
    elif val > root.val:
        print('inserting in right')
        insertIntoBST(root.right, val)
        return root
    else:
        print('error: duplicate of {} found'.format(val))

    return root 

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
