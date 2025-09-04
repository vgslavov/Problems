#!/usr/bin/env python3

import argparse
from collections import deque
import sys
import unittest

# tags: bfs

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: iterative bfs
# complexity:
# run-time: O(n)
# space: O(n)
def level_order_traversal(root: Node) -> list[list[int]]:
    queue = deque([root])
    ans = []

    while queue:
        n = len(queue)
        curr = []

        for _ in range(n):
            node = queue.popleft()

            curr.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        ans.append(curr)

    return ans

class TestLevelOrderTraversal(unittest.TestCase):
    def test_level_order_traversal(self):
        # Test case 1: Simple tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        expected = [[1], [2, 3]]
        self.assertEqual(level_order_traversal(root), expected)

        # Test case 2: More complex tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        expected = [[1], [2, 3], [4, 5]]
        self.assertEqual(level_order_traversal(root), expected)

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(" ".join(map(str, row)))