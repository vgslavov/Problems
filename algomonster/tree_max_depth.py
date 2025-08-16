#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: tree, dfs

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(h) average, O(n) worst if tree skewed
def tree_max_depth(root: Node) -> int:
    def dfs(node):
        if not node:
            return 0
    
        return max(dfs(node.left), dfs(node.right)) + 1

    # count edges, not nodes
    return dfs(root)-1 if root else 0

class TestMaxDepth(unittest.TestCase):
    def test_tree_max_depth(self):
        # Test case 1: Balanced tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertEqual(tree_max_depth(root), 2)

        # Test case 2: Unbalanced tree
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertEqual(tree_max_depth(root), 2)

        # Test case 3: Single node
        root = Node(1)
        self.assertEqual(tree_max_depth(root), 0)

        # Test case 4: Empty tree
        root = None
        self.assertEqual(tree_max_depth(root), 0)

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
    res = tree_max_depth(root)
    print(res)