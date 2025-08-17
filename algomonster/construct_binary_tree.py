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

# solution: LeetCode recursive dfs + dict
# complexity:
# run-time: O(n)
# space: O(n)
def construct_binary_tree(preorder: list[int], inorder: list[int]) -> Node:
    def array2tree(left, right):
        # base case
        if left > right:
            return None

        # global
        nonlocal preorder_i

        # identify the root from the preorder array
        root_val = preorder[preorder_i]
        # create new node
        root = Node(root_val)

        preorder_i += 1

        # find root's index in inorder
        root_i = val2index[root_val]

        # split tree, skip root
        root.left = array2tree(left, root_i-1)
        root.right = array2tree(root_i+1, right)

        return root
        
    val2index = {inorder[i]:i for i in range(len(inorder))}
    preorder_i = 0

    return array2tree(0, len(inorder)-1)

def build_tree_recursive(preorder_index: int, inorder_start: int, size: int, value_to_index: dict) -> Node | None:
    if size <= 0:
        return None

    root_value = preorder[preorder_index]
    inorder_root_index = value_to_index[root_value]
    left_subtree_size = inorder_root_index - inorder_start

    left_child = build_tree_recursive(preorder_index + 1, inorder_start, left_subtree_size, value_to_index)
    right_child = build_tree_recursive(preorder_index + 1 + left_subtree_size, inorder_root_index + 1, size - 1 - left_subtree_size, value_to_index)

    return Node(root_value, left_child, right_child)

# solution: AlgoMonster recursive dfs + dict
# complexity:
# run-time: O(n)
# space: O(n)
def construct_binary_tree2(preorder: list[int], inorder: list[int]) -> Node | None:
    value_to_index = {val: idx for idx, val in enumerate(inorder)}

    return build_tree_recursive(0, 0, len(preorder), value_to_index)

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

class TestConstructBinaryTree(unittest.TestCase):
    def test_construct_binary_tree(self):
        # Test case 1: Simple tree
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        tree = construct_binary_tree(preorder, inorder)
        self.assertEqual(tree.val, 1)
        self.assertEqual(tree.left.val, 2)
        self.assertEqual(tree.right.val, 3)

        # Test case 2: Tree with only left children
        preorder = [1, 2, 3, 4]
        inorder = [4, 3, 2, 1]
        tree = construct_binary_tree(preorder, inorder)
        self.assertEqual(tree.val, 1)
        self.assertEqual(tree.left.val, 2)
        self.assertEqual(tree.left.left.val, 3)
        self.assertEqual(tree.left.left.left.val, 4)

        # Test case 3: Tree with only right children
        preorder = [1, 2, 3, 4]
        inorder = [1, 2, 3, 4]
        tree = construct_binary_tree(preorder, inorder)
        self.assertEqual(tree.val, 1)
        self.assertEqual(tree.right.val, 2)
        self.assertEqual(tree.right.right.val, 3)
        self.assertEqual(tree.right.right.right.val, 4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]
    res = construct_binary_tree(preorder, inorder)
    print(" ".join(format_tree(res)))