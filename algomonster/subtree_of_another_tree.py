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

def find_sub(root, sub_root):
    if not root:
        return None

    if root.val == sub_root.val:
        return root
   
    return find_sub(root.left, sub_root) or find_sub(root.right, sub_root)

def compare(root, sub_root):
    # both are leaves
    if not root and not sub_root:
        return True
    # one ended earlier than the other
    elif not root or not sub_root:
        return False

    if root.val != sub_root.val:
        return False

    return compare(root.left, sub_root.left) and compare(root.right, sub_root.right)
    
# solution: recursive dfs
# complexity:
# run-time: O(m*n)?
# space: O(m+n)?
def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    if not root and not sub_root:
        return True
    elif not root or not sub_root:
        return False

    sub = find_sub(root, sub_root)

    # didn't find subtree's root
    if not sub:
        return False

    return compare(sub, sub_root)

def is_same_tree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return (tree1.val == tree2.val and is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right))

# solution: AlgoMonster recursive dfs
# complexity:
# run-time: O(m*n)
# space: O(m+n)
def subtree_of_another_tree2(root: Node, sub_root: Node) -> bool:
    if not root:
        return False
    return is_same_tree(root, sub_root) or subtree_of_another_tree2(root.left, sub_root) or subtree_of_another_tree2(root.right, sub_root)

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

class TestSubtreeOfAnotherTree(unittest.TestCase):
    def test_subtree_of_another_tree(self):
        # Test case 1: Simple case
        root = build_tree(iter("1 2 x x 3 x x".split()), int)
        sub_root = build_tree(iter("2 x x".split()), int)
        self.assertTrue(subtree_of_another_tree(root, sub_root))

        # Test case 2: Not a subtree
        sub_root = build_tree(iter("4 x x".split()), int)
        self.assertFalse(subtree_of_another_tree(root, sub_root))

        # Test case 3: Both trees are empty
        self.assertTrue(subtree_of_another_tree(None, None))

        # Test case 4: Root is a subtree of itself
        self.assertTrue(subtree_of_another_tree(root, root))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    root = build_tree(iter(input().split()), int)
    sub_root = build_tree(iter(input().split()), int)
    res = subtree_of_another_tree(root, sub_root)
    print("true" if res else "false")