#!/usr/bin/env python3

import argparse
import heapq
import sys
import unittest

# tags: heap

# solution: min heap
# complexity:
# run-time: O(n*log n)
# space: O(n)
def merge_k_sorted_lists2(lists: list[list[int]]) -> list[int]:
    heap = []
    ans = []

    # Add all elements to heap
    for l in lists:
        for n in l:
            heapq.heappush(heap, n)

    while heap:
        ans.append(heapq.heappop(heap))

    return ans

# solution: AlgoMonster min heap, uses sorting requirement
# complexity:
# run-time: O(n*log k)
# space: O(k)
def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    # min heap
    # values: value, list index, element index
    # maintains only k elements in heap at any time
    heap = []
    ans = []

    for i in range(len(lists)):
        if not lists[i]:
            continue

        # push first element of each list
        heapq.heappush(heap, (lists[i][0], i, 0))

    while heap:
        val, list_index, index = heapq.heappop(heap)
        index += 1
        ans.append(val)

        if index < len(lists[list_index]):
            heapq.heappush(heap, (lists[list_index][index], list_index, index))

    return ans

class TestMergeKSortedLists(unittest.TestCase):
    def test_merge_k_sorted_lists(self):
        self.assertEqual(merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
        self.assertEqual(merge_k_sorted_lists2([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])

        self.assertEqual(merge_k_sorted_lists([[], [], []]), [])
        self.assertEqual(merge_k_sorted_lists2([[], [], []]), [])

        self.assertEqual(merge_k_sorted_lists([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(merge_k_sorted_lists2([[1], [2], [3]]), [1, 2, 3])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(" ".join(map(str, res)))