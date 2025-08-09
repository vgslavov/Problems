#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: binary search

# complexity:
# run-time: O(log n)
# space: O(1)
def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1

    return -1

class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binary Search Implementation")
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)