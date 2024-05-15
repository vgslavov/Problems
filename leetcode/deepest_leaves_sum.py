#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 100
def deepest_leaves_sum(root):
    queue = deque([root])

    while queue:
        current_len = len(queue)
        ans = 0

        for _ in range(current_len):
            node = queue.popleft()
            ans += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return ans

if __name__ == '__main__':
    sys.exit(unittest.main())
