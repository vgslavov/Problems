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
def insert_bst(bst: Node, val: int) -> Node:
    if not bst:
        return Node(val)
    
    if val > bst.val:
        bst.right = insert_bst(bst.right, val)
    elif val < bst.val:
        bst.left = insert_bst(bst.left, val)
    
    return bst

class TestInsertBST(unittest.TestCase):
    def test_insert_bst(self):
        # Test case 1: Insert into empty tree
        bst = None
        bst = insert_bst(bst, 5)
        self.assertEqual(bst.val, 5)

        # Test case 2: Insert smaller value
        bst = insert_bst(bst, 3)
        self.assertEqual(bst.left.val, 3)

        # Test case 3: Insert larger value
        bst = insert_bst(bst, 7)
        self.assertEqual(bst.right.val, 7)

        # Test case 4: Insert duplicate value
        bst = insert_bst(bst, 5)
        self.assertEqual(bst.val, 5)
        self.assertEqual(bst.left.val, 3)
        self.assertEqual(bst.right.val, 7)

        # Test case 5: Insert into left subtree
        bst = insert_bst(bst, 2)
        self.assertEqual(bst.left.left.val, 2)

        # Test case 6: Insert into right subtree
        bst = insert_bst(bst, 6)
        self.assertEqual(bst.right.left.val, 6)

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    bst = build_tree(iter(input().split()), int)
    val = int(input())
    res = insert_bst(bst, val)
    print(" ".join(format_tree(res)))