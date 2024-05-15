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

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
def zigzag_level_order(root):
    if not root:
        return []

    queue = deque([root])
    ans = []
    reverse = False

    while queue:
        current_len = len(queue)
        level = []

        for _ in range(current_len):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if reverse:
            level.reverse()

        reverse = not reverse

        if level:
            ans.append(level)

    return ans

if __name__ == '__main__':
    sys.exit(unittest.main())
