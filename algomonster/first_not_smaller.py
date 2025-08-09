#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: binary search

def feasible(num, target):
    return num >= target

# complexity:
# run-time: O(log n)
# space: O(1)
def first_not_smaller(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)-1
    first = -1

    while left <= right:
        mid = (left+right) // 2

        if feasible(arr[mid], target):
            first = mid
            right = mid-1
        else:
            left = mid+1
            
    return first

class TestFirstNotSmaller(unittest.TestCase):
    def test_example_1(self):
        arr = [1, 3, 3, 5, 8, 8, 10]
        target = 5
        self.assertEqual(first_not_smaller(arr, target), 3)

    def test_example_2(self):
        arr = [1, 3, 3, 5, 8, 8, 10]
        target = 9
        self.assertEqual(first_not_smaller(arr, target), 6)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)