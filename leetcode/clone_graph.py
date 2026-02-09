#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 133
# title: Clone Graph
# url: https://leetcode.com/problems/clone-graph/
# section: graph
# difficulty: medium
# tags: graph, dfs, bfs, hash table, meta, grind 75

# constraints
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# solution: recursive DFS
# complexity
# run-time: O(V + E)
# space: O(V), not counting output
def clone_graph(node):
    def dfs(node):
        # base case
        if not node:
            return node

        # look up clone node given original node
        if node in visited:
            # either return the visited node
            return visited[node]

        # create a clone node and add it to visited
        clone_node = Node(node.val)
        visited[node] = clone_node

        # recursively clone all neighbors
        for neighbor in node.neighbors:
            # clone the neighbor's neighbors recursively
            # O(V) space for the recursion stack
            clone_node.neighbors.append(dfs(neighbor))

        # or the cloned node
        return clone_node

    # original node to cloned
    # O(V) space
    visited = {}
    return dfs(node)

# solution: iterative BFS
# complexity
# run-time: O(V + E)
# space: O(V), not counting output
def clone_graph2(node):
    def bfs(root):
        if not root:
            return None

        # O(V) space
        queue = deque([root])
        clone_root = Node(root.val)

        # key: old node, value: cloned node
        # O(V) space
        visited = {}
        visited[root] = clone_root

        while queue:
            node = queue.popleft()
            # invariant: every node in the queue is already in visited
            clone_node = visited[node]

            for neighbor in node.neighbors:
                # not cloned yet
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    # to process the neighbor's neighbors
                    queue.append(neighbor)

                clone_neighbor = visited[neighbor]
                # map neighbor's clone to node's clone
                clone_node.neighbors.append(clone_neighbor)

        return clone_root

    return bfs(node)

class TestCloneGraph(unittest.TestCase):
    def test_clone_graph(self):
        # Create a simple graph
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        cloned_graph = clone_graph(node1)

        # Check if the cloned graph has the same structure
        self.assertEqual(cloned_graph.val, 1)
        self.assertEqual(len(cloned_graph.neighbors), 2)
        self.assertEqual(cloned_graph.neighbors[0].val, 2)
        self.assertEqual(cloned_graph.neighbors[1].val, 4)

    def test_clone_graph2(self):
        # Create a simple graph
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        cloned_graph = clone_graph2(node1)

        # Check if the cloned graph has the same structure
        self.assertEqual(cloned_graph.val, 1)
        self.assertEqual(len(cloned_graph.neighbors), 2)
        self.assertEqual(cloned_graph.neighbors[0].val, 2)
        self.assertEqual(cloned_graph.neighbors[1].val, 4)


if __name__ == "__main__":
    sys.exit(unittest.main())