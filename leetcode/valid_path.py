#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 1971
# title: Valid Path in a Graph
# url: https://leetcode.com/problems/valid-path-in-a-graph/
# section: graph
# difficulty: easy
# tags: dfs, bfs, union find, graph

# constraints:
# 1 <= n <= 2 * 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= u_i, v_i <= n - 1
# u_i != v_i
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.

# solution: recursive DFS
# complexity:
# run-time: O(n + e)
# space: O(n + e)
def valid_path(n, edges, source, destination) -> bool:
    if source == destination:
        return True

    graph = defaultdict(list)
    
    # build adjacency list
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node):
        # base case
        if node == destination:
            return True

        for neighbor in graph[node]:
            # skip seen
            if neighbor in seen:
                continue

            # visit
            #print(f"visiting: x={node}, y={neighbor}")
            seen.add(neighbor)

            # only return if True
            if dfs(neighbor):
                return True

        return False

    seen = {source}
    return dfs(source)

class TestValidPath(unittest.TestCase):
    def test_valid_path(self):
        self.assertTrue(valid_path(3, [[0,1],[1,2],[2,0]], 0, 2))
        self.assertFalse(valid_path(6, [[0,1],[1,2],[2,3],[4,5]], 0, 5))
        self.assertTrue(valid_path(5, [[0,1],[1,2],[2,3],[3,4]], 0, 4))
        self.assertFalse(valid_path(5, [[0,1],[1,2],[2,3],[3,4]], 0, 5))

    def test_valid_path_empty(self):
        self.assertTrue(valid_path(1, [], 0, 0))
        self.assertTrue(valid_path(1, [[0,0]], 0, 0))
        self.assertTrue(valid_path(1, [[0,1]], 0, 1))
        self.assertTrue(valid_path(1, [[1,0]], 1, 0))

    def test_invalid_path(self):
        self.assertFalse(valid_path(3, [[0,1],[1,2],[2,0]], 0, 3))
        self.assertFalse(valid_path(6, [[0,1],[1,2],[2,3],[4,5]], 0, 4))
        self.assertFalse(valid_path(5, [[0,1],[1,2],[2,3],[3,4]], 0, 5))
        self.assertFalse(valid_path(5, [[0,1],[1,2],[2,3],[3,4]], 1, 5))

if __name__ == "__main__":
    sys.exit(unittest.main())