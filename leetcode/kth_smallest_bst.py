#!/usr/bin/env python3

import sys
import unittest

# number: 230
# section: binary search tree
# difficulty: medium
# tags: tree, dfs, bst, binary tree, top 150

# constraints
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4

# complexity
# run-time: O(n)
# space: O(n)
def dfs(root, values):
    if not root:
        return

    left = dfs(root.left, values)
    values.append(root.val)
    right = dfs(root.right, values)

# solution: recursive in-order dfs
# complexity
# run-time: O(n)
# space: O(n)
def kth_smallest_bst(root, k):
    nums_sorted = []
    dfs(root, nums_sorted)

    for n in nums_sorted:
        k -= 1
        if not k:
            return n

    return None

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
