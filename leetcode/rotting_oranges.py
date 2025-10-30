#!/usr/bin/env python3

from collections import deque
from enum import IntEnum
import sys
import unittest

# number: 994
# title: Rotting Oranges
# url: https://leetcode.com/problems/rotting-oranges/
# section: graph matrix
# difficulty: medium
# tags: array, bfs, matrix

# constraints
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

class Oranges(IntEnum):
    NONE = 0
    FRESH = 1
    ROTTEN = 2

# solution: iterative multi-source BFS
# complexity:
# run-time: O(m*n) for m x n grid
# space: O(m*n)
def rotting_oranges(grid: list[list[int]]) -> int:
    def get_neighbors(node):
        row, col = node
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]

        for i in range(len(delta_row)):
            n_row = row + delta_row[i]
            n_col = col + delta_col[i]

            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                if grid[n_row][n_col] == Oranges.FRESH:
                    yield n_row, n_col

    def skip(node, value):
        r,c = node
        return grid[r][c] == value or node in seen

    queue = deque() 
    seen = set()
    ans = 0
    fresh = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # count fresh
            if grid[row][col] == Oranges.FRESH:
                fresh += 1
            # enqueue rotten
            elif grid[row][col] == Oranges.ROTTEN:
                queue.append((row,col))

    # optimization: nothing to rot
    if fresh == 0:
        return 0

    # 1 level = 1 minute
    while queue and fresh > 0:
        n = len(queue)

        for _ in range(n):
            node = queue.popleft()

            for neighbor in get_neighbors(node):
                if skip(neighbor, Oranges.NONE):
                    continue

                nr,nc = neighbor
                grid[nr][nc] = Oranges.ROTTEN
                fresh -= 1
                seen.add(neighbor)
                queue.append(neighbor)

        ans += 1

    return ans if fresh == 0 else -1

class TestRottingOranges(unittest.TestCase):
    def test_example_1(self):
        grid = [
            [2,1,1],
            [1,1,0],
            [0,1,1]
        ]
        expected = 4
        self.assertEqual(rotting_oranges(grid), expected)

    def test_example_2(self):
        grid = [
            [2,1,1],
            [0,1,1],
            [1,0,1]
        ]
        expected = -1
        self.assertEqual(rotting_oranges(grid), expected)

    def test_example_3(self):
        grid = [
            [0,2]
        ]
        expected = 0
        self.assertEqual(rotting_oranges(grid), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())