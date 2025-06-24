#!/usr/bin/env python3

import sys
import unittest

# number: 236
# title: Lowest Common Ancestor of a Binary Tree
# url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# section: binary tree
# difficulty: medium
# tags: tree, dfs, binary tree, top 150, meta

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
    # empty tree
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

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
