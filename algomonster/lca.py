#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: dfs, binary tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity:
# run-time: O(n)
# space: O(n)
def lca(root: Node, node1: Node, node2: Node) -> Node:
    if not root:
        return None

    # 1) p or q is root
    if root == node1 or root == node2:
        return root

    # 2) p is in left subtree, q is in right subtree
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left and right:
        return root

    # 3) p & q in same subtree
    if left:
        return left
        
    return right

class TestLCA(unittest.TestCase):
    def test_lca(self):
        # Test case 1
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(lca(root, root.left, root.right), root)

        # Test case 2
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertEqual(lca(root, root.left.left, root.left.right), root.left)

        # Test case 3
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(lca(root, root.right.left, root.right.right), root.right)

        # Test case 4
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)
        self.assertEqual(lca(root, root.left.left.left, root.left.left.right), root.left.left)

        # Test case 5
        root.right.right.left = Node(10)
        root.right.right.right = Node(11)
        self.assertEqual(lca(root, root.right.right.left, root.right.right.right), root.right.right)

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def find_node(root, target):
    if not root:
        return None
    if root.val == target:
        return root
    return find_node(root.left, target) or find_node(root.right, target)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    s = input().split()
    root = build_tree(iter(s), int)
    node1 = find_node(root, int(input()))
    node2 = find_node(root, int(input()))
    ans = lca(root, node1, node2)
    if not ans:
        print("null")
    else:
        print(ans.val)