#!/usr/bin/env python3

import argparse
import heapq
import sys
import unittest

# tags: heap

# solution: max heap
# complexity:
# run-time: O(n^2 * log k)
# space: O(k)
def find_k_smallest(matrix: list[list[int]], k: int) -> int:
    heap = []
    
    for row in matrix:
        for col in row:
            heapq.heappush(heap, -col)

            if len(heap) > k:
                heapq.heappop(heap)

    return -heap[0]

# solution: AlgoMonster min heap
# complexity:
# run-time: O(n+k*log n)
# space: O(n)
# TODO: understand better
def find_k_smallest2(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)

    # Keeps track of items in the heap, and their row and column numbers
    heap = [(matrix[0][0], 0, 0)]

    # Keeps track of the top of each row that is not processed
    column_top = [0] * n

    # Keeps track of the first number each row not processed
    row_first = [0] * n

    # Repeat the process k - 1 times.
    while k > 1:
        k -= 1
        _, row, column = heapq.heappop(heap)
        row_first[row] = column + 1

        # Add the item on the right to the heap if everything above it is processed
        if column + 1 < n and column_top[column + 1] == row:
            heapq.heappush(heap, (matrix[row][column + 1], row, column + 1))

        column_top[column] = row + 1

        # Add the item below it to the heap if everything before it is processed
        if row + 1 < n and row_first[row + 1] == column:
            heapq.heappush(heap, (matrix[row + 1][column], row + 1, column))

    return heap[0][0]

class TestKthSmallest(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_k_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13)
        self.assertEqual(find_k_smallest2([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13)

        self.assertEqual(find_k_smallest([[1, 2], [1, 3]], 2), 1)
        self.assertEqual(find_k_smallest2([[1, 2], [1, 3]], 2), 1)

        self.assertEqual(find_k_smallest([[1]], 1), 1)
        self.assertEqual(find_k_smallest2([[1]], 1), 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = find_k_smallest(matrix, k)
    print(res)