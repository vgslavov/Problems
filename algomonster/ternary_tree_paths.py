#!/usr/bin/env python3

import argparse
import sys
import unittest

# leetcode: 257
# tags: dfs, tree

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def join_str(s1, s2):
    return '->'.join([s1, s2]) if s1 else s2

# solution: recursive dfs, string path
# complexity:
# run-time: O(n)
# space: O(n)
def ternary_tree_paths(root: Node) -> list[str]:
    def dfs(node, p):
        if not node:
            return
        elif not node.children:
            paths.append(join_str(p, str(node.val)))
            return

        p = join_str(p, str(node.val))
        for child in node.children:
            dfs(child, p)

    paths = []
    # don't pass paths, do use str for each path
    dfs(root, '')
    return paths

# solution: AlgoMonster* recursive dfs, popping path
# complexity:
# run-time: O(n)
# space: O(n)
def ternary_tree_paths2(root):
    # dfs helper function
    def dfs(node, p):
        if not node:
            return
        # exit condition: when a leaf node is reached, append the path to the results
        elif not node.children:
            p.append(str(node.val))
            paths.append('->'.join(p))
            p.pop()
            return

        # DFS on each non-null child
        for child in node.children:
            p.append(str(node.val))
            dfs(child, p)
            p.pop()

    paths = []
    dfs(root, [])
    return paths

class TestTernaryTreePaths(unittest.TestCase):
    def test_ternary_tree_paths(self):
        # Test case 1: Simple tree
        root = Node(1, [Node(2), Node(3, [Node(4)])])
        expected = ['1->2', '1->3->4']
        self.assertEqual(ternary_tree_paths(root), expected)
        self.assertEqual(ternary_tree_paths2(root), expected)

        # Test case 2: Single node
        root = Node(1)
        expected = ['1']
        self.assertEqual(ternary_tree_paths(root), expected)
        self.assertEqual(ternary_tree_paths2(root), expected)

        # Test case 3: Empty tree
        root = None
        expected = []
        self.assertEqual(ternary_tree_paths(root), expected)
        self.assertEqual(ternary_tree_paths2(root), expected)

        # Test case 4: More complex tree
        root = Node(1, [Node(2, [Node(5), Node(6)]), Node(3), Node(4)])
        expected = ['1->2->5', '1->2->6', '1->3', '1->4']
        self.assertEqual(ternary_tree_paths(root), expected)
        self.assertEqual(ternary_tree_paths2(root), expected)

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)