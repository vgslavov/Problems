#!/usr/bin/env python3

from collections import deque
import copy
import sys
import unittest

# number: 733
# title: Flood Fill
# url: https://leetcode.com/problems/flood-fill/
# section: graph
# difficulty: easy
# tags: dfs, bfs, array, matrix, grind 75, graph

# constraints
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n

def get_neighbors(node, image, old_color):
    row, col = node
    delta_row = [-1,0,1,0]
    delta_col = [0,1,0,-1]

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]

        if 0 <= neighbor_row < len(image) and 0 <= neighbor_col < len(image[0]):
            # generator: yield only neighbors if they match the color of the root
            if image[neighbor_row][neighbor_col] == old_color:
                yield neighbor_row, neighbor_col

# solution: iterative BFS
# complexity:
# run-time: O(m*n) for m x n image
# space: O(m*n)
def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

    def bfs(root):
        r, c = root
        # save old color: need to check neighbors' color
        old_color = image[r][c]

        # optimization: if old color is same as new color, no need to fill
        if old_color == color:
            return

        # fill root
        image[r][c] = color

        queue = deque([root])
        seen = set([root])

        while queue:
            node = queue.popleft()

            for neighbor in get_neighbors(node, image, old_color):
                if neighbor in seen:
                    continue

                nr, nc = neighbor
                image[nr][nc] = color
                
                seen.add(neighbor)
                queue.append(neighbor)


    bfs((sr,sc))
    return image

# solution: recursive DFS
# complexity:
# run-time: O(m*n) for m x n image
# space: O(m*n)
def flood_fill2(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    def dfs(node, old_color):
        for neighbor in get_neighbors(node, image, old_color):
            if neighbor in seen:
                continue

            nr,nc = neighbor
            image[nr][nc] = color
            seen.add(neighbor)
            dfs(neighbor, old_color)

    root = (sr, sc)
    seen = set([root])
    old_color = image[sr][sc]

    # optimization: no changes
    if old_color == color:
        return image

    image[sr][sc] = color
    dfs(root, old_color)

    return image

class TestFloodFill(unittest.TestCase):
    
    def test_flood_fill(self):
        image = [
            [1,1,1],
            [1,1,0],
            [1,0,1]
        ]

        image2 = [row[:] for row in image]
        #image2 = copy.deepcopy(image)

        expected = [
            [2,2,2],
            [2,2,0],
            [2,0,1]
        ]
        self.assertEqual(flood_fill(image, 1, 1, 2), expected)
        self.assertEqual(flood_fill2(image2, 1, 1, 2), expected)

    def test_flood_fill_no_change(self):
        image = [
            [0,0,0],
            [0,1,1]
        ]
        expected = [
            [0,0,0],
            [0,1,1]
        ]
        self.assertEqual(flood_fill(image, 1, 1, 1), expected)
        # no change to image, no need to deepcopy
        self.assertEqual(flood_fill2(image, 1, 1, 1), expected)

if __name__ == "__main__":
    sys.exit(unittest.main())