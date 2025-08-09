#!/usr/bin/env python3

import argparse
import sys
import unittest

# tags: binary search

# non-solution: buggy if peak is at index 0 or len(arr)-1
# complexity:
# run-time: O(log n)
# space: O(1)
def peak_of_mountain_array2(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = left + (right-left) // 2

        if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid-1] < arr[mid] and arr[mid] < arr[mid+1]:
            left = mid+1
        else:
            right = mid-1

    return 0

# solution: follow pattern
# complexity:
# run-time: O(log n)
# space: O(1)
def peak_of_mountain_array(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    boundary = 0

    while left <= right:
        mid = left + (right-left) // 2

        # found peak or it's to left
        if arr[mid] > arr[mid+1]:
            boundary = mid
            right = mid-1
        else:
            left = mid+1

    return boundary

class TestPeakOfMountainArray(unittest.TestCase):
    def test_example_1(self):
        arr = [1, 2, 1]
        self.assertEqual(peak_of_mountain_array(arr), 1)
        
    def test_example_2(self):
        arr = [0, 10, 5, 2]
        self.assertEqual(peak_of_mountain_array(arr), 1)

    def test_example_3(self):
        arr = [3, 4, 5, 1]
        self.assertEqual(peak_of_mountain_array(arr), 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run unit tests')
    args = parser.parse_args()

    if args.test:
        sys.exit(unittest.main(argv=[sys.argv[0]]))

    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)