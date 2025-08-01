#!/usr/bin/env python3

import sys
import unittest

# number: 1650
# title: Lowest Common Ancestor of a Binary Tree III
# url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
# section: meta
# difficulty: medium
# tags: hash table, two pointers, tree, binary tree, meta, me

# constraints
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q exist in the tree.

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def traverse(node, path):
    if not node.parent:
        path.add(node)
        return node

    path.add(node)

    return traverse(node.parent, path)

# solution: traverse + set
# complexity
# run-time: O(n), if unbalanced, O(log n) if balanced
# space: O(n)
def lca3(p: 'Node', q: 'Node') -> 'Node':
    path = set()
    root = traverse(p, path)

    if not root:
        return None

    while q:
        if q in path:
            return q

        q = q.parent

    return None

def traverse2(node, n):
    while node and n:
        node = node.parent
        n -= 1

    return node

def depth2(node):
    d = 0

    while node:
        node = node.parent
        d += 1

    return d

# solution: traverse + depth
# complexity
# run-time: O(n), if unbalanced, O(log n) if balanced
# space: O(1)
def lca3_2(p: 'Node', q: 'Node') -> 'Node':
    depth_p = depth2(p)
    depth_q = depth2(q)
    diff = abs(depth_p-depth_q)

    if depth_p > depth_q:
        p = traverse2(p, diff)
    elif depth_p < depth_q:
        q = traverse2(q, diff)

    while p and q:
        if p == q:
            return p

        p = p.parent
        q = q.parent

    return None

class TestLCA3(unittest.TestCase):
    def test_lca3(self):
        # Create a simple binary tree
        root = Node(1)
        p = Node(2)
        q = Node(3)
        root.left = p
        root.right = q
        p.parent = root
        q.parent = root

        self.assertEqual(lca3(p, q), root)
        self.assertEqual(lca3_2(p, q), root)

        # Test with a deeper tree
        r = Node(4)
        p.left = r
        r.parent = p

        self.assertEqual(lca3(r, q), root)
        self.assertEqual(lca3_2(r, q), root)

if __name__ == '__main__':
    sys.exit(unittest.main())