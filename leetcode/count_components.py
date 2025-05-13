#!/usr/bin/env python3

from collections import defaultdict
import sys
import unittest

# number: 323
# title: Number of Connected Components in an Undirected Graph
# url: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# section: graph
# difficulty: medium
# tags: dfs, bfs, union find, graph

# constraints:
# 1 <= n <= 2 * 10^4
# 0 <= edges.length <= 2 * 10^4
# edges[i].length == 2
# 0 <= u_i, v_i <= n - 1
# u_i != v_i
# There are no duplicate edges.

# solution: recursive DFS
# complexity:
# run-time: O(n + e)
# space: O(n + e)
def count_components(n, edges) -> int:
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    # build adjacency list
    graph = defaultdict(list)

    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)

    ans = 0
    seen = set()

    for i in range(n):
        if i not in seen:
            ans += 1
            seen.add(i)
            dfs(i)

    return ans

class TestCountComponents(unittest.TestCase):
    def test_count_components(self):
        self.assertEqual(count_components(5, [[0, 1], [1, 2], [3, 4]]), 2)
        self.assertEqual(count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)
        self.assertEqual(count_components(5, []), 5)
        self.assertEqual(count_components(0, []), 0)
        self.assertEqual(count_components(1, []), 1)

if __name__ == "__main__":
    sys.exit(unittest.main())