#!/usr/bin/env python3

import sys
import unittest

# number: 112
# section: binary tree general
# difficulty: easy
# tags: tree, dfs, bfs, binary tree, top 150

# constraints
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root, target_sum, cur_sum):
    if not root:
        return False
    elif not root.left and not root.right:
        return target_sum == cur_sum + root.val

    cur_sum += root.val

    return dfs(root.left, target_sum, cur_sum) or \
           dfs(root.right, target_sum, cur_sum)

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(n)
def path_sum(root, target_sum):
    return dfs(root, target_sum, 0)

# TODO: add unit tests & solve using iterative dfs
# test 1
# root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
# target_sum = 22
# expected = True
#
# test 2
# root = [1,2,3]
# target_sum = 5
# expected = False
#
# test 3
# root = []
# target_sum = 0
# expected = False
#
# test 4
# root = [1,2]
# target_sum = 1
# expected = False
#
# test 5
# root = [1]
# target_sum = 1
# expected = True
#
# test 6
# root = [1,2]
# target_sum = 2
# expected = False
#
# test 7
# root = [1,2,null,3,null,4,null,5]
# target_sum = 6
# expected = False

if __name__ == '__main__':
    return sys.exit(unittest.main())
