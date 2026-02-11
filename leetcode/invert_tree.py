#!/usr/bin/env python3

import sys
import unittest

# number: 226
# title: Invert Binary Tree
# url: https://leetcode.com/problems/invert-binary-tree/
# section: binary tree general
# difficulty: easy
# tags: tree, dfs, bfs, binary tree, top 150, grind 75

# constraints
# The number of nodes in the tree is in the range [0, 100].
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
def invert_tree(root):
    if not root:
        return

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# TODO: solve iteratively

class TestInvertTree(unittest.TestCase):
    def test_invert_tree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        self.assertEqual(invert_tree(root), root)
        self.assertEqual(invert_tree(None), None)
        self.assertEqual(invert_tree(root.left), root.left)
        self.assertEqual(invert_tree(root.right), root.right)
        self.assertEqual(invert_tree(root.left.left), root.left.left)
        self.assertEqual(invert_tree(root.left.right), root.left.right)
        self.assertEqual(invert_tree(root.right.left), root.right.left)
        self.assertEqual(invert_tree(root.right.right), root.right.right)

if __name__ == '__main__':
    sys.exit(unittest.main())
