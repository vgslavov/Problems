#!/usr/bin/env python3

import sys
import unittest

# number: 104
# title: Maximum Depth of Binary Tree
# url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# section: binary tree general
# difficulty: easy
# tags: tree, dfs, bfs, binary tree, top 150, leetcode 75, grind 75

# constraints
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity
# run-time: O(n), fast
# space: O(n)
def max_depth(root):
    if not root:
        return 0

    # post-order traversal
    return max(max_depth(root.left), max_depth(root.right)) + 1

# solution: iterative dfs
# complexity
# run-time: O(n), slow
# space: O(n)
def max_depth2(root):
    if not root:
        return 0

    stack = [(root, 1)]
    ans = 0

    while stack:
        # pre-order traversal
        node, depth = stack.pop()

        ans = max(ans, depth)

        if node.left:
            stack.append((node.left, depth+1))

        # visiting right first as stack is LIFO!
        if node.right:
            stack.append((node.right, depth+1))

    return ans


class TestMaxDepth(unittest.TestCase):
    def test_max_depth(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(max_depth(root), 3)
        self.assertEqual(max_depth2(root), 3)
        self.assertEqual(max_depth(None), 0)
        self.assertEqual(max_depth2(None), 0)
        self.assertEqual(max_depth(root.left), 1)
        self.assertEqual(max_depth2(root.left), 1)
        self.assertEqual(max_depth(root.right), 2)
        self.assertEqual(max_depth2(root.right), 2)
        self.assertEqual(max_depth(root.right.left), 1)
        self.assertEqual(max_depth2(root.right.left), 1)
        self.assertEqual(max_depth(root.right.right), 1)

if __name__ == '__main__':
    sys.exit(unittest.main())
