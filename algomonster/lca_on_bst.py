#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: dfs, bst

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: recursive dfs
# complexity:
# run-time: O(n)
# space: O(n)
def lca_on_bst(bst: Node, p: int, q: int) -> int:
    # 1) p and q in right subtree
    if p > bst.val and q > bst.val:
        return lca_on_bst(bst.right, p, q)
    # 2) p and q in left subtree
    elif p < bst.val and q < bst.val:
        return lca_on_bst(bst.left, p, q)
    # 3) p or q is root: check last
    else:
        return bst.val

class TestLCAOnBST(unittest.TestCase):
    def test_lca_on_bst(self):
        # Test case 1: LCA of 2 and 8
        bst = build_tree(iter("6 2 0 x x 4 3 x x 5 x x 8 7 x x 9 x x".split()), int)
        self.assertEqual(lca_on_bst(bst, 2, 8), 6)

        # Test case 2: LCA of 2 and 4
        self.assertEqual(lca_on_bst(bst, 2, 4), 2)

        # Test case 3: LCA of 3 and 5
        self.assertEqual(lca_on_bst(bst, 3, 5), 4)

        # Test case 4: LCA of 7 and 9
        self.assertEqual(lca_on_bst(bst, 7, 9), 8)

        # Test case 5: LCA of 2 and 3
        self.assertEqual(lca_on_bst(bst, 2, 3), 2)

        # Test case 6: LCA of 4 and 5
        self.assertEqual(lca_on_bst(bst, 4, 5), 4)

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

    bst = build_tree(iter(input().split()), int)
    p = int(input())
    q = int(input())
    res = lca_on_bst(bst, p, q)
    print(res)