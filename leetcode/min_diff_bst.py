#!/usr/bin/env python3

import math
import sys
import unittest

# number: 530
# section: binary search tree
# difficulty: easy
# tags: tree, dfs, bfs, binary search tree, binary tree, top 150

# constraints
# The number of nodes in the tree is in the range [2, 10^4].
# 0 <= Node.val <= 10^5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(n)
def dfs(node, values):
    if not node:
        return

    # in-order traversal produces sorted order in BST
    dfs(node.left, values)
    values.append(node.val)
    dfs(node.right, values)

def min_diff(root):
    values = []
    dfs(root, values)

    ans = math.inf
    for i in range(len(values)-1):
        ans = min(ans, values[i+1] - values[i])

    return ans

# TODO: add unit tests & solve iteratively using dfs

if __name__ == '__main__':
    sys.exit(unittest.main())
