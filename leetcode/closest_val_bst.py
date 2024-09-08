#!/usr/bin/env python3

import math
import sys
import unittest

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
# run-time: O(n)
# space: O(1)
def min_diff(root, target):
    # to be safe
    if not root:
        return None, math.inf
    # leaf
    elif not root.left and not root.right:
        return root.val, abs(root.val - target)

    left_val, left_diff = min_diff(root.left, target)
    #print('left_val:{},left_diff:{}'.format(left_val, left_diff))

    right_val, right_diff = min_diff(root.right, target)
    #print('right_val:{},right_diff:{}'.format(right_val, right_diff))

    # works if duplicate diffs: picks smallest val
    cur_diff,cur_val = min([(abs(root.val - target),root.val),
                            (left_diff,left_val),
                            (right_diff,right_val)])
    return cur_val,cur_diff

def closest_val_bst(root, target):
    return int(min_diff(root, target)[0])

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
