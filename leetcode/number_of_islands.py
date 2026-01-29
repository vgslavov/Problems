#!/usr/bin/env python3

from collections import deque
import sys
import unittest

# number: 200
# title: Number of Islands
# url: https://leetcode.com/problems/number-of-islands/
# section: graph matrix
# difficulty: medium
# tags: array, bfs, dfs, union find, matrix, grind 75

# constraints
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# solution: iterative BFS
# complexity:
# run-time: O(m*n) for m x n grid
# space: O(m*n)
def number_of_islands(grid: list[list[str]]) -> int:
    def get_neighbors(node):
        row, col = node
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]

        for i in range(len(delta_row)):
            n_row = row + delta_row[i]
            n_col = col + delta_col[i]

            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                yield n_row, n_col

    def bfs(node):
        queue = deque([node])

        while queue:
            node = queue.popleft()

            for neighbor in get_neighbors(node):
                if skip(neighbor, '0'):
                    continue

                seen.add(neighbor)
                queue.append(neighbor)

    def skip(node, value):
        r,c = node
        return grid[r][c] == value or node in seen

    ans = 0
    seen = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if skip((row, col), '0'):
                continue

            seen.add((row, col))
            bfs((row, col))
            ans += 1

    return ans

# TODO: solve in O(m+n) space by reusing grid (w/o seen set)

class TestNumberOfIslands(unittest.TestCase):
    def test_example_1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        expected = 1
        self.assertEqual(number_of_islands(grid), expected)

    def test_example_2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        expected = 3
        self.assertEqual(number_of_islands(grid), expected)

    def test_example_3(self):
        grid = [
            ["1","0","1","1","0","1","1"]
        ]
        expected = 3
        self.assertEqual(number_of_islands(grid), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())