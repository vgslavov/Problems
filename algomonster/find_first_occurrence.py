#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: binary search

# complexity:
# run-time: O(log n)
# space: O(1)
def find_first_occurrence(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)-1
    first = -1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == target:
            first = mid
            right = mid-1
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    
    return first

class TestFindFirstOccurrence(unittest.TestCase):
    def test_example_1(self):
        arr = [1, 2, 2, 2, 3, 4, 5]
        target = 2
        self.assertEqual(find_first_occurrence(arr, target), 1)

    def test_example_2(self):
        arr = [1, 1, 1, 1, 1]
        target = 1
        self.assertEqual(find_first_occurrence(arr, target), 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)