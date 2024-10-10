#!/usr/bin/env python3

from collections import deque
import math
import sys
import unittest

# number: 515
# section: assessments
# difficulty: medium
# tags: tree, dfs, bfs, binary tree, meta

# constraints
# The number of nodes in the tree will be in the range [0, 10^4].
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
def largest_values_tree(root):
    if not root:
        return []

    queue = deque([root])
    ans = []

    while queue:
        row_max = -math.inf
        row_len = len(queue)

        for _ in range(row_len):
            node = queue.popleft()
            row_max = max(row_max, node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        ans.append(row_max)

    return ans

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
