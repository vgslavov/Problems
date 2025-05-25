#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 637
# title: Average of Levels in Binary Tree
# url: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# section: binary tree BFS
# difficulty: easy
# tags: tree, dfs, bfs, binary tree, top 150

# constraints
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1

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
def avg_levels(root):
    queue = deque([root])
    ans = []

    while queue:
        current_len = len(queue)

        level_sum = 0

        for _ in range(current_len):
            node = queue.popleft()

            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        ans.append(level_sum/current_len)

    return ans

# TODO: add unit tests & solve recursively

if __name__ == '__main__':
    sys.exit(unittest.main())
