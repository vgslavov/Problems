#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 199
# title: Binary Tree Right Side View
# url: https://leetcode.com/problems/binary-tree-right-side-view/
# section: binary tree bfs
# difficulty: medium
# tags: dfs, bfs, binary tree, top 150, meta, grind 75

# constraints
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: iterative bfs
# complexity
# run-time: O(n)
# space: O(n)
def right_side_view(root):
    if not root:
        return []

    # queue contains a full level
    queue = deque([root])

    ans = []

    while queue:
        level_len = len(queue)
        # or
        #ans.append(queue[-1].val)

        for i in range(level_len):
            node = queue.popleft()

            # last (right-most) node in level
            if i == level_len - 1:
                ans.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return ans

class TestRightSideView(unittest.TestCase):
    def test_right_side_view(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(right_side_view(root), [1, 3, 4])
        self.assertEqual(right_side_view(None), [])
        self.assertEqual(right_side_view(root.left), [2, 5])
        self.assertEqual(right_side_view(root.right), [3, 4])
        self.assertEqual(right_side_view(root.left.right), [5])
        self.assertEqual(right_side_view(root.right.right), [4])

if __name__ == '__main__':
    sys.exit(unittest.main())
