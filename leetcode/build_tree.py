#!/usr/bin/env python3

import sys
import unittest

# number: 105
# title: Construct Binary Tree from Preorder and Inorder Traversal
# url: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# section: binary tree general
# difficulty: medium
# tags: array, hash table, divide & conquer, tree, binary tree

# constraints
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: Leetcode recursive dfs
# run-time: O(n)
# space: O(n)
def build_tree(preorder, inorder):
    def array2tree(left, right):
        if left > right:
            return None

        # keep track of preorder_i: it's the root of a subtree
        nonlocal preorder_i

        # create the node
        root_val = preorder[preorder_i]
        root = TreeNode(root_val)

        preorder_i += 1

        # find index of root in inorder
        root_i = val2i[root_val]

        # split left & right subtrees from inorder but exclude root
        # left first!
        root.left = array2tree(left, root_i-1)
        root.right = array2tree(root_i+1, right)

        return root

    # value to index dict in inorder
    val2i = {inorder[i]:i for i in range(len(inorder))}
    preorder_i = 0

    return array2tree(0, len(inorder)-1)

if __name__ == '__main__':
    sys.exit(unittest.main())
