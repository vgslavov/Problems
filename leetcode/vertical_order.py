#!/usr/bin/env python3

from collections import defaultdict, deque
import unittest
import sys

# number: 314
# title: Binary Tree Vertical Order Traversal
# difficulty: medium
# url: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# tags: hash table, tree, bfs, dfs, sorting, binary tree, meta

# constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: LeetCode iterative bfs
# complexity:
# run-time: O(n log n)
# space: O(n)
def vertical_order(root):
    if not root:
        return []
        
    # key: column index
    # value: list of node values
    col2val = defaultdict(list)

    # store index of column for each node
    # left child is col-1, right child is col+1
    queue = deque([(root,0)])
    col = 0

    while queue:
        size = len(queue)

        for _ in range(size):
            node, col = queue.popleft()
            col2val[col].append(node.val)

            if node.left:
                queue.append((node.left, col-1))

            if node.right:
                queue.append((node.right, col+1))

    return [col2val[k] for k in sorted(col2val.keys())]

class TestVerticalOrder(unittest.TestCase):
    def test_vertical_order(self):
        # Example 1
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20, TreeNode(15), TreeNode(7))
        self.assertEqual(vertical_order(root), [[9], [3, 15], [20], [7]])

        # Example 2
        root = TreeNode(1)
        root.left = TreeNode(2, None, TreeNode(4))
        root.right = TreeNode(3, None, TreeNode(5))
        self.assertEqual(vertical_order(root), [[2], [1, 4], [3], [5]])

        # Edge case: empty tree
        self.assertEqual(vertical_order(None), [])

if __name__ == "__main__":
    sys.exit(unittest.main())