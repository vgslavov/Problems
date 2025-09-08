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

# solution: iterative bfs + deque
# complexity:
# run-time: O(n)
# space: O(n)
def zig_zag_traversal(root: Node) -> list[list[int]]:
    if not root:
        return []

    queue = deque([root])
    ans = []
    reverse = False

    while queue:
        n = len(queue)
        curr = deque()

        for _ in range(n):
            node = queue.popleft()

            if reverse:
                curr.appendleft(node.val)
            else:
                curr.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        # w/o deque
        #if reverse:
        #    curr.reverse()

        reverse = not reverse
        ans.append(list(curr))

    return ans

class TestZigZagTraversal(unittest.TestCase):
    def test_zig_zag_traversal(self):
        # Test case 1
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        expected = [[1], [3, 2], [4, 5, 6, 7]]
        self.assertEqual(zig_zag_traversal(root), expected)

        # Test case 2
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        expected = [[1], [3, 2], [4, 5]]
        self.assertEqual(zig_zag_traversal(root), expected)

        # Test case 3
        root = None
        expected = []
        self.assertEqual(zig_zag_traversal(root), expected)

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
    res = zig_zag_traversal(root)
    for row in res:
        print(" ".join(map(str, row)))