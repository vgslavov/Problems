#!/usr/bin/env python3

import argparse
from collections import deque
import sys
import unittest

# tags: bfs, graph, matrix

# solution: iterative BFS
# complexity:
# run-time: O(m*n) for m x n grid
# space: O(m*n)
def count_number_of_islands(grid: list[list[int]]) -> int:
    def get_neighbors(node):
        row, col = node
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]

        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]

            if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
                yield neighbor_row, neighbor_col

    def skip(node, value):
        row, col = node
        return grid[row][col] == value or node in seen
        
    def bfs(node):
        queue = deque([node])

        while queue:
            node = queue.popleft()

            for neighbor in get_neighbors(node):
                if skip(neighbor, 0):
                    continue

                queue.append(neighbor)
                seen.add(neighbor)

    ans = 0
    seen = set()
    
    # iterate over grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # skip 0s, only counting 1s
            if skip((row, col), 0):
                continue

            seen.add((row, col))
            bfs((row, col))
            ans += 1
            
    return ans

# TODO: solve in O(m+n) space by reusing grid (w/o seen set)

class TestCountNumberOfIslands(unittest.TestCase):
    def test_count_number_of_islands(self):
        grid = [
            [1,1,0,0,0],
            [1,1,0,0,1],
            [0,0,1,0,1],
            [0,0,0,1,1]
        ]
        self.assertEqual(count_number_of_islands(grid), 3)

        grid = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.assertEqual(count_number_of_islands(grid), 0)

        grid = [
            [1,1,0,0,0],
            [1,1,0,0,1],
            [0,0,1,0,1],
            [0,0,0,1,1]
        ]
        self.assertEqual(count_number_of_islands(grid), 3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)