#!/usr/bin/env python3

import sys
import unittest

# number: 257
# title: Binary Tree Paths
# url: https://leetcode.com/problems/binary-tree-paths/
# section: binary tree general
# difficulty: easy
# tags: tree, dfs, backtracking, string, meta

# constraints
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def join_str(s1, s2):
    return '->'.join([s1, s2]) if s1 else s2

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(n)
def binary_tree_paths(root):
    # pass string, not a list!
    # need to pass by value, not by reference
    def dfs(node, p):
        # base case
        if not node:
            return
        elif not node.left and not node.right:
            paths.append(join_str(p, str(node.val)))
            return

        p = join_str(p, str(node.val))
        dfs(node.left, p)
        dfs(node.right, p)

    paths = []
    dfs(root, '')
    return paths

class TestBinaryTreePaths(unittest.TestCase):
    def test_example_1(self):
        # Example 1
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        expected = ["1->2", "1->3"]
        self.assertEqual(binary_tree_paths(root), expected)

    def test_example_2(self):
        # Example 2
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        expected = ["1->2->3"]
        self.assertEqual(binary_tree_paths(root), expected)

    def test_single_node(self):
        # Single node
        root = TreeNode(5)
        expected = ["5"]
        self.assertEqual(binary_tree_paths(root), expected)

if __name__ == '__main__':
    sys.exit(unittest.main())