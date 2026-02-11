#!/usr/bin/env python3 

import sys
import unittest

# number: 106
# title: Construct Binary Tree from Inorder and Postorder Traversal
# url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# section: binary tree
# difficulty: medium
# tags: array, hash table, divide & conquer, tree, binary tree

# constraints
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

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
def build_tree2(inorder, postorder):
    def array2tree(left, right):
        if left > right:
            return None

        # root is last in postorder
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # lookup index of root in inorder
        root_i = val2i[root_val]

        # split inorder tree at root
        # right subtree first!
        # postorder: left, right, root
        root.right = array2tree(root_i+1, right)
        root.left = array2tree(left, root_i-1)

        return root

    # inorder: value to index mapping
    # used for splitting left & right subtrees
    val2i = {inorder[i]:i for i in range(len(inorder))}

    return array2tree(0, len(inorder)-1)

if __name__ == '__main__':
    sys.exit(unittest.main())
