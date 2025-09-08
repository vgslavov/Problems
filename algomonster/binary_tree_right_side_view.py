#!/usr/bin/env python3

import argparse
from collections import deque
import sys
import unittest

# tags: bfs, tree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution: iterative bfs
# complexity:
# run-time: O(n)
# space: O(n)
def binary_tree_right_side_view(root: Node) -> list[int]:
    if not root:
        return []

    queue = deque([root])
    ans = []

    while queue:
        n = len(queue)

        for _ in range(n):
            node = queue.popleft()

            curr = node.val
        
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
            
        ans.append(curr)

    return ans

class TestBinaryTreeRightSideView(unittest.TestCase):
    def test_binary_tree_right_side_view(self):
        # Test case 1
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.right = Node(5)
        root.right.right = Node(4)
        expected = [1, 3, 4]
        self.assertEqual(binary_tree_right_side_view(root), expected)

        # Test case 2
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.right = Node(5)
        expected = [1, 3, 5]
        self.assertEqual(binary_tree_right_side_view(root), expected)

        # Test case 3
        root = None
        expected = []
        self.assertEqual(binary_tree_right_side_view(root), expected)

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
    res = binary_tree_right_side_view(root)
    print(" ".join(map(str, res)))