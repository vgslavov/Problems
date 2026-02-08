#!/usr/bin/env python3

import argparse
from collections import deque
import sys
import unittest

# tags: bfs, graph

# solution: iterative bfs
# complexity:
# run-time: O(n+m)
# space: O(n)
# input: adjacency list
def shortest_path(graph: list[list[int]], a: int, b: int) -> int:
    def get_neighbors(node: int) -> list[int]:
        return graph[node]

    def bfs(start: int, end: int) -> int:
        # start node
        queue = deque([start])
        seen = {start}

        level = 0

        while queue:
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
        
                # found end node
                if node == end:
                    return level
        
                for neighbor in get_neighbors(node):
                    if neighbor in seen:
                        continue
        
                    seen.add(neighbor)
                    queue.append(neighbor)

            level += 1

        return -1

    return bfs(a, b)

class TestShortestPath(unittest.TestCase):
    def test_shortest_path(self):
        graph = [
            [1, 2],
            [0, 3, 4],
            [0, 5],
            [1],
            [1],
            [2]
        ]
        self.assertEqual(shortest_path(graph, 0, 4), 2)
        self.assertEqual(shortest_path(graph, 0, 5), 2)
        self.assertEqual(shortest_path(graph, 3, 4), 2)
        self.assertEqual(shortest_path(graph, 0, 0), 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)