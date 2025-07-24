#!/usr/bin/env python3

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

# solution: recursive dfs
# complexity
# run-time: O(V + E)
# space: O(V)
def clone_graph(node):
    def dfs(node):
        # base case
        if not node:
            return node

        # look up clone node given original node
        if node in visited:
            return visited[node]

        # create a clone node and add it to visited
        clone_node = Node(node.val, [])
        visited[node] = clone_node

        # recursively clone all neighbors
        for neighbor in node.neighbors:
            clone_node.neighbors.append(dfs(neighbor))

        return clone_node

    # original node to cloned
    visited = {}
    return dfs(node)

# TODO: solve using bfs

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

        cloned_graph = cloneGraph(node1)

        # Check if the cloned graph has the same structure
        self.assertEqual(cloned_graph.val, 1)
        self.assertEqual(len(cloned_graph.neighbors), 2)
        self.assertEqual(cloned_graph.neighbors[0].val, 2)
        self.assertEqual(cloned_graph.neighbors[1].val, 4)

if __name__ == "__main__":
    sys.exit(unittest.main())