#!/usr/bin/env python3

# number: 173
# title: Binary Search Tree Iterator
# url: https://leetcode.com/problems/binary-search-tree-iterator/
# section: binary tree general
# difficulty: medium
# tags: stack, tree, design, bst, binary tree, iterator

# constraints
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext, and next.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    # complexity
    # run-time: O(n)
    # space: O(n)
    def __init__(self, root: TreeNode):
        self.nodes = []
        self.index = -1
        self.dfs(root)

    # complexity
    # run-time: O(1)
    # space: O(n)
    def next(self) -> int:
        self.index += 1
        return self.nodes[self.index] if self.index < len(self.nodes) else -1

    # complexity
    # run-time: O(1)
    # space: O(n)
    def hasNext(self) -> bool:
        return self.index < len(self.nodes)-1

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.nodes.append(root.val)
        self.dfs(root.right)

# TODO: add unit tests & solve w/ O(log n) space

# Your BSTIterator object will be instantiated and called as such:
root = TreeNode(7)
obj = BSTIterator(root)
while obj.hasNext():
    print(obj.next())