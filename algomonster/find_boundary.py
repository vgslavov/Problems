#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: binary search

# complexity:
# run-time: O(log n)
# space: O(1)
def find_boundary2(arr: list[bool]) -> int:
    left = 0
    right = len(arr)-1

    # no equality
    while left < right:
        mid = left + (right-left)//2

        # if False, go right
        if not arr[mid]:
            left = mid+1
        else:
            right = mid

    if left < len(arr) and arr[left]:
        return left
        
    return -1

def feasible(arr: list[int], i: int) -> bool:
    return arr[i] == True

# solution: more generic, same as vanilla binary search
# complexity:
# run-time: O(log n)
# space: O(1)
def find_boundary(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1

    # preserve equality
    while left <= right:
        mid = (left + right) // 2

        if feasible(arr, mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index

class TestFindBoundary(unittest.TestCase):

    def test_find_boundary(self):
        self.assertEqual(find_boundary([False, False, True, True, True]), 2)
        self.assertEqual(find_boundary([False, False, False]), -1)
        self.assertEqual(find_boundary([True, True, True]), 0)
        self.assertEqual(find_boundary([False, True, True]), 1)
        self.assertEqual(find_boundary([False, False, False, True]), 3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)