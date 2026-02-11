#!/usr/bin/env python3

import sys
import unittest

# number: 236
# title: Lowest Common Ancestor of a Binary Tree
# url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# section: binary tree
# difficulty: medium
# tags: tree, dfs, binary tree, top 150, meta, grind 75

# constraints
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(n)
def lca(root, p, q):
    # base case
    if not root:
        return None

    # 1) p or q is root, root is LCA
    if root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    # 2) p and q in different subtrees, root is LCA
    if left and right:
        return root

    # 3) p and q in same subtree
    if left:
        return left

    return right

class TestLCA(unittest.TestCase):
    def test_lca(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)

        self.assertEqual(lca(root, root.left, root.right), root)
        self.assertEqual(lca(root, root.left.right.left, root.left.right.right), root.left.right)
        self.assertEqual(lca(root, root.left.left, root.left.right.right), root.left)
        self.assertEqual(lca(root, root.right.left, root.right.right), root.right)
        self.assertEqual(lca(root, root.left.left, root.right.right), root)

if __name__ == '__main__':
    sys.exit(unittest.main())
