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
def serialize(root):
    def dfs(node, tree):
        if not node:
            tree.append('x')
            return

        tree.append(str(node.val))
        dfs(node.left, tree)
        dfs(node.right, tree)

    tree = []
    dfs(root, tree)
    return ' '.join(tree)

def deserialize(s):
    def dfs(nodes):
        val = next(nodes)

        if not val or val == 'x':
            return None

        node = Node(val)
        node.left = dfs(nodes)
        node.right = dfs(nodes)

        return node

    return dfs(iter(s.split()))

class TestSerializeDeserialize(unittest.TestCase):
    def test_serialize(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(serialize(root), "1 2 x x 3 x x")

    def test_deserialize(self):
        s = "1 2 x x 3 x x"
        root = deserialize(s)
        self.assertEqual(root.val, '1')
        self.assertEqual(root.left.val, '2')
        self.assertEqual(root.right.val, '3')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    def build_tree(nodes):
        val = next(nodes)
        if not val or val == "x":
            return None
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur

    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)

    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print(" ".join(print_tree(new_root)))