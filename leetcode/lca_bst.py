#!/usr/bin/env python3

import sys
import unittest

# number: 235
# title: Lowest Common Ancestor of a Binary Search Tree
# url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# difficulty: medium
# tags: tree, dfs, bst, binary tree, grind 75

# constraints
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution: recursive dfs
# complexity
# run-time: O(n), if skewed tree
# space: O(n)
def lca_bst(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # base case
    if not root:
        return None

    # 1) LCA is root if p or q is root
    if p == root or q == root:
        return root

    # 2) LCA is root if p or q in different subtrees
    if (
        (p.val < root.val and root.val < q.val)
            or (q.val < root.val and root.val < p.val)
    ):
        return root

    # 3) p & q in same subtree
    if p.val < root.val and q.val < root.val:
        return lca_bst(root.left, p, q)
    else:
        return lca_bst(root.right, p, q)

    return None

class TestLCA(unittest.TestCase):
    def test_lca_bst(self):
        # create a simple BST
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left  # Node with value 2
        q = root.right  # Node with value 8

        self.assertEqual(lca_bst(root, p, q), root)  # LCA should be 6
        self.assertEqual(lca_bst(root, p.left, p.right), p)

if __name__ == '__main__':
    sys.exit(unittest.main())
