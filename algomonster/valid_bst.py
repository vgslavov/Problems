#!/usr/bin/env python3

import argparse
import math
import sys
import unittest

# tags: dfs, tree, bst

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity:
# run-time: O(n)
# space: O(n)
def valid_bst(root: Node) -> bool:
    def dfs(node, left, right):
        # empty tree is valid
        if not node:
            return True

        # value has to be b/w left & right to be valid
        if node.val > right or node.val < left:
            return False

        # change search range: left to current & current to right
        return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
    return dfs(root, -math.inf, math.inf)

class TestValidBST(unittest.TestCase):
    def test_valid_bst(self):
        # Test case 1: Valid BST
        root = Node(2, Node(1), Node(3))
        self.assertTrue(valid_bst(root))

        # Test case 2: Invalid BST
        root = Node(5, Node(1), Node(4, Node(3), Node(6)))
        self.assertFalse(valid_bst(root))

        # Test case 3: Empty tree
        root = None
        self.assertTrue(valid_bst(root))

        # Test case 4: Single node
        root = Node(10)
        self.assertTrue(valid_bst(root))

        # Test case 5: Left skewed tree
        root = Node(3, Node(2, Node(1)))
        self.assertTrue(valid_bst(root))

        # Test case 6: Right skewed tree
        root = Node(1, None, Node(2, None, Node(3)))
        self.assertTrue(valid_bst(root))

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
    res = valid_bst(root)
    print("true" if res else "false")