#!/usr/bin/env python3

import sys
import unittest

# number: 110
# title: Balanced Binary Tree
# url: https://leetcode.com/problems/balanced-binary-tree/
# difficulty: easy
# tags: tree, dfs, binary tree, grind 75

# constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0

    return max(max_depth(root.left), max_depth(root.right)) + 1

# solution: recursive top-down dfs
# complexity
# run-time: O(n^2)
# space: O(n)
def isbalanced(root) -> bool:
    if not root:
        return True

    return (
        abs(max_depth(root.right)-max_depth(root.left)) <= 1
        and isbalanced(root.left)
        and isbalanced(root.right)
    )

def check_balance(root):
    if not root:
        return True, 0

    left_balanced, left_depth = check_balance(root.left)

    if not left_balanced:
        return False, 0

    right_balanced, right_depth = check_balance(root.right)

    if not right_balanced:
        return False, 0

    return abs(left_depth-right_depth) <= 1, max(right_depth,left_depth)+1

# solution: LeetCode recursive bottom-up dfs
# complexity
# run-time: O(n)
# space: O(n)
def isbalanced2(root) -> bool:
    return check_balance(root)[0]

class TestIsBalanced(unittest.TestCase):
    def test_isbalanced(self):
        # Example 1
        root1 = TreeNode(3)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
        self.assertTrue(isbalanced(root1))
        self.assertTrue(isbalanced2(root1))

        # Example 2
        root2 = TreeNode(1)
        root2.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), None)
        self.assertFalse(isbalanced(root2))
        self.assertFalse(isbalanced2(root2))

        # Example 3
        root3 = None
        self.assertTrue(isbalanced(root3))
        self.assertTrue(isbalanced2(root3))

if __name__ == "__main__":
    sys.exit(unittest.main())