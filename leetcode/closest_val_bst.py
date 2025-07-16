#!/usr/bin/env python3

import math
import sys
import unittest

# number: 270
# title: Closest Binary Search Tree Value
# url: https://leetcode.com/problems/closest-binary-search-tree-value/
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

# solution: recursive dfs
# complexity
# run-time: O(log n)
# space: O(n)
def closest_val_bst(root, target):
    return int(min_diff(root, target)[1])

# solution: recursive dfs
# complexity
# run-time: O(log n)
# space: O(n)
def closest_val_bst2(root, target) -> int:
    def dfs(node, closest):
        if not node:
            return closest

        new_diff = abs(node.val - target)
        old_diff = abs(closest - target)

        if new_diff < old_diff:
            closest = node.val
        # if equal, pick the smaller one
        elif new_diff == old_diff:
            closest = min(node.val, closest)

        if target == node.val:
            # don't return target as it may have trailing 0s
            return node.val
        elif target > node.val:
            return dfs(node.right, closest)
        else:
            return dfs(node.left, closest)

    return dfs(root, root.val)

class TestClosestValBST(unittest.TestCase):
    def test_closest_val_bst(self):
        # Example tree:
        #       4
        #      / \
        #     2   5
        #    / \
        #   1   3
        root = TreeNode(4)
        root.left = TreeNode(2, TreeNode(1), TreeNode(3))
        root.right = TreeNode(5)

        self.assertEqual(closest_val_bst(root, 3.714286), 4)
        self.assertEqual(closest_val_bst2(root, 3.714286), 4)

        self.assertEqual(closest_val_bst(root, 2.1), 2)
        self.assertEqual(closest_val_bst2(root, 2.1), 2)

        self.assertEqual(closest_val_bst(root, 6), 5)
        self.assertEqual(closest_val_bst2(root, 6), 5)

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
