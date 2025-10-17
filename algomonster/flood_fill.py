#!/usr/bin/env python3

import argparse
from collections import deque
import sys
import unittest

# tags: bfs, graph, matrix

# complexity:
# run-time: O(m*n) for m x n image
# space: O(m*n), O(1) in place
def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]

        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]

            if 0 <= neighbor_row < len(image) and 0 <= neighbor_col < len(image[0]):
                # generator: yield only neighbors if they match the color of the root
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row, neighbor_col

    def bfs(root):
        r, c = root
        # save color: need to check neighbors' color
        color = image[r][c]

        # optimization: if color is same as replacement, no need to fill
        if color == replacement:
            return

        # fill root
        image[r][c] = replacement
 
        queue = deque([root])
        seen = set([root])
    
        while queue:
            node = queue.popleft()
    
            for neighbor in get_neighbors(node, color):
                if neighbor in seen:
                    continue

                nr, nc = neighbor
                image[nr][nc] = replacement
                seen.add(neighbor)
                queue.append(neighbor)

    bfs((r,c))
    return image

class TestFloodFill(unittest.TestCase):
    
    def test_flood_fill(self):
        image = [
            [1,1,1],
            [1,1,0],
            [1,0,1]
        ]
        expected = [
            [2,2,2],
            [2,2,0],
            [2,0,1]
        ]
        self.assertEqual(flood_fill(1, 1, 2, image), expected)

        image = [
            [0,0,0],
            [0,1,1]
        ]
        expected = [
            [0,0,0],
            [0,1,1]
        ]
        self.assertEqual(flood_fill(1, 1, 1, image), expected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(" ".join(map(str, row)))