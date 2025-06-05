#!/usr/bin/env python3

import sys
import unittest

# number: 543
# title: Diameter of Binary Tree
# url: https://leetcode.com/problems/diameter-of-binary-tree/
# difficulty: easy
# tags: tree, dfs, binary tree

# constraints
# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100

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
def diameter_tree(root):
    def dfs(root):
        # need nonlocal for POD variable!
        # (don't for list/dict/etc.)
        nonlocal diameter

        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)

        diameter = max(diameter, left+right)
        
        return max(left, right) + 1

    diameter = 0
    dfs(root)
    return diameter

class TestDiameterTree(unittest.TestCase):
    def test_example1(self):
        # Example 1
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(diameter_tree(root), 3)

    def test_example2(self):
        # Example 2
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(diameter_tree(root), 1)

if __name__ == '__main__':
    sys.exit(unittest.main())