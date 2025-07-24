#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 102
# title: Binary Tree Level Order Traversal
# url: https://leetcode.com/problems/binary-tree-level-order-traversal/
# section: binary tree bfs
# difficulty: medium
# tags: tree, bfs, binary tree, top 150, grind 75

# constraints
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

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
def level_order(root):
    if not root:
        return []

    queue = deque([root])

    ans = []

    while queue:
        level_len = len(queue)

        # or list comprehension
        #ans.append([node.val for node in queue])
        ans.append([])

        for _ in range(level_len):
            node = queue.popleft()

            ans[-1].append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return ans

if __name__ == '__main__':
    sys.exit(unittest.main())
