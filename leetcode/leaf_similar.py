#!/usr/bin/env python3

import sys
import unittest

# number: 872
# section: assessments
# difficulty: easy
# tags: tree, dfs, binary tree, microsoft

# constraints
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# complexity
# run-time: O(n)
# space: O(n)
def dfs(self, root, leaves):
    if not root:
        return
    elif not root.left and not root.right:
        leaves.append(root.val)
        return

    self.dfs(root.left, leaves)
    self.dfs(root.right, leaves)

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(n)
def leaf_similar(root1, root2) -> bool:
    # both empty
    if not root1 and not root2:
        return True
    # one empty but not other
    elif not root1 or not root2:
        return False

    leaves1 = []
    self.dfs(root1, leaves1)

    leaves2 = []
    self.dfs(root2, leaves2)

    return leaves1 == leaves2

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
