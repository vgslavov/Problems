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

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
