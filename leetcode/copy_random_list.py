#!/usr/bin/env python3

import sys
import unittest

# number: 138
# section: linked list
# difficulty: medium
# tags: linked list, hash table, top 150

# constraints
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random is null or is pointing to some node in the linked list.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# solution: dict of visited nodes
# complexity
# run-time: O(n)
# space: O(n)
def copy_random_list(head):
    def create_node(old):
        if not old:
            return None

        # visited
        if old in visited:
            return visited[old]

        # new
        new = Node(old.val)
        visited[old] = new

        return new

    if not head:
        return None

    visited = {}

    # use prev node
    new_head = new_node = Node(0)
    prev_node = None

    while head:
        new_node.next = create_node(head)

        # connect prev node
        if prev_node:
            prev_node.next = new_node
            prev_node = prev_node.next
        # bootstrap
        else:
            prev_node = new_node

        # go forth
        new_node = new_node.next

        # set random
        new_node.random = create_node(head.random)

        # iterate
        head = head.next

    return new_head.next

# TODO: solve recursively

# TODO: add unit tests

if __name__ == '__main__':
    sys.exit(unittest.main())
