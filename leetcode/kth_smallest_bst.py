#!/usr/bin/env python3

import sys
import unittest

# number: 230
# title: Kth Smallest Element in a BST
# url: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# section: binary search tree
# difficulty: medium
# tags: tree, dfs, bst, binary tree, top 150, grind 75

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# constraints
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4

# complexity
# run-time: O(n)
# space: O(n)
def dfs(root, values):
    if not root:
        return

    dfs(root.left, values)
    values.append(root.val)
    dfs(root.right, values)

# solution: recursive in-order dfs
# complexity
# run-time: O(n)
# space: O(n)
def kth_smallest_bst(root, k):
    if not root or k < 1:
        return None

    nums_sorted = []
    dfs(root, nums_sorted)

    if k > len(nums_sorted):
        return None

    return nums_sorted[k - 1]

# TODO: solve in O(log n)

class TestKthSmallestBST(unittest.TestCase):
    def test_kth_smallest_bst(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(kth_smallest_bst(root, 1), 1)
        self.assertEqual(kth_smallest_bst(root, 2), 2)
        self.assertEqual(kth_smallest_bst(root, 3), 3)
        self.assertEqual(kth_smallest_bst(root, 4), 4)
        self.assertEqual(kth_smallest_bst(None, 1), None)
        self.assertEqual(kth_smallest_bst(root, 0), None)
        self.assertEqual(kth_smallest_bst(root, 5), None)
        self.assertEqual(kth_smallest_bst(root, -1), None)
        self.assertEqual(kth_smallest_bst(root, 10), None)
        self.assertEqual(kth_smallest_bst(root, 100), None)

if __name__ == '__main__':
    sys.exit(unittest.main())
