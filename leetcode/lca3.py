#!/usr/bin/env python3

import sys
import unittest

# number: 1650
# title: Lowest Common Ancestor of a Binary Tree III
# url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
# section: meta
# difficulty: medium
# tags: hash table, two pointers, tree, binary tree, meta

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

# solution: traverse
# complexity
# run-time: O(n)
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

if __name__ == '__main__':
    sys.exit(unittest.main())