#!/usr/bin/env python3

import argparse
import math
import sys
import unittest

# tags: dfs, tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: AlgoMonster recursive dfs
# complexity:
# run-time: O(n)
# space: O(h) average, O(n) worst
def visible_tree_node(root: Node) -> int:
    def dfs(node, max_so_far):
        if not node:
            return 0

        total = 0
        # current node is visible only if
        # greater than anything on the path from root to this node
        if node.val >= max_so_far:
            total += 1

        return (
            dfs(node.left, max(max_so_far, node.val)) + 
            dfs(node.right, max(max_so_far, node.val)) + 
            total
        )

    return dfs(root, -math.inf)

class TestVisibleTreeNode(unittest.TestCase):

    def test_visible_tree_node(self):
        # Test case 1: Simple tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(visible_tree_node(root), 3)

        # Test case 2: Some nodes visible
        root = Node(3)
        root.left = Node(2)
        root.right = Node(5)
        self.assertEqual(visible_tree_node(root), 2)

        # Test case 3: No nodes visible, except for root
        root = Node(1)
        root.left = Node(0)
        root.right = Node(-1)
        self.assertEqual(visible_tree_node(root), 1)

        # Test case 4: Complex tree
        root = Node(5)
        root.left = Node(3)
        root.right = Node(8)
        root.left.left = Node(1)
        root.left.right = Node(4)
        root.right.right = Node(9)
        self.assertEqual(visible_tree_node(root), 3)

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
    res = visible_tree_node(root)
    print(res)