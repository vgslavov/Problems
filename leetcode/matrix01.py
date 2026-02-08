#!/usr/bin/env python3

from collections import deque
import copy
import sys
import unittest

# number: 542
# title: 01 Matrix
# url: https://leetcode.com/problems/01-matrix/
# section: graph
# difficulty: medium
# tags: bfs, array, matrix, graph, dp, grind 75

# constraints
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.

def get_neighbors(node, grid):
    row,col,steps = node
    delta_row = [-1,0,1,0]
    delta_col = [0,1,0,-1]

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]

        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
            # return as is, don't increment steps
            yield neighbor_row, neighbor_col, steps


# solution: multi-source iterative BFS
# complexity:
# run-time: O(m*n) for m x n matrix
# space: O(m*n)
def update_matrix(mat: list[list[int]]) -> list[list[int]]:
    def bfs():
        while queue:
            node = queue.popleft()

            for neighbor in get_neighbors(node, mat):
                next_row, next_col, steps = neighbor

                if (next_row, next_col) in seen:
                    continue

                seen.add((next_row, next_col))
                queue.append((next_row, next_col, steps+1))
                mat[next_row][next_col] = steps+1

    queue = deque()
    seen = set()

    # start with 0s as sources
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                # row, col, steps
                queue.append((r,c,0))
                seen.add((r,c))

    bfs()
    return mat

# solution: multi-source iterative DFS
# complexity:
# run-time: O(m*n) for m x n matrix
# space: O(m*n)
def update_matrix2(mat: list[list[int]]) -> list[list[int]]:
    def dfs():
        while stack:
            node = stack.pop()

            for neighbor in get_neighbors(node, mat):
                next_row, next_col, steps = neighbor
                if (next_row, next_col) in seen:
                    continue

                seen.add((next_row, next_col))
                stack.append((next_row, next_col, steps+1))
                mat[next_row][next_col] = steps+1

    stack = []
    seen = set()

    # start with 0s as sources
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                # row, col, steps
                stack.append((r,c,0))
                seen.add((r,c))

    dfs()
    return mat

class TestMatrix01(unittest.TestCase):
    
    def test_update_matrix(self):
        # can't test DFS solution: doesn't guarantee shortest path
        mat = [
            [0,0,0],
            [0,1,0],
            [1,1,1]
        ]
        expected = [
            [0,0,0],
            [0,1,0],
            [1,2,1]
        ]
        self.assertEqual(update_matrix(mat), expected)

        mat2 = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        expected2 = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        self.assertEqual(update_matrix(mat2), expected2)

    def test_update_matrix2(self):
        """Same expected outputs as update_matrix (correct 01 Matrix answer).
        Uses deepcopy because update_matrix2 mutates the input."""
        mat = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        expected = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        self.assertEqual(update_matrix2(copy.deepcopy(mat)), expected)

        # single cell
        self.assertEqual(update_matrix2(copy.deepcopy([[0]])), [[0]])

        # single row
        mat_row = [[0, 1, 1, 1]]
        self.assertEqual(update_matrix2(copy.deepcopy(mat_row)), [[0, 1, 2, 3]])

        # all zeros
        mat_zeros = [[0, 0], [0, 0]]
        self.assertEqual(update_matrix2(copy.deepcopy(mat_zeros)), [[0, 0], [0, 0]])

if __name__ == "__main__":
    sys.exit(unittest.main())