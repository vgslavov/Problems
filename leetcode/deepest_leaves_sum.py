#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 1302
# title: Deepest Leaves Sum
# url: https://leetcode.com/problems/deepest-leaves-sum/
# section:
# difficulty: medium
# tags: tree, dfs, bfs, binary tree

# constraints
# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 100

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
def deepest_leaves_sum(root):
    queue = deque([root])

    while queue:
        current_len = len(queue)
        # reset sum on every level
        ans = 0

        for _ in range(current_len):
            node = queue.popleft()
            # count sum on every level
            ans += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    # sum on deepest level will not be reset
    return ans

if __name__ == '__main__':
    sys.exit(unittest.main())
