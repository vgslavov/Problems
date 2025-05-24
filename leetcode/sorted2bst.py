#!/usr/bin/env python3

import sys
import unittest

# number: 108
# title: Convert Sorted Array to Binary Search Tree
# url: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# section: divide & conquer
# difficulty: easy
# tags: array, divide & conquer, tree, bst, binary tree, top 150

# constraints
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive pre-order dfs
# complexity
# run-time: O(n)
# space: O(log n), max height
def sorted2bst(nums):
    def dfs(left, right):
        if left > right:
            return None

        # root is left middle
        mid = (left+right)//2

        # pre-order traversal
        root = TreeNode(nums[mid])
        root.left = dfs(left, mid-1)
        root.right = dfs(mid+1, right)

        return root

    return dfs(0, len(nums)-1)

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
