#!/usr/bin/env python3

import sys
import unittest 

# number: 94
# title: Binary Tree Inorder Traversal
# url: https://leetcode.com/problems/binary-tree-inorder-traversal/
# difficulty: easy
# tags: stack, tree, dfs, binary tree

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
def inorder_traversal(root):
    def dfs(node):
        if not node:
            return

        dfs(node.left)
        ans.append(node.val)
        dfs(node.right)

    ans = []
    dfs(root)

    return ans

class TestInorderTraversal(unittest.TestCase):
    def test_inorder_traversal(self):
        # Create a sample binary tree
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        # Test the inorder_traversal function
        self.assertEqual(inorder_traversal(root), [1, 3, 2])

    def test_empty_tree(self):
        # Test with an empty tree
        self.assertEqual(inorder_traversal(None), [])

    def test_large_tree(self):
        # Create a larger binary tree
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)

        # Test the inorder_traversal function
        self.assertEqual(inorder_traversal(root), [1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
    sys.exit(unittest.main())