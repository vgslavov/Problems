#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: dfs, tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity:
# run-time: O(n)
# space: O(n)
def invert_binary_tree(tree: Node) -> Node:
    if not tree:
        return None

    tree.left, tree.right = tree.right, tree.left

    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
    
    return tree

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        # Test case 1: Simple tree
        tree = Node(1, Node(2), Node(3))
        inverted = invert_binary_tree(tree)
        self.assertEqual(inverted.val, 1)
        self.assertEqual(inverted.left.val, 3)
        self.assertEqual(inverted.right.val, 2)

        # Test case 2: Empty tree
        tree = None
        inverted = invert_binary_tree(tree)
        self.assertIsNone(inverted)

        # Test case 3: Tree with one node
        tree = Node(1)
        inverted = invert_binary_tree(tree)
        self.assertEqual(inverted.val, 1)
        self.assertIsNone(inverted.left)
        self.assertIsNone(inverted.right)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    tree = build_tree(iter(input().split()), int)
    res = invert_binary_tree(tree)
    print(" ".join(format_tree(res)))