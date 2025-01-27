#!/usr/bin/env python3

from collections import deque

# number: 117
# section: binary tree
# difficulty: medium
# tags: linked list, tree, dfs, bfs, binary tree

# constraints
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# solution: iterative bfs
# complexity
# run-time: O(n)
# space: O(n)
def connect(root):
    if not root:
        return None

    queue = deque([root])

    while queue:
        size = len(queue)
        prev_node = None

        for _ in range(size):
            node = queue.popleft()

            # link each node to previous one on the same level
            if prev_node:
                prev_node.next = node

            prev_node = node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return root
