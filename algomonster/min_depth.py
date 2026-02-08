#!/usr/bin/env python3

import argparse
from collections import deque
import sys
import unittest

# tags: bfs, tree
# leetcode: 111

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: iterative bfs
# complexity:
# run-time: O(n)
# space: O(n)
def min_depth(root: Node) -> int:
    if not root:
        return 0

    queue = deque([root])
    # 0-based depth
    depth = 0

    while queue:
        n = len(queue)

        for _ in range(n):
            node = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
     
        depth += 1

    return 0

class TestBinaryTreeMinDepth(unittest.TestCase):
    def test_binary_tree_min_depth(self):
        # Test case 1: Minimum depth is 1
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(min_depth(root), 1)

        # Test case 2: Minimum depth is 0
        root = Node(1)
        self.assertEqual(min_depth(root), 0)

        # Test case 3: Minimum depth is 2
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertEqual(min_depth(root), 2)

        # Test case 4: Empty tree
        root = None
        self.assertEqual(min_depth(root), 0)

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
    res = binary_tree_min_depth(root)
    print(res)