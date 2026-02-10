#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: dfs, tree
# leetcode: 110

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity
# run-time: O(n)
# space: O(h) average, O(n) worst if tree skewed
def max_depth(node):
    if not node:
        return 0

    return max(max_depth(node.left), max_depth(node.right))+1

# solution: recursive dfs
# complexity
# run-time: O(n^2)
# space: O(h) average, O(n) worst if tree skewed
def isbalanced(tree: Node) -> bool:
    if not tree:
        return True

    return (
        abs(max_depth(tree.left)-max_depth(tree.right)) <= 1
        and isbalanced(tree.left)
        and isbalanced(tree.right)
    )

# Returns -1 if is not a balanced binary tree. The height if it is.
def tree_height(tree):
    if not tree:
        return 0

    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)

    if left_height == -1 or right_height == -1:
        return -1
    elif abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1

# solution: AlgoMonster recursive dfs
# complexity
# run-time: O(n)
# space: O(h) average, O(n) worst if tree skewed
def isbalanced2(tree: Node) -> bool:
    return tree_height(tree) != -1

class TestIsBalanced(unittest.TestCase):
    def test_is_balanced(self):
        # Test case 1: Balanced tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertTrue(isbalanced(root))
        self.assertTrue(isbalanced2(root))

        # Test case 2: Unbalanced tree
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertFalse(isbalanced(root))
        self.assertFalse(isbalanced2(root))

        # Test case 3: Single node
        root = Node(1)
        self.assertTrue(isbalanced(root))
        self.assertTrue(isbalanced2(root))

        # Test case 4: Empty tree
        root = None
        self.assertTrue(isbalanced(root))
        self.assertTrue(isbalanced2(root))

        # Test case 5: Right heavy tree
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        self.assertFalse(isbalanced(root))
        self.assertFalse(isbalanced2(root))

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

    tree = build_tree(iter(input().split()), int)
    res = isbalanced(tree)
    print("true" if res else "false")