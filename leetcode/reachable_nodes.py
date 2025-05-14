#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 2368
# title: Reachable Nodes With Restrictions
# url: https://leetcode.com/problems/reachable-nodes-with-restrictions/
# section: graph
# difficulty: medium
# tags: array, hash table, dfs, bfs, union find, graph

# constraints:
# 2 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= a_i, b_i < n
# a_i != b_i
# edges represents a valid tree.
# 1 <= restricted.length < n
# 1 <= restricted[i] < n
# All the values of restricted are unique.


# solution: recursive DFS
# complexity:
# run-time: O(n + e)
# space: O(n + e)
def reachable_nodes(n, edges, restricted) -> int:
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in restricted and neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    graph = defaultdict(list)

    # build adjacency list
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)

    seen = {0}
    restricted = set(restricted)
    dfs(0)
    return len(seen)


class TestReachableNodes(unittest.TestCase):
    def test_reachable_nodes(self):
        self.assertEqual(reachable_nodes(7, [[0, 1], [0, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]), 4)
        self.assertEqual(reachable_nodes(7, [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1]), 3)

if __name__ == "__main__":
    sys.exit(unittest.main())